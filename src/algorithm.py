import random
import boto3
import numpy as np
from botocore import client
from scipy.optimize import fsolve
from scipy.stats import beta
from storage_client import StorageClient
import docstrings
import validation

client = StorageClient(boto3.client('s3', config=client.Config(max_pool_connections=50)))
BAND1_THRESHOLD = 0.34
BAND3_THRESHOLD = 0.66
CONFIDENCE_THRESHOLD = 0.6


def choose_initial_question(topic_id_for_study_guide_id, study_guide_id_list):
    study_guide_id = random.choice(study_guide_id_list)

    question_id_list = get_all_question_ids_from_guide(study_guide_id)

    question_id = random.choice(question_id_list)['id']

    question = _get_question_text(question_id, study_guide_id)

    question.update({
        "studyGuideId": study_guide_id,
        "topicId": topic_id_for_study_guide_id[study_guide_id]
    })

    return question


def get_all_question_ids_from_guide(study_guide_id):
    return client.select_all_question_ids(study_guide_id)


def _remove_completed_guide(
        study_guide_id, study_guide_id_list, confidence_intervals_list):

    index = study_guide_id_list.index(study_guide_id)

    filtered_study_guide_id_list = [guide_id for guide_id in study_guide_id_list
                                    if guide_id != study_guide_id]

    filtered_confidence_intervals_list = [confidence_interval
                                          for index_, confidence_interval
                                          in enumerate(confidence_intervals_list)
                                          if index_ != index]

    return filtered_study_guide_id_list, filtered_confidence_intervals_list


def _get_list_of_unasked_questions_from_guide(
        study_guide_id, question_id_list):
    return client.select_and_filter_question_ids(
        study_guide_id, question_id_list)


def choose_next_question(topic_id_for_study_guide_id, study_guide_id_list,
                         confidence_intervals_list, question_id_list):
    
    study_guide_id = _choose_next_study_guide_id(
        study_guide_id_list, confidence_intervals_list)

    filtered_question_id_list = _get_list_of_unasked_questions_from_guide(
        study_guide_id, question_id_list)

    if not filtered_question_id_list:
        filtered_study_guide_id_list, filtered_confidence_intervals_list = \
            _remove_completed_guide(
                study_guide_id, study_guide_id_list, confidence_intervals_list)

        return choose_next_question(
            topic_id_for_study_guide_id, filtered_study_guide_id_list,
            filtered_confidence_intervals_list, question_id_list)

    question_id = random.choice(filtered_question_id_list)['id']

    question = _get_question_text(question_id, study_guide_id)

    question.update({
        "studyGuideId": study_guide_id,
        "topicId": topic_id_for_study_guide_id[study_guide_id]
    })

    return question


def _get_question_text(question_id, study_guide_id):
    return client.select_question_by_id(question_id, study_guide_id)


def _choose_next_study_guide_id(study_guide_id_list, confidence_intervals_list):
    probabilities_list = _convert_confidence_interval_into_probability(
        confidence_intervals_list)

    return np.random.choice(a=study_guide_id_list, p=probabilities_list)


@docstrings.calculate_confidence_intervals_list
@validation.calculate_confidence_intervals_list
def calculate_confidence_intervals_list(
        study_guide_id_list, study_guide_alpha_and_beta):

    confidence_intervals_list = []
    for study_guide_id in study_guide_id_list:
        weighted_alpha = study_guide_alpha_and_beta[
            study_guide_id]['weighted_alpha']
        weighted_beta = study_guide_alpha_and_beta[
            study_guide_id]['weighted_beta']

        confidence_interval = calculate_confidence_interval(
            weighted_alpha, weighted_beta)

        confidence_intervals_list.append(confidence_interval)

    return confidence_intervals_list


@docstrings._convert_confidence_interval_into_probability
@validation._convert_confidence_interval_into_probability
def _convert_confidence_interval_into_probability(confidence_intervals):
    probabilities_list = [confidence_interval **
                          8 for confidence_interval in confidence_intervals]

    return _normalise_list(probabilities_list)


def _normalise_list(list_):
    return [element / sum(list_) for element in list_]


@docstrings.calculate_study_guide_weighting
@validation._calculate_study_guide_weighting
def calculate_study_guide_weighting(
        study_guide_alpha, study_guide_beta, topic_alpha, topic_beta):

    average_study_guide_mastery = calculate_beta_distribution_mean(
        study_guide_alpha, study_guide_beta)
    average_topic_mastery = calculate_beta_distribution_mean(
        topic_alpha, topic_beta)

    study_guide_weighting = _calculate_thompson_sampling(
        study_guide_alpha, study_guide_beta,
        topic_alpha, topic_beta)

    if average_study_guide_mastery < average_topic_mastery:
        study_guide_weighting = (1 - study_guide_weighting)

    return float(study_guide_weighting)


@docstrings.calculate_beta_distribution_mean
# @validation.calculate_beta_distribution_mean
def calculate_beta_distribution_mean(alpha, beta_):
    return alpha / (alpha + beta_)


def _thompson_sampling_integrand(
        mastery, study_guide_alpha, study_guide_beta,
        topic_alpha, topic_beta):

    topic_ability_equals_mastery = beta.pdf(
        mastery, topic_alpha, topic_beta)

    study_guide_ability_exceeds_mastery = \
        1 - _calculate_cumulative_probability(
            mastery, study_guide_alpha, study_guide_beta)

    return study_guide_ability_exceeds_mastery * topic_ability_equals_mastery


def _calculate_thompson_sampling(study_guide_alpha, study_guide_beta,
                                 topic_alpha, topic_beta):

    trapezium_edge_points = np.linspace(0, 1, 100)
    trapezium_heights = _thompson_sampling_integrand(
        trapezium_edge_points, study_guide_alpha, study_guide_beta,
        topic_alpha, topic_beta)

    return float(np.trapz(y=trapezium_heights, x=trapezium_edge_points))


@docstrings.calculate_weighted_value
@validation.calculate_weighted_value
def calculate_weighted_value(weighting, study_guide_value, topic_value):
    return weighting * study_guide_value \
        + (1 - weighting) * topic_value


def _5th_percentile_equation(mastery, alpha, beta_):
    return beta.cdf(mastery, alpha, beta_) - 0.05


def _calculate_5th_percentile(alpha, beta_):
    return fsolve(_5th_percentile_equation, x0=0,
                  args=(alpha, beta_), xtol=0.1)[0]


def _calculate_95th_percentile(alpha, beta_):
    return fsolve(_95th_percentile_equation, x0=1,
                  args=(alpha, beta_), xtol=0.1)[0]


def _95th_percentile_equation(mastery, alpha, beta_):
    return beta.cdf(mastery, alpha, beta_) - 0.95


@docstrings.calculate_confidence_interval
@validation.calculate_confidence_interval
def calculate_confidence_interval(alpha, beta_):
    _95th_percentile = _calculate_95th_percentile(alpha, beta_)
    _5th_percentile = _calculate_5th_percentile(alpha, beta_)
    return float(_95th_percentile - _5th_percentile)


def _calculate_cumulative_probability(mastery_threshold, alpha, beta_):
    return beta.cdf(mastery_threshold, alpha, beta_)


def _calculate_band1_confidence(alpha, beta_):
    return float(_calculate_cumulative_probability(BAND1_THRESHOLD, alpha, beta_))


def _calculate_band3_confidence(alpha, beta_):
    return float(1 - _calculate_cumulative_probability(BAND3_THRESHOLD, alpha, beta_))


def _calculate_band2_confidence(alpha, beta_):
    band_1_confidence = _calculate_cumulative_probability(
        BAND1_THRESHOLD, alpha, beta_)
    band_1_or_2_confidence = _calculate_cumulative_probability(
        BAND3_THRESHOLD, alpha, beta_)
    return float(band_1_or_2_confidence - band_1_confidence)


@docstrings._calculate_band_confidence
@validation._calculate_band_confidence
def _calculate_band_confidence(mastery_score, alpha, beta_):
    band = _place_mastery_in_band(mastery_score)
    if band == 1:
        return _calculate_band1_confidence(alpha, beta_)
    elif band == 3:
        return _calculate_band3_confidence(alpha, beta_)
    else:
        return _calculate_band2_confidence(alpha, beta_)


@docstrings._place_mastery_in_band
@validation._place_mastery_in_band
def _place_mastery_in_band(mastery_score):
    if mastery_score < BAND1_THRESHOLD:
        return 1
    elif mastery_score > BAND3_THRESHOLD:
        return 3
    else:
        return 2


@docstrings._calculate_confident_mastery_band
@validation._calculate_confident_mastery_band
def _calculate_confident_mastery_band(mastery_score, confidence):
    if confidence > CONFIDENCE_THRESHOLD:
        return _place_mastery_in_band(mastery_score)
    else:
        return 2


def calculate_mastery_band_and_confidence(mastery_score, alpha, beta_):
    confidence = _calculate_band_confidence(mastery_score, alpha, beta_)
    mastery_band = _calculate_confident_mastery_band(
        mastery_score, confidence)
    return mastery_band, confidence
