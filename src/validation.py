import numpy as np
import algorithm


def is_float_like(value):
    return type(value) in [int, float]


def _accumulate_score_and_attempts(undecorated_function):
    def validate_accumulate_score_and_attempts(
            study_guide_id_list, topic_id_list, questions):

        if not isinstance(study_guide_id_list, list):
            raise TypeError(f"study_guide_id_list should be a list, a {study_guide_id_list.__class__.__name__} was provided")
        if not isinstance(topic_id_list, list):
            raise TypeError(f"topic_id_list should be a list, a {topic_id_list.__class__.__name__} was provided")
        if not isinstance(questions, list):
            raise TypeError(f"questions should be a list, a {questions.__class__.__name__} was provided")
        # if any([~isinstance(study_guide_id, str) | (study_guide_id == '')
        #         for study_guide_id in study_guide_id_list]):
        #     raise ValueError(
        #         f"unexpected value encountered in study_guide_id_list: study_guide_ids should be a non-empty string")

        return undecorated_function(
            study_guide_id_list, topic_id_list, questions)

    return validate_accumulate_score_and_attempts


def calculate_weighted_value(undecorated_function):
    def validate_calculate_weighted_value(
            weighting, study_guide_value, topic_value):

        if not isinstance(weighting, float):
            raise TypeError(f"weighting should be a float, a {weighting.__class__.__name__} was provided")
        if not isinstance(study_guide_value, float):
            raise TypeError(f"study_guide_value should be a float, a {study_guide_value.__class__.__name__} was provided")
        if not isinstance(topic_value, float):
            raise TypeError(f"topic_value should be a float, a {topic_value.__class__.__name__} was provided")

        if (weighting < 0) | (weighting > 1):
            raise ValueError(f"unexpected value encountered - weighted_score should be in the interval [0, 1]")
        if study_guide_value < 0:
            raise ValueError(f"{study_guide_value} < 0 : study_guide_value should be non-negative")
        if topic_value < 0:
            raise ValueError(f"{topic_value} < 0 : topic_value should be non-negative")

        # if study_guide_value > topic_value:
        #     raise ValueError(f"{study_guide_value} > {topic_value} : study_guide_value should be less than or equal to topic_value")

        return undecorated_function(
            weighting, study_guide_value, topic_value)

    return validate_calculate_weighted_value


def calculate_confidence_interval(undecorated_function):
    def validate_calculate_confidence_interval(
            weighted_score, weighted_attempts):

        if not isinstance(weighted_score, float):
            raise TypeError(f"weighted_score should be a float, a {weighted_score.__class__.__name__} was provided")
        if not isinstance(weighted_attempts, float):
            raise TypeError(f"weighted_attempts should be a float, a {weighted_attempts.__class__.__name__} was provided")

        if weighted_score < 0:
            raise ValueError(f"{weighted_score} < 0 : weighted_score should be non-negative")
        if weighted_attempts < 0:
            raise ValueError(f"{weighted_attempts} < 0 : weighted_attempts should be non-negative")

        # if weighted_score > weighted_attempts:
        #     raise ValueError(f"{weighted_score} > {weighted_attempts} : weighted_score should be less than or equal to weighted_attempts")

        return undecorated_function(
            weighted_score, weighted_attempts)

    return validate_calculate_confidence_interval


def _convert_confidence_interval_into_probability(undecorated_function):
    def validate_confidence_interval_into_probability(
            confidence_intervals_list):

        if not isinstance(confidence_intervals_list, list):
            raise TypeError(f"confidence_intervals_list should be a list, a {confidence_intervals_list.__class__.__name__} was provided")

        for confidence_interval in confidence_intervals_list:
            if not isinstance(confidence_interval, float):
                raise TypeError(f"unexpected type encountered in confidence_intervals_list : expected float, got {confidence_interval.__class__.__name__}")
            if confidence_interval < 0:
                raise ValueError(f"{confidence_interval} < 0 : all confidence intervals should be non-negative")

        return undecorated_function(
            confidence_intervals_list
        )

    return validate_confidence_interval_into_probability


def _place_mastery_in_band(undecorated_function):
    def validate_place_mastery_in_band(mastery_score):

        if not is_float_like(mastery_score):
            raise TypeError(f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided")
        if (mastery_score < 0) | (mastery_score > 1):
            raise TypeError(f"unexpected value encountered: mastery_score should be in the interval [0, 1]")

        return undecorated_function(mastery_score)

    return validate_place_mastery_in_band


def calculate_beta_distribution_mean(undecorated_function):
    def validate_calculate_beta_distribution_mean(alpha, beta_):

        if not isinstance(alpha, float):
            raise TypeError(f"alpha should be a float, a {alpha.__class__.__name__} was provided")
        if not isinstance(beta_, float):
            raise TypeError(f"beta should be a float, a {beta_.__class__.__name__} was provided")
        if alpha < 0:
            raise ValueError(f"{alpha} < 0 : score should be non-negative")
        if beta_ < 0:
            raise ValueError(f"{beta_} < 0 : attempts should be non-negative")

        return undecorated_function(alpha, beta_)

    return validate_calculate_beta_distribution_mean


def _calculate_band_confidence(undecorated_function):
    def validate_calculate_band_confidence(mastery_score, alpha, beta):

        if not isinstance(mastery_score, float):
            raise TypeError(f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided")
        if not isinstance(alpha, float):
            raise TypeError(f"alpha should be a float, a {alpha.__class__.__name__} was provided")
        if not isinstance(beta, float):
            raise TypeError(f"beta should be a float, a {beta.__class__.__name__} was provided")

        if (mastery_score < 0) | (mastery_score > 1):
            raise ValueError(f"unexpected value encountered : mastery_score should be in the interval [0, 1]")
        if alpha < 0:
            raise ValueError(f"{alpha} < 0 : alpha should be non-negative")
        if beta < 0:
            raise ValueError(f"{beta} < 0 : beta should be non-negative")

        return undecorated_function(mastery_score, alpha, beta)

    return validate_calculate_band_confidence


def _calculate_confident_mastery_band(undecorated_function):
    def validate_calculate_confident_mastery_band(mastery_score, confidence):

        if not is_float_like(mastery_score):
            raise TypeError(f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided")
        if not is_float_like(confidence):
            raise TypeError(f"confidence should be a float, a {confidence.__class__.__name__} was provided")
        if (mastery_score < 0) | (mastery_score > 1):
            raise ValueError(f"unexpected value encountered - mastery_score should be in the interval [0, 1]")
        if (confidence < 0) | (confidence > 1):
            raise ValueError(f"unexpected value encountered - confidence should be in the interval [0, 1]")

        return undecorated_function(mastery_score, confidence)

    return validate_calculate_confident_mastery_band


def _calculate_study_guide_weighting(undecorated_function):
    def validate_calculate_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts):

        if not isinstance(study_guide_score, float):
            raise TypeError(f"study_guide_score should be a float, a {study_guide_score.__class__.__name__} was provided")
        if not isinstance(study_guide_attempts, float):
            raise TypeError(f"study_guide_attempts should be a float, a {study_guide_attempts.__class__.__name__} was provided")
        if not isinstance(topic_score, float):
            raise TypeError(f"topic_score should be a float, a {topic_score.__class__.__name__} was provided")
        if not isinstance(topic_attempts, float):
            raise TypeError(f"topic_attempts should be a float, a {topic_attempts.__class__.__name__} was provided")

        if study_guide_score < 0:
            raise ValueError(f"{study_guide_score} < 0 : study_guide_score should be non-negative")
        if study_guide_attempts < 0:
            raise ValueError(f"{study_guide_attempts} < 0 : study_guide_attempts should be non-negative")
        if topic_score < 0:
            raise ValueError(f"{topic_score} < 0 : topic_score should be non-negative")
        if topic_attempts < 0:
            raise ValueError(f"{topic_attempts} < 0 : topic_attempts should be non-negative")

        # if study_guide_score > study_guide_attempts:
        #     raise ValueError(f"{study_guide_score} > {study_guide_attempts} : study_guide_score should be less than or equal to study_guide_attempts")
        # if topic_score > topic_attempts:
        #     raise ValueError(f"{topic_score} > {topic_attempts} : topic_score should be less than or equal to topic_attempts")
        # if study_guide_score > topic_score:
        #     raise ValueError(f"{study_guide_score} > {topic_score} : study_guide_score should be less than or equal to topic_score")
        # if study_guide_attempts > topic_attempts:
        #     raise ValueError(f"{study_guide_attempts} > {topic_attempts} : study_guide_attempts should be less than or equal to topic_attempts")

        return undecorated_function(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)

    return validate_calculate_study_guide_weighting


def calculate_confidence_intervals_list(undecorated_function):
    def validate_calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts):

        if type(study_guide_id_list) != list:
            raise TypeError(f"study_guide_id_list should be a list, a {study_guide_id_list.__class__.__name__} was provided")
        for study_guide_id in study_guide_id_list:
            if type(study_guide_id) != str:
                raise TypeError(f"unexpected type encountered in study_guide_id_list_list : expected str but got {study_guide_id.__class__.__name__}")
        if type(weighted_score_and_attempts) != dict:
            raise TypeError(f"weighted_score_and_attempts should be a dict, a {weighted_score_and_attempts.__class__.__name__} was provided")

        if any([study_guide_id == '' for study_guide_id in study_guide_id_list]):
            raise ValueError(f"unexpected value encountered in study_guide_id_list: study_guide_ids should be non-empty")
        for study_guide_id in study_guide_id_list:
            if study_guide_id[0] != 'z':
                raise ValueError(f"unexpected value encountered in study_guide_id_list: study_guide_ids should be the z id of a study guide, received {study_guide_id}")
        for key in weighted_score_and_attempts:
            if key not in study_guide_id_list:
                raise ValueError(f"unexpected key encountered in weighted_score_and_attempts: key {key} does not appear in study_guide_id_list")

        return undecorated_function(
            study_guide_id_list, weighted_score_and_attempts)

    return validate_calculate_confidence_intervals_list
