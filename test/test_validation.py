import pytest
import algorithm


# -------------------------------------------------------------------
# Validation tests on algorithm.calculate_weighted_score_and_attempts
# -------------------------------------------------------------------

@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_weighting_is_float():
    weighting = 1
    study_guide_value = 1.
    topic_value = 1.
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"weighting should be a float, a {weighting.__class__.__name__} was provided"


@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_study_guide_value_is_float():
    weighting = 0.5
    study_guide_value = 1
    topic_value = 1.
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"study_guide_value should be a float, a {study_guide_value.__class__.__name__} was provided"


@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_topic_value_is_float():
    weighting = 0.5
    study_guide_value = 1.
    topic_value = 1
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"topic_value should be a float, a {topic_value.__class__.__name__} was provided"


@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_weighting_in_range_0_to_1():
    weighting = 5.
    study_guide_value = 1.
    topic_value = 1.
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"unexpected value encountered - weighted_score should be in the interval [0, 1]"


@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_study_guide_value_nonnegative():
    weighting = 0.5
    study_guide_value = -1.
    topic_value = 1.
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_value} < 0 : study_guide_value should be non-negative"


@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_topic_value_nonnegative():
    weighting = 0.5
    study_guide_value = 1.
    topic_value = -1.
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_value} < 0 : topic_value should be non-negative"


@pytest.mark.validation_calculate_weighted_value
def test_calculate_weighted_value_study_guide_value_lt_topic_value():
    weighting = 0.5
    study_guide_value = 2.
    topic_value = 1.
    try:
        algorithm.calculate_weighted_value(
            weighting, study_guide_value, topic_value)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_value} > {topic_value} : study_guide_value should be less than or equal to topic_value"


# -------------------------------------------------------------------
# Validation tests on algorithm.calculate_weighted_score_and_attempts
# -------------------------------------------------------------------

# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_typeerror_on_study_guide_score():
#     study_guide_score = 1
#     study_guide_attempts = 1.
#     topic_score = 1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'TypeError'
#         assert str(error) == f"study_guide_score should be an int or float, a {study_guide_score.__class__.__name__} was provided"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_typeerror_on_study_guide_attempts():
#     study_guide_score = 1.
#     study_guide_attempts = 1
#     topic_score = 1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'TypeError'
#         assert str(error) == f"study_guide_attempts should be an int or float, a {study_guide_attempts.__class__.__name__} was provided"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_typeerror_on_topic_score():
#     study_guide_score = 1.
#     study_guide_attempts = 1.
#     topic_score = 1
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'TypeError'
#         assert str(error) == f"topic_score should be an int or float, a {topic_score.__class__.__name__} was provided"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_typeerror_on_topic_attempts():
#     study_guide_score = 1.
#     study_guide_attempts = 1.
#     topic_score = 1.
#     topic_attempts = 1
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'TypeError'
#         assert str(error) == f"topic_attempts should be an int or float, a {topic_attempts.__class__.__name__} was provided"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_study_guide_score_nonnegative():
#     study_guide_score = -1.
#     study_guide_attempts = 1.
#     topic_score = 1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{study_guide_score} < 0 : study_guide_score should be non-negative"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_study_guide_attempts_nonnegative():
#     study_guide_score = 1.
#     study_guide_attempts = -1.
#     topic_score = 1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{study_guide_attempts} < 0 : study_guide_attempts should be non-negative"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_topic_score_nonnegative():
#     study_guide_score = 1.
#     study_guide_attempts = 1.
#     topic_score = -1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{topic_score} < 0 : topic_score should be non-negative"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_topic_attempts_nonnegative():
#     study_guide_score = 1.
#     study_guide_attempts = 1.
#     topic_score = 1.
#     topic_attempts = -1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{topic_attempts} < 0 : topic_attempts should be non-negative"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_study_guide_score_lt_attempts():
#     study_guide_score = 2.
#     study_guide_attempts = 1.
#     topic_score = 1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{study_guide_score} > {study_guide_attempts} : study_guide_score should be less than or equal to study_guide_attempts"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_topic_score_lt_attempts():
#     study_guide_score = 1.
#     study_guide_attempts = 1.
#     topic_score = 2.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{topic_score} > {topic_attempts} : topic_score should be less than or equal to topic_attempts"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_study_guide_attempts_lt_topic_attempts():
#     study_guide_score = 1.
#     study_guide_attempts = 3.
#     topic_score = 1.
#     topic_attempts = 1.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{study_guide_attempts} > {topic_attempts} : study_guide_attempts should be less than or equal to topic_attempts"
#
#
# @pytest.mark.validation_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_study_guide_score_lt_topic_score():
#     study_guide_score = 2.
#     study_guide_attempts = 3.
#     topic_score = 1.
#     topic_attempts = 3.
#     try:
#         algorithm.calculate_weighted_score_and_attempts(
#             study_guide_score, study_guide_attempts,
#             topic_score, topic_attempts)
#         assert False
#     except Exception as error:
#         assert error.__class__.__name__ == 'ValueError'
#         assert str(error) == f"{study_guide_score} > {topic_score} : study_guide_score should be less than or equal to topic_score"


# ------------------------------------------------------------
# Validation tests on algorithm.calculate_confidence_interval
# ------------------------------------------------------------

@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_score_is_float():
    weighted_score = '2'
    weighted_attempts = 3.
    try:
        algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"weighted_score should be a float, a {weighted_score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_attempts_is_float():
    weighted_score = 2.
    weighted_attempts = '3'
    try:
        algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"weighted_attempts should be a float, a {weighted_attempts.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_score_is_nonnegative():
    weighted_score = -2.
    weighted_attempts = 3.
    try:
        algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{weighted_score} < 0 : weighted_score should be non-negative"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_attempts_is_nonnegative():
    weighted_score = 2.
    weighted_attempts = -3.
    try:
        algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{weighted_attempts} < 0 : weighted_attempts should be non-negative"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_score_lt_attempts():
    weighted_score = 5.
    weighted_attempts = 3.
    try:
        algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{weighted_score} > {weighted_attempts} : weighted_score should be less than or equal to weighted_attempts"


# ---------------------------------------------------------------------------
# Validation tests on algorithm._convert_confidence_interval_into_probability
# ---------------------------------------------------------------------------

@pytest.mark.validation_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_receives_list():
    confidence_intervals_list = {1., 1., 3.}
    try:
        algorithm._convert_confidence_interval_into_probability(
            confidence_intervals_list)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"confidence_intervals_list should be a list, a {confidence_intervals_list.__class__.__name__} was provided"


@pytest.mark.validation_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_contains_floats():
    confidence_intervals_list = [1., 1, 3.]
    try:
        algorithm._convert_confidence_interval_into_probability(
            confidence_intervals_list)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"unexpected type encountered in confidence_intervals_list : expected float, got int"


@pytest.mark.validation_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_nonegative():
    confidence_intervals_list = [1., -1., 3.]
    try:
        algorithm._convert_confidence_interval_into_probability(
            confidence_intervals_list)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"-1.0 < 0 : all confidence intervals should be non-negative"


# ---------------------------------------------------------------------------
# Validation tests on algorithm._convert_confidence_interval_into_probability
# ---------------------------------------------------------------------------

@pytest.mark.validation_place_mastery_in_band
def test_place_mastery_in_band_receives_float():
    mastery_score = '4'
    try:
        algorithm._place_mastery_in_band(mastery_score)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided"


@pytest.mark.validation_place_mastery_in_band
def test_place_mastery_in_band_mastery_in_0_to_1():
    mastery_score = 4
    try:
        algorithm._place_mastery_in_band(mastery_score)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"unexpected value encountered: mastery_score should be in the interval [0, 1]"


# ---------------------------------------------------------------------------
# Validation tests on algorithm._convert_confidence_interval_into_probability
# ---------------------------------------------------------------------------

@pytest.mark.validation_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_score_is_float():
    score = 1
    attempts = 2.
    try:
        algorithm.calculate_beta_distribution_mean(score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"score should be a float, a {score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_attempts_is_float():
    score = 1.
    attempts = 2
    try:
        algorithm.calculate_beta_distribution_mean(score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"attempts should be a float, a {score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_score_is_nonegative():
    score = -1.
    attempts = 2.
    try:
        algorithm.calculate_beta_distribution_mean(score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{score} < 0 : score should be non-negative"


@pytest.mark.validation_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_attempts_is_nonegative():
    score = 1.
    attempts = -2.
    try:
        algorithm.calculate_beta_distribution_mean(score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{attempts} < 0 : attempts should be non-negative"


@pytest.mark.validation_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_score_lt_attempts():
    score = 2.
    attempts = 1.
    try:
        algorithm.calculate_beta_distribution_mean(score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{score} > {attempts} : score should be less than or equal to attempts"


# --------------------------------------------------------
# Validation tests on algorithm._calculate_band_confidence
# --------------------------------------------------------

@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_mastery_is_float():
    mastery_score, score, attempts = '0.7', 1., 1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_score_is_float():
    mastery_score, score, attempts = 0.7, 1, 1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"score should be a float, a {score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_attempts_is_float():
    mastery_score, score, attempts = 0.7, 1., 1
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"attempts should be a float, a {attempts.__class__.__name__} was provided"


@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_mastery_score_in_0_to_1():
    mastery_score, score, attempts = -0.7, 1., 1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"unexpected value encountered : mastery_score should be in the interval [0, 1]"

    mastery_score, score, attempts = 7., 1., 1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"unexpected value encountered : mastery_score should be in the interval [0, 1]"


@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_score_is_non_negative():
    mastery_score, score, attempts = 0.7, -1., 1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{score} < 0 : score should be non-negative"


@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_attempts_is_non_negative():
    mastery_score, score, attempts = 0.7, 1., -1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{attempts} < 0 : attempts should be non-negative"


@pytest.mark.validation_calculate_band_confidence
def test_calculate_band_confidence_score_lt_attempts():
    mastery_score, score, attempts = 0.7, 2., 1.
    try:
        algorithm._calculate_band_confidence(mastery_score, score, attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{score} > {attempts} : score should be less than or equal to attempts"


# ---------------------------------------------------------------
# Validation tests on algorithm._calculate_confident_mastery_band
# ---------------------------------------------------------------

@pytest.mark.validation_calculate_confident_mastery_band
def test_calculate_calculate_confident_mastery_band_mastery_is_float():
    mastery_score, confidence = '0.7', 2.
    try:
        algorithm._calculate_confident_mastery_band(mastery_score, confidence)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confident_mastery_band
def test_calculate_calculate_confident_mastery_band_confidence_is_float():
    mastery_score, confidence = 0.7, '2.'
    try:
        algorithm._calculate_confident_mastery_band(mastery_score, confidence)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"confidence should be a float, a {confidence.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confident_mastery_band
def test_calculate_calculate_confident_mastery_band_mastery_in_0_to_1():
    mastery_score, confidence = 1.7, 0.5
    try:
        algorithm._calculate_confident_mastery_band(mastery_score, confidence)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"unexpected value encountered - mastery_score should be in the interval [0, 1]"


@pytest.mark.validation_calculate_confident_mastery_band
def test_calculate_calculate_confident_mastery_band_confidence_in_0_to_1():
    mastery_score, confidence = 0.7, 2.
    try:
        algorithm._calculate_confident_mastery_band(mastery_score, confidence)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"unexpected value encountered - confidence should be in the interval [0, 1]"


# -------------------------------------------------------------
# Validation tests on algorithm.calculate_study_guide_weighting
# -------------------------------------------------------------

@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_score_is_float():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1, 1., 2., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"study_guide_score should be a float, a {study_guide_score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_attempts_is_float():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1, 2., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"study_guide_attempts should be a float, a {study_guide_attempts.__class__.__name__} was provided"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_topic_score_is_float():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1., 2, 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"topic_score should be a float, a {topic_score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_topic_attempts_is_float():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1., 2., 2
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"topic_attempts should be a float, a {topic_attempts.__class__.__name__} was provided"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_score_is_nonnegative():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = -1., 1., 2., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_score} < 0 : study_guide_score should be non-negative"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_attempts_is_nonnegative():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., -1., 2., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_attempts} < 0 : study_guide_attempts should be non-negative"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_topic_score_is_nonnegative():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1., -2., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_score} < 0 : topic_score should be non-negative"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_topic_attempts_is_nonnegative():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1., 2., -2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_attempts} < 0 : topic_attempts should be non-negative"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_score_lt_attempts():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 10., 1., 2., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_score} > {study_guide_attempts} : study_guide_score should be less than or equal to study_guide_attempts"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_topic_score_lt_attempts():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 1., 1., 20., 2.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_score} > {topic_attempts} : topic_score should be less than or equal to topic_attempts"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_score_lt_topic_score():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 3., 3., 2., 4.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_score} > {topic_score} : study_guide_score should be less than or equal to topic_score"


@pytest.mark.validation_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_study_guide_attempts_lt_topic_attempts():
    study_guide_score, study_guide_attempts, topic_score, topic_attempts = 2., 5., 2., 4.
    try:
        algorithm.calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_attempts} > {topic_attempts} : study_guide_attempts should be less than or equal to topic_attempts"


# -------------------------------------------------------------------
# Validation tests on algorithm.calculate_weighted_score_and_attempts
# -------------------------------------------------------------------

@pytest.mark.validation_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_study_guide_id_list_is_list():
    study_guide_id_list = {}
    weighted_score_and_attempts = {'z': {}}
    try:
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"study_guide_id_list should be a list, a {study_guide_id_list.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_study_guide_id_list_is_list_of_strings():
    study_guide_id_list = [1]
    weighted_score_and_attempts = {'z': {}}
    try:
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"unexpected type encountered in study_guide_id_list_list : expected str but got int"


@pytest.mark.validation_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_weighted_s_and_a_is_dict():
    study_guide_id_list = ['z']
    weighted_score_and_attempts = ['z']
    try:
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"weighted_score_and_attempts should be a dict, a {weighted_score_and_attempts.__class__.__name__} was provided"

@pytest.mark.validation_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_study_guide_ids_non_empty():
    study_guide_id_list = ['']
    weighted_score_and_attempts = {'z': {}}
    try:
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(
            error) == f"unexpected value encountered in study_guide_id_list: study_guide_ids should be non-empty"


@pytest.mark.validation_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_study_guide_ids_not_z_id():
    study_guide_id_list = ['b']
    weighted_score_and_attempts = {'z': {}}
    try:
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(
            error) == f"unexpected value encountered in study_guide_id_list: study_guide_ids should be the z id of a study guide, received b"


@pytest.mark.validation_calculate_confidence_intervals_list
def test_calculate_confidence_intervals_list_keys_are_in_study_guide_id_list():
    study_guide_id_list = ['z1']
    weighted_score_and_attempts = {'z': {}}
    try:
        algorithm.calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(
            error) == f"unexpected key encountered in weighted_score_and_attempts: key z does not appear in study_guide_id_list"
