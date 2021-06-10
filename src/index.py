import algorithm
import helper
import os

# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def handler(event, context):
    try:
        topic_id_list = event['topicIds']
        questions = event['questions']
        return_results = event['returnResults']
    except KeyError:
        raise Exception('[BAD REQUEST]: Invalid event')

    study_guide_id_list = helper.get_study_guide_id_list(
        topic_id_list)

    topic_id_for_study_guide_id = helper.get_topic_id(
        study_guide_id_list)

    response = {'nextQuestion': {},
                'results': []}

    if not questions:
        response['nextQuestion'] = algorithm.choose_initial_question(
            topic_id_for_study_guide_id, study_guide_id_list)

        return _build_response(200, response)

    question_id_list = _create_question_id_list(questions)

    study_guide_score_and_attempts, topic_score_and_attempts = \
        _accumulate_score_and_attempts(
            study_guide_id_list, topic_id_list, questions)

    _add_weighted_score_and_attempts(
        study_guide_score_and_attempts, topic_score_and_attempts,
        study_guide_id_list, topic_id_for_study_guide_id)

    if return_results:
        results_list = []
        for study_guide_id in study_guide_id_list:
            topic_id = topic_id_for_study_guide_id[study_guide_id]

            weighted_score = study_guide_score_and_attempts[
                study_guide_id]['weighted_score']
            weighted_attempts = study_guide_score_and_attempts[
                study_guide_id]['weighted_attempts']

            mastery = float(algorithm.calculate_beta_distribution_mean(
                weighted_score, weighted_attempts))

            mastery_band, band_confidence = algorithm.calculate_mastery_band_and_confidence(
                mastery, weighted_score, weighted_attempts)

            results_list.append({
                'studyGuideId': study_guide_id,
                'topicId': topic_id,
                'band': mastery_band,
                'masteryScore': mastery * 100,
                'confidenceScore': band_confidence * 100
            })

        response['results'] = results_list
    else:
        confidence_intervals_list = algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, study_guide_score_and_attempts)

        response['nextQuestion'] = algorithm.choose_next_question(
            topic_id_for_study_guide_id, study_guide_id_list,
            confidence_intervals_list, question_id_list)

    return _build_response(200, response)


def _add_weighted_score_and_attempts(
    study_guide_score_and_attempts, topic_score_and_attempts,
        study_guide_id_list, topic_id_for_study_guide_id):

    for study_guide_id in study_guide_id_list:
        topic_id = topic_id_for_study_guide_id[study_guide_id]
        topic_score = topic_score_and_attempts[topic_id]['score']
        topic_attempts = topic_score_and_attempts[topic_id]['attempts']

        study_guide_score = study_guide_score_and_attempts[study_guide_id]['score']
        study_guide_attempts = study_guide_score_and_attempts[study_guide_id]['attempts']

        study_guide_weighting = algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)

        study_guide_score_and_attempts[study_guide_id]['weighted_score'] = \
            algorithm.calculate_weighted_value(
                study_guide_weighting, study_guide_score, topic_score)

        study_guide_score_and_attempts[study_guide_id]['weighted_attempts'] = \
            algorithm.calculate_weighted_value(
                study_guide_weighting, study_guide_attempts, topic_attempts)


def _accumulate_score_and_attempts(
        study_guide_id_list, topic_id_list, questions):

    topic_score_and_attempts = _initialise_score_and_attempts(topic_id_list)
    study_guide_score_and_attempts = _initialise_score_and_attempts(
        study_guide_id_list)

    for question in questions:
        _update_topic_score_and_attempts(topic_score_and_attempts, question)
        _update_study_guide_score_and_attempts(
            study_guide_score_and_attempts, question)

    return study_guide_score_and_attempts, topic_score_and_attempts


def _create_question_id_list(questions):
    question_id_list = [question['id'] for question in questions]
    return question_id_list


def _initialise_score_and_attempts(list_):
    return {
        key: {
            'score': 0.,
            'attempts': 0.
        } for key in list_
    }


def _update_topic_score_and_attempts(topic_score_and_attempts, question):
    topic_id = question['topicId']
    score = question['isCorrect']

    topic_score_and_attempts[topic_id]['score'] += score
    topic_score_and_attempts[topic_id]['attempts'] += 1


def _update_study_guide_score_and_attempts(study_guide_score_and_attempts, question):
    study_guide_id = question['studyGuideId']
    score = question['isCorrect']

    study_guide_score_and_attempts[study_guide_id]['score'] += score
    study_guide_score_and_attempts[study_guide_id]['attempts'] += 1


def _build_response(code, body):
    return {
        'statusCode': code,
        'body': body
    }
