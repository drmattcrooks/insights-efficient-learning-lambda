import pytest
import algorithm
import index
from index import _accumulate_score_and_attempts

from test.fixtures.accumulation import EXPECTED_ACCUMULATED_STUDY_GUIDE_ALPHA_AND_BETA,\
    EXPECTED_ACCUMULATED_TOPIC_ALPHA_AND_BETA, QUESTIONS_TO_TEST_ACCUMULATION,\
    STUDY_GUIDE_ID_LIST, TOPIC_ID_LIST


# ------------------------------------------------
# Functionality tests on accumulate_alpha_and_beta
# ------------------------------------------------

@pytest.mark.feature_accumulate_score_and_attempts
def test_accumulation_of_score_and_attempts_has_right_keys():
    study_guide_alpha_and_beta, topic_alpha_and_beta = \
        _accumulate_score_and_attempts(
            STUDY_GUIDE_ID_LIST, TOPIC_ID_LIST, QUESTIONS_TO_TEST_ACCUMULATION)
    assert set(study_guide_alpha_and_beta.keys()) == set(STUDY_GUIDE_ID_LIST)
    assert set(topic_alpha_and_beta.keys()) == set(TOPIC_ID_LIST)


@pytest.mark.feature_accumulate_score_and_attempts
def test_accumulation_of_score_and_attempts_has_float_alpha_and_beta():
    questions = QUESTIONS_TO_TEST_ACCUMULATION
    study_guide_id_list = [f"zg{i}" for i in range(1, 7)]
    topic_id_list = ['zt1', 'zt2']
    study_guide_alpha_and_beta, topic_alpha_and_beta = \
        _accumulate_score_and_attempts(
            study_guide_id_list, topic_id_list, questions)
    assert all([isinstance(guide_alpha_and_beta['alpha'], float)
                for guide_alpha_and_beta
                in study_guide_alpha_and_beta.values()])
    assert all([isinstance(guide_alpha_and_beta['beta'], float)
                for guide_alpha_and_beta
                in study_guide_alpha_and_beta.values()])
    assert all([isinstance(topic_alpha_and_beta_['alpha'], float)
                for topic_alpha_and_beta_
                in topic_alpha_and_beta.values()])
    assert all([isinstance(topic_alpha_and_beta_['beta'], float)
                for topic_alpha_and_beta_
                in topic_alpha_and_beta.values()])


@pytest.mark.feature_accumulate_score_and_attempts
def test_accumulation_of_score_and_attempts_has_nonnegative_alpha_and_beta():
    questions = QUESTIONS_TO_TEST_ACCUMULATION
    study_guide_id_list = [f"zg{i}" for i in range(1, 7)]
    topic_id_list = ['zt1', 'zt2']
    study_guide_alpha_and_beta, topic_alpha_and_beta = \
        _accumulate_score_and_attempts(
            study_guide_id_list, topic_id_list, questions)
    assert all([guide_alpha_and_beta['alpha'] >= 0
                for guide_alpha_and_beta
                in study_guide_alpha_and_beta.values()])
    assert all([guide_alpha_and_beta['beta'] >= 0
                for guide_alpha_and_beta
                in study_guide_alpha_and_beta.values()])
    assert all([topic_alpha_and_beta_['alpha'] >= 0
                for topic_alpha_and_beta_
                in topic_alpha_and_beta.values()])
    assert all([topic_alpha_and_beta_['beta'] >= 0
                for topic_alpha_and_beta_
                in topic_alpha_and_beta.values()])


# -------------------------------------------------------
# Functionality tests on calculate_beta_distribution_mean
# -------------------------------------------------------

@pytest.mark.functionality_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_1_out_of_1():
    weighted_score = 1.
    weighted_attempts = 1.
    weighted_alpha = 1 + weighted_score
    weighted_beta = 1 + weighted_attempts - weighted_score
    mastery = algorithm.calculate_beta_distribution_mean(
        weighted_alpha, weighted_beta)
    assert mastery == pytest.approx(0.66, abs=0.01)


@pytest.mark.functionality_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_1_out_of_2():
    weighted_score = 1.
    weighted_attempts = 2.
    weighted_alpha = 1 + weighted_score
    weighted_beta = 1 + weighted_attempts - weighted_score
    mastery = algorithm.calculate_beta_distribution_mean(
        weighted_alpha, weighted_beta)
    assert mastery == pytest.approx(0.5, abs=0.01)


@pytest.mark.functionality_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_0_out_of_1():
    weighted_score = 0.
    weighted_attempts = 1.
    weighted_alpha = 1 + weighted_score
    weighted_beta = 1 + weighted_attempts - weighted_score
    mastery = algorithm.calculate_beta_distribution_mean(
        weighted_alpha, weighted_beta)
    assert mastery == pytest.approx(0.33, abs=0.01)


# ----------------------------------------------------
# Functionality tests on calculate_confidence_interval
# ----------------------------------------------------

@pytest.mark.functionality_calculate_confidence_interval
def test_calculate_confidence_interval_0_out_of_0():
    weighted_score = 0.
    weighted_attempts = 0.
    weighted_alpha = 1. + weighted_score
    weighted_beta = 1. + weighted_attempts - weighted_score
    confidence = algorithm.calculate_confidence_interval(
        weighted_alpha, weighted_beta)
    assert confidence == pytest.approx(0.9, abs=0.01)


@pytest.mark.functionality_calculate_confidence_interval
def test_calculate_confidence_interval_1_out_of_1():
    weighted_score = 1.
    weighted_attempts = 1.
    weighted_alpha = 1. + weighted_score
    weighted_beta = 1. + weighted_attempts - weighted_score
    confidence = algorithm.calculate_confidence_interval(
        weighted_alpha, weighted_beta)
    assert confidence == pytest.approx(0.75, abs=0.01)
