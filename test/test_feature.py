import pytest
import numpy as np
import algorithm
from index import _accumulate_score_and_attempts

from test.fixtures.accumulation import EXPECTED_ACCUMULATED_STUDY_GUIDE_ALPHA_AND_BETA,\
    EXPECTED_ACCUMULATED_TOPIC_ALPHA_AND_BETA, QUESTIONS_TO_TEST_ACCUMULATION,\
    STUDY_GUIDE_ID_LIST, TOPIC_ID_LIST


# ------------------------------------------
# Feature tests on accumulate_alpha_and_beta
# ------------------------------------------

@pytest.mark.functionality_accumulate_score_and_attempts
def test_accumulation_of_score_and_attempts():
    study_guide_alpha_and_beta, topic_alpha_and_beta = \
        _accumulate_score_and_attempts(
            STUDY_GUIDE_ID_LIST, TOPIC_ID_LIST, QUESTIONS_TO_TEST_ACCUMULATION)
    assert study_guide_alpha_and_beta == EXPECTED_ACCUMULATED_STUDY_GUIDE_ALPHA_AND_BETA
    assert topic_alpha_and_beta == EXPECTED_ACCUMULATED_TOPIC_ALPHA_AND_BETA


# -----------------------------------------
# Feature tests on calculate_weighted_value
# -----------------------------------------

@pytest.mark.feature_calculate_weighted_value
def test_calculate_weighted_value_returns_float():
    weighted_value = \
        algorithm.calculate_weighted_value(0.5, 1., 2.)
    assert isinstance(weighted_value, float)


@pytest.mark.feature_calculate_weighted_value
def test_calculate_weighted_value_between_study_guide_and_topic_value():
    weighting = 0.5
    study_guide_value = 1.
    topic_value = 2.
    weighted_value = \
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
    assert weighted_value >= study_guide_value
    assert weighted_value <= topic_value


@pytest.mark.feature_calculate_weighted_value
def test_calculate_weighted_value_is_study_guidewhen_weighting_is_1():
    weighting = 1.
    study_guide_value = 1.
    topic_value = 2.
    weighted_value = \
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
    assert weighted_value == study_guide_value


# ----------------------------------------------
# Feature tests on calculate_confidence_interval
# ----------------------------------------------

@pytest.mark.feature_calculate_confidence_interval
def test_calculate_confidence_interval_returns_float():
    confidence = \
        algorithm.calculate_confidence_interval(1., 2.)
    assert isinstance(confidence, float)


@pytest.mark.feature_calculate_confidence_interval
def test_calculate_confidence_interval_in_range_0_to_1():
    confidence = \
        algorithm.calculate_confidence_interval(1., 2.)
    assert confidence == pytest.approx(0.5, abs=0.5)


# ----------------------------------------------------
# Feature tests on calculate_confidence_intervals_list
# ----------------------------------------------------

@pytest.mark.feature_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_returns_list():
    study_guide_id_list = ['z1', 'z2']
    weighted_score_and_attempts = {
        'z1': {'weighted_alpha': 0.,
               'weighted_beta': 0.},
        'z2': {'weighted_alpha': 0.,
               'weighted_beta': 0.}
    }
    confidence_intervals_list = \
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
    assert isinstance(confidence_intervals_list, list)


@pytest.mark.feature_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_returns_floats():
    study_guide_id_list = ['z1', 'z2']
    weighted_score_and_attempts = {
        'z1': {'weighted_alpha': 10.,
               'weighted_beta': 10.},
        'z2': {'weighted_alpha': 0.,
               'weighted_beta': 10.}
    }
    confidence_intervals_list = \
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
    assert all([isinstance(confidence, float)
                for confidence in confidence_intervals_list])


@pytest.mark.feature_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_returns_floats_in_range_0_to_1():
    study_guide_id_list = ['z1', 'z2']
    weighted_score_and_attempts = {
        'z1': {'weighted_alpha': 10.,
               'weighted_beta': 10.},
        'z2': {'weighted_alpha': 0.,
               'weighted_beta': 10.}
    }
    confidence_intervals_list = \
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
    assert all([(confidence >= 0) & (confidence <= 1)
                for confidence in confidence_intervals_list])


# -------------------------------------------------------------
# Feature tests on convert_confidence_interval_into_probability
# -------------------------------------------------------------

@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_returns_list():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert isinstance(list_of_probabilities, list)


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_returns_floats():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert all([isinstance(probability, float) for probability in list_of_probabilities])


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_probabilities_nonnegative():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert all([probability >= 0 for probability in list_of_probabilities])


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_probabilities_sum_to_1():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert sum(list_of_probabilities) == 1


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_probabilities_monotonic():
    confidence_intervals = [2., 1., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert list_of_probabilities[2] == max(list_of_probabilities)
    assert list_of_probabilities[1] == min(list_of_probabilities)


# -------------------------------------------------
# Feature tests on calculate_beta_distribution_mean
# -------------------------------------------------

@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_returns_float():
    score = 1.
    attempts = 2.
    alpha = 1 + score
    beta_ = 1 + attempts - score
    mastery = algorithm.calculate_beta_distribution_mean(alpha, beta_)
    assert isinstance(mastery, float)


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_in_range_0_to_1():
    score = 1.
    attempts = 2.
    alpha = 1 + score
    beta_ = 1 + attempts - score
    mastery = algorithm.calculate_beta_distribution_mean(alpha, beta_)
    assert mastery == pytest.approx(0.5, abs=0.5)


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_is_half():
    score = 1.
    attempts = 2.
    alpha = 1 + score
    beta_ = 1 + attempts - score
    mastery = algorithm.calculate_beta_distribution_mean(alpha, beta_)
    assert mastery == 0.5


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_is_2_thirds():
    score = 1.
    attempts = 1.
    alpha = 1 + score
    beta_ = 1 + attempts - score
    mastery = algorithm.calculate_beta_distribution_mean(alpha, beta_)
    assert mastery == 2 / 3


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_is_1_thirds():
    score = 0.
    attempts = 1.
    alpha = 1 + score
    beta_ = 1 + attempts - score
    mastery = algorithm.calculate_beta_distribution_mean(alpha, beta_)
    assert mastery == 1 / 3


# -------------------------------------------------------------
# Feature tests on convert_confidence_interval_into_probability
# -------------------------------------------------------------

@pytest.mark.feature_place_mastery_in_band
def test_place_mastery_in_band_returns_1_2_3():
    mastery_scores = [float(mastery) for mastery in np.linspace(0, 1)]
    bands = [algorithm._place_mastery_in_band(mastery)
             for mastery in mastery_scores]
    assert all([band in [1, 2, 3] for band in bands])


@pytest.mark.feature_place_mastery_in_band
def test_place_mastery_in_band_returns_1_for_0_mastery():
    mastery = 0.
    band = algorithm._place_mastery_in_band(mastery)
    assert band == 1


@pytest.mark.feature_place_mastery_in_band
def test_place_mastery_in_band_returns_3_for_1_mastery():
    mastery = 1.
    band = algorithm._place_mastery_in_band(mastery)
    assert band == 3


# ------------------------------------------
# Feature tests on calculate_band_confidence
# ------------------------------------------

@pytest.mark.feature_calculate_band_confidence
def test_calculate_band_confidence_returns_float():
    confidence = algorithm._calculate_band_confidence(0.5, 1., 2.)
    assert isinstance(confidence, float)


@pytest.mark.feature_calculate_band_confidence
def test_calculate_band_confidence_in_range_0_to_1():
    confidence = algorithm._calculate_band_confidence(0.5, 1., 2.)
    assert confidence == pytest.approx(0.5, abs=0.5)


# ------------------------------------------
# Feature tests on calculate_confidence_band
# ------------------------------------------

@pytest.mark.feature_calculate_confident_mastery_band
def test_calculate_confident_mastery_band_is_1_2_or_3():
    mastery_scores = np.linspace(0, 1, 20)
    confidence_scores = np.linspace(0, 1, 20)
    for mastery in mastery_scores:
        for confidence in confidence_scores:
            band = algorithm._calculate_confident_mastery_band(
                float(mastery), float(confidence))
            assert band in [1, 2, 3]


@pytest.mark.feature_calculate_confident_mastery_band
def test_calculate_confident_mastery_band_confident_1():
    band = algorithm._calculate_confident_mastery_band(0., 1.)
    assert band == 1


@pytest.mark.feature_calculate_confident_mastery_band
def test_calculate_confident_mastery_band_confident_3():
    band = algorithm._calculate_confident_mastery_band(1., 1.)
    assert band == 3


@pytest.mark.feature_calculate_confident_mastery_band
def test_calculate_confident_mastery_band_unconfident_1():
    band = algorithm._calculate_confident_mastery_band(0., 0.)
    assert band == 2


@pytest.mark.feature_calculate_confident_mastery_band
def test_calculate_confident_mastery_band_unconfident_3():
    band = algorithm._calculate_confident_mastery_band(1., 0.)
    assert band == 2


# ------------------------------------------------
# Feature tests on calculate_study_guide_weighting
# ------------------------------------------------

@pytest.mark.feature_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_is_float():
    study_guide_score = 1.
    study_guide_attempts = 2.
    topic_score = 2.
    topic_attempts = 3.
    weighting = algorithm.calculate_study_guide_weighting(
        study_guide_score, study_guide_attempts, topic_score, topic_attempts)
    assert isinstance(weighting, float)


@pytest.mark.feature_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_in_range_0_to_1():
    study_guide_score = 1.
    study_guide_attempts = 2.
    topic_score = 2.
    topic_attempts = 3.
    weighting = algorithm.calculate_study_guide_weighting(
        study_guide_score, study_guide_attempts, topic_score, topic_attempts)
    assert weighting == pytest.approx(0.5, abs=0.5)


@pytest.mark.feature_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_1_when_much_better_at_guide():
    study_guide_alpha = 101.
    study_guide_beta = 1.
    topic_alpha = 101.
    topic_beta = 901.
    weighting = algorithm.calculate_study_guide_weighting(
        study_guide_alpha, study_guide_beta, topic_alpha, topic_beta)
    assert weighting == pytest.approx(1, rel=1e-6)


@pytest.mark.feature_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_1_when_much_worse_at_guide():
    study_guide_alpha = 1.
    study_guide_beta = 101.
    topic_alpha = 101.
    topic_beta = 1.
    weighting = algorithm.calculate_study_guide_weighting(
        study_guide_alpha, study_guide_beta, topic_alpha, topic_beta)
    assert weighting == pytest.approx(1, rel=1e-6)