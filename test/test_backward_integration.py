import pytest
import algorithm
import index

from test.fixtures.accumulation import EXPECTED_ACCUMULATED_STUDY_GUIDE_ALPHA_AND_BETA,\
    EXPECTED_ACCUMULATED_TOPIC_ALPHA_AND_BETA, QUESTIONS_TO_TEST_ACCUMULATION,\
    STUDY_GUIDE_ID_LIST, TOPIC_ID_LIST, TOPIC_ID_FOR_STUDY_GUIDE_ID


# --------------------------------------------------------------
# Backward Integration tests on calculate_beta_distribution_mean
# --------------------------------------------------------------

@pytest.mark.bint_calculate_beta_distribution_mean
def test_calculate_beta_distribution_passes_with_weighted_values():
    study_guide_alpha, study_guide_beta, topic_alpha, topic_beta = 1., 1., 1., 1.
    weighted_alpha = algorithm.calculate_weighted_value(
        0.5, study_guide_alpha, topic_alpha)
    weighted_beta = algorithm.calculate_weighted_value(
        0.5, study_guide_beta, topic_beta)
    try:
        algorithm.calculate_beta_distribution_mean(
            weighted_alpha, weighted_beta)
        assert True
    except:
        assert False


@pytest.mark.bint_calculate_beta_distribution_mean
def test_calculate_study_guide_weighting_passes_when_calculating_weighted_values():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1., 1., 1.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert True
    except:
        assert False


# -----------------------------------------------------------
# Backward Integration tests on calculate_confidence_interval
# -----------------------------------------------------------

@pytest.mark.bint_calculate_confidence_interval
def test_calculate_confidence_interval_passes():
    study_guide_alpha_and_beta, topic_alpha_and_beta = \
        index._accumulate_score_and_attempts(
            STUDY_GUIDE_ID_LIST, TOPIC_ID_LIST, QUESTIONS_TO_TEST_ACCUMULATION)

    index._add_weighted_alpha_and_beta(
        study_guide_alpha_and_beta, topic_alpha_and_beta,
        STUDY_GUIDE_ID_LIST, TOPIC_ID_FOR_STUDY_GUIDE_ID)
    try:
        algorithm.calculate_confidence_intervals_list(
            STUDY_GUIDE_ID_LIST, study_guide_alpha_and_beta)
        assert True
    except:
        assert False
