import algorithm
import helper
import os
import docstrings
import validation

# pylint: disable=too-many-locals
# pylint: disable=unused-argument


USE_INFORMED_PRIORS = bool(os.getenv('USE_INFORMED_PRIORS')) or False


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

    study_guide_alpha_and_beta, topic_alpha_and_beta = \
        _accumulate_score_and_attempts(
            study_guide_id_list, topic_id_list, questions)

    _add_weighted_alpha_and_beta(
        study_guide_alpha_and_beta, topic_alpha_and_beta,
        study_guide_id_list, topic_id_for_study_guide_id)

    if return_results:
        results_list = []
        for study_guide_id in study_guide_id_list:
            topic_id = topic_id_for_study_guide_id[study_guide_id]

            weighted_alpha = study_guide_alpha_and_beta[
                study_guide_id]['weighted_alpha']
            weighted_beta = study_guide_alpha_and_beta[
                study_guide_id]['weighted_beta']

            mastery = float(algorithm.calculate_beta_distribution_mean(
                weighted_alpha, weighted_beta))

            mastery_band, band_confidence = algorithm.calculate_mastery_band_and_confidence(
                mastery, weighted_alpha, weighted_beta)

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
            study_guide_id_list, study_guide_alpha_and_beta)

        response['nextQuestion'] = algorithm.choose_next_question(
            topic_id_for_study_guide_id, study_guide_id_list,
            confidence_intervals_list, question_id_list)

    return _build_response(200, response)


def _add_weighted_alpha_and_beta(
    study_guide_alpha_and_beta, topic_alpha_and_beta,
        study_guide_id_list, topic_id_for_study_guide_id):

    for study_guide_id in study_guide_id_list:
        topic_id = topic_id_for_study_guide_id[study_guide_id]
        topic_alpha = topic_alpha_and_beta[topic_id]['alpha']
        topic_beta = topic_alpha_and_beta[topic_id]['beta']

        study_guide_alpha = study_guide_alpha_and_beta[study_guide_id]['alpha']
        study_guide_beta = study_guide_alpha_and_beta[study_guide_id]['beta']

        study_guide_weighting = algorithm.calculate_study_guide_weighting(
            study_guide_alpha, study_guide_beta, topic_alpha, topic_beta)

        study_guide_alpha_and_beta[study_guide_id]['weighted_alpha'] = \
            algorithm.calculate_weighted_value(
                study_guide_weighting, study_guide_alpha, topic_alpha)

        study_guide_alpha_and_beta[study_guide_id]['weighted_beta'] = \
            algorithm.calculate_weighted_value(
                study_guide_weighting, study_guide_beta, topic_beta)


@docstrings._accumulate_score_and_attempts
@validation._accumulate_score_and_attempts
def _accumulate_score_and_attempts(
        study_guide_id_list, topic_id_list, questions):

    topic_alpha_and_beta = _initialise_alpha_and_beta(
        topic_id_list)
    study_guide_alpha_and_beta = _initialise_alpha_and_beta(
        study_guide_id_list)

    for question in questions:
        _update_topic_alpha_and_beta(topic_alpha_and_beta, question)
        _update_study_guide_alpha_and_beta(
            study_guide_alpha_and_beta, question)

    return study_guide_alpha_and_beta, topic_alpha_and_beta


def _create_question_id_list(questions):
    question_id_list = [question['id'] for question in questions]
    return question_id_list


def _initialise_alpha_and_beta_results(study_guide_id_list, questions=[]):
    total_score = sum([question['isCorrect'] for question in questions])
    alpha_prior, beta_prior = 1., 1.

    if USE_INFORMED_PRIORS:
        informed_priors_params = helper.load_informed_priors()
        alpha_prior, beta_prior = informed_priors_params[total_score]

    alpha_and_beta = {
        key: {
            'alpha': alpha_prior,
            'beta': beta_prior
        } for key in study_guide_id_list
    }
    return alpha_and_beta


def _initialise_alpha_and_beta(study_guide_id_list):
    alpha_prior, beta_prior = 1., 1.
    alpha_and_beta = {
        key: {
            'alpha': alpha_prior,
            'beta': beta_prior
        } for key in study_guide_id_list
    }
    return alpha_and_beta


def _update_topic_alpha_and_beta(topic_alpha_and_beta, question):
    topic_id = question['topicId']
    score = question['isCorrect']

    topic_alpha_and_beta[topic_id]['alpha'] += score
    topic_alpha_and_beta[topic_id]['beta'] += 1 - score


def _update_study_guide_score_and_attempts(
        study_guide_alpha_and_beta, question):

    study_guide_id = question['studyGuideId']
    score = question['isCorrect']

    study_guide_alpha_and_beta[study_guide_id]['score'] += score
    study_guide_alpha_and_beta[study_guide_id]['attempts'] += 1.


def _update_study_guide_alpha_and_beta(study_guide_alpha_and_beta, question):
    study_guide_id = question['studyGuideId']
    score = question['isCorrect']

    study_guide_alpha_and_beta[study_guide_id]['alpha'] += score
    study_guide_alpha_and_beta[study_guide_id]['beta'] += 1 - score


def _build_response(code, body):
    return {
        'statusCode': code,
        'body': body
    }
