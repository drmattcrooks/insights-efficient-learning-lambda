import pytest
import algorithm


# -------------------------------------------------------
# Functionality tests on calculate_beta_distribution_mean
# -------------------------------------------------------

@pytest.mark.functionality_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_1_out_of_1():
    weighted_score = 1.
    weighted_attempts = 1.
    mastery = algorithm.calculate_beta_distribution_mean(
        weighted_score, weighted_attempts)
    assert mastery == pytest.approx(0.66, abs=0.01)


@pytest.mark.functionality_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_1_out_of_2():
    weighted_score = 1.
    weighted_attempts = 2.
    mastery = algorithm.calculate_beta_distribution_mean(
        weighted_score, weighted_attempts)
    assert mastery == pytest.approx(0.5, abs=0.01)


@pytest.mark.functionality_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_0_out_of_1():
    weighted_score = 0.
    weighted_attempts = 1.
    mastery = algorithm.calculate_beta_distribution_mean(
        weighted_score, weighted_attempts)
    assert mastery == pytest.approx(0.33, abs=0.01)


# ----------------------------------------------------
# Functionality tests on calculate_confidence_interval
# ----------------------------------------------------

@pytest.mark.functionality_calculate_confidence_interval
def test_calculate_confidence_interval_0_out_of_0():
    weighted_score = 0.
    weighted_attempts = 0.
    confidence = algorithm.calculate_confidence_interval(
        weighted_score, weighted_attempts)
    assert confidence == pytest.approx(0.9, abs=0.01)


@pytest.mark.functionality_calculate_confidence_interval
def test_calculate_confidence_interval_1_out_of_1():
    weighted_score = 1.
    weighted_attempts = 1.
    confidence = algorithm.calculate_confidence_interval(
        weighted_score, weighted_attempts)
    assert confidence == pytest.approx(0.75, abs=0.01)
