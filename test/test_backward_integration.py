import pytest
import algorithm


# --------------------------------------------------------------
# Backward Integration tests on calculate_beta_distribution_mean
# --------------------------------------------------------------

@pytest.mark.bint_calculate_beta_distribution_mean
def test_calculate_beta_distribution_passes():
    weighted_score, weighted_attempts = algorithm.calculate_weighted_score_and_attempts(
        1., 1., 1., 1.)
    try:
        algorithm.calculate_beta_distribution_mean(
            weighted_score, weighted_attempts)
        assert True
    except:
        assert False


# -----------------------------------------------------------
# Backward Integration tests on calculate_confidence_interval
# -----------------------------------------------------------

@pytest.mark.bint_calculate_confidence_interval
def test_calculate_confidence_interval_passes():
    weighted_score, weighted_attempts = algorithm.calculate_weighted_score_and_attempts(
        1., 1., 1., 1.)
    try:
        algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert True
    except:
        assert False