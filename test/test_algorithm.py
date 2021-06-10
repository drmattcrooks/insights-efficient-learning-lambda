from test.fixtures.questions import VALID_QUESTION, VALID_SINGLE_QUESTION_ID_LIST
import pytest
import algorithm
from algorithm import _calculate_thompson_sampling


def test_choose_initial_question(mocker):
    question_ids_mock = mocker.patch(
        'storage_client.StorageClient.select_all_question_ids')
    question_ids_mock.return_value = VALID_SINGLE_QUESTION_ID_LIST

    question_mock = mocker.patch(
        'storage_client.StorageClient.select_question_by_id')
    question_mock.return_value = VALID_QUESTION

    topic_id_for_study_guide_id = {'zc7k2nb': 'z2s8v9q'}
    study_guide_id_list = ['zc7k2nb']

    actual_question = algorithm.choose_initial_question(
        topic_id_for_study_guide_id, study_guide_id_list)

    assert actual_question == VALID_QUESTION


def test_choose_next_question_multiple_recursions(mocker):
    question_ids_mock = mocker.patch(
        'storage_client.StorageClient.select_and_filter_question_ids')
    question_ids_mock.side_effect = [[], VALID_SINGLE_QUESTION_ID_LIST]

    question_mock = mocker.patch(
        'storage_client.StorageClient.select_question_by_id')
    question_mock.return_value = VALID_QUESTION

    topic_id_for_study_guide_id = {'zc7k2nb': 'z2s8v9q', 'zs8y4qt': 'zc7k2nb'}
    study_guide_id_list = ['zc7k2nb', 'zs8y4qt']
    confidence_intervals_list = [0.70, 0.10]
    question_id_list = ['abc-abc-abc-abc']

    actual_question = algorithm.choose_next_question(
        topic_id_for_study_guide_id, study_guide_id_list, confidence_intervals_list, question_id_list)

    assert len(study_guide_id_list) == 2
    assert actual_question == VALID_QUESTION


def test_get_mastery_band_and_confidence_confident_band1():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        1 / 6, 0., 4.)

    assert actual_mastery_band == 1
    assert actual_confidence == pytest.approx(0.87, abs=0.005)


def test_get_mastery_band_and_confidence_uncertain_band2():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        2 / 3, 1., 1.)

    assert actual_mastery_band == 2
    assert actual_confidence == pytest.approx(0.56, abs=0.005)


def test_get_mastery_band_and_confidence_confident_band2():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        0.5, 4., 8.)

    assert actual_mastery_band == 2
    assert actual_confidence == pytest.approx(0.69, abs=0.005)


def test_get_mastery_band_and_confidence_confident_band3():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        5 / 6, 4., 4.)

    assert actual_mastery_band == 3
    assert actual_confidence == pytest.approx(0.87, abs=0.005)


def test_thompson_sampling_integral_returns_correct_values():
    actual_weighting = _calculate_thompson_sampling(0, 2, 1, 3)
    assert actual_weighting == pytest.approx(0.286, abs=0.001)

    actual_weighting = _calculate_thompson_sampling(2, 2, 1, 3)
    assert actual_weighting == pytest.approx(0.886, abs=0.001)
