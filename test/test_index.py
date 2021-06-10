from test.fixtures.events import INVALID_EVENT, \
    VALID_EVENT_NO_QUESTIONS, \
    VALID_EVENT_NO_RESULTS, VALID_EVENT_WITH_RESULTS,\
    FINAL_EVENT_FOR_REPEATABLE_RESULTS
from test.fixtures.questions import NEXT_QUESTION, \
    VALID_QUESTION_RESPONSE_NO_RESULTS, VALID_RESPONSE_WITH_RESULTS,\
    REPEATABLE_RESULTS


import pytest
from index import handler

CONTEXT = None


def test_invalid_event_raises_exception():
    with pytest.raises(Exception) as error:
        handler(INVALID_EVENT, CONTEXT)

    assert str(error.value) == '[BAD REQUEST]: Invalid event'


def test_valid_event_initial_question(mocker):

    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = {}

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = {}

    random_question_mock = mocker.patch(
        'algorithm.choose_initial_question')
    random_question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_NO_QUESTIONS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS


def test_valid_event_with_results_returns_next_question(mocker):

    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = ['zc7k2nb', 'z84jtv4', 'zs8y4qt', 'zt8t3k7', 'zxr7ng8', 'z3tgw6f', 'z8fkmsg']

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = {'zc7k2nb': 'z2s8v9q', 'z84jtv4': 'z2s8v9q', 'zs8y4qt': 'z2s8v9q', 'zt8t3k7': 'z9236yc', 'zxr7ng8': 'z9236yc', 'z3tgw6f': 'z9236yc', 'z8fkmsg': 'z9236yc'}

    mastery_mock = mocker.patch('algorithm.calculate_beta_distribution_mean')
    mastery_mock.return_value = 0.75

    confidence_mock = mocker.patch('algorithm.calculate_confidence_interval')
    confidence_mock.return_value = 0.5

    band_mock = mocker.patch('algorithm.calculate_mastery_band_and_confidence')
    band_mock.return_value = 3, 0.65

    question_mock = mocker.patch('algorithm.choose_next_question')
    question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_WITH_RESULTS, CONTEXT)

    assert actual_question == VALID_RESPONSE_WITH_RESULTS


def test_valid_event_no_results_returns_next_question(mocker):
    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = ['zc7k2nb', 'z84jtv4', 'zs8y4qt', 'zt8t3k7', 'zxr7ng8', 'z3tgw6f', 'z8fkmsg']

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = {'zc7k2nb': 'z2s8v9q', 'z84jtv4': 'z2s8v9q', 'zs8y4qt': 'z2s8v9q', 'zt8t3k7': 'z9236yc', 'zxr7ng8': 'z9236yc', 'z3tgw6f': 'z9236yc', 'z8fkmsg': 'z9236yc'}

    mastery_mock = mocker.patch('algorithm.calculate_beta_distribution_mean')
    mastery_mock.return_value = 0.75

    confidence_mock = mocker.patch('algorithm.calculate_confidence_interval')
    confidence_mock.return_value = 0.5

    band_mock = mocker.patch('algorithm.calculate_mastery_band_and_confidence')
    band_mock.return_value = 3, 0.65

    question_mock = mocker.patch('algorithm.choose_next_question')
    question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_NO_RESULTS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS


def test_results_are_repeatable(mocker):

    topic_from_study_guide = {"z9vrjty": "zcj78mn", "zxtscj6": "zcj78mn", "zcpxfcw": "zcj78mn",
                              "zsfpb82": "zcj78mn", "zpk2srd": "zcj78mn", "zxmmsrd": "zcj78mn",
                              "zy98msg": "zcj78mn", "zgmpgdm": "zcj78mn", "zscrw6f": "zcj78mn",
                              "z2ty97h": "zcj78mn", "zgcrxfr": "zxsyh39", "zwbyjty": "zxsyh39",
                              "zqsxrwx": "zxsyh39", "z8npk2p": "zxsyh39", "zg9rxfr": "zxsyh39",
                              "z3fsdxs": "zxsyh39", "z9nr6yc": "z398rwx", "zsf9pbk": "z398rwx",
                              "z2rmrwx": "z398rwx", "z2jndxs": "z398rwx", "ztr7b82": "z398rwx",
                              "z3h4h39": "z398rwx"}
    study_guide_id_list = ["z9vrjty", "zxtscj6", "zcpxfcw", "zsfpb82", "zpk2srd", "zxmmsrd",
                           "zy98msg", "zgmpgdm", "zscrw6f", "z2ty97h", "zgcrxfr", "zwbyjty",
                           "zqsxrwx", "z8npk2p", "zg9rxfr", "z3fsdxs", "z9nr6yc", "zsf9pbk",
                           "z2rmrwx", "z2jndxs", "ztr7b82", "z3h4h39"]

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = topic_from_study_guide

    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = study_guide_id_list

    question_mock = mocker.patch('algorithm.choose_next_question')
    question_mock.return_value = NEXT_QUESTION

    actual_results = handler(FINAL_EVENT_FOR_REPEATABLE_RESULTS, CONTEXT)['body']['results']

    assert actual_results == REPEATABLE_RESULTS
