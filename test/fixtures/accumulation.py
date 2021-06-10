STUDY_GUIDE_ID_LIST = [f"zg{i}" for i in range(1, 7)]
TOPIC_ID_LIST = ['zt1', 'zt2']
TOPIC_ID_FOR_STUDY_GUIDE_ID = {'zg1': 'zt1', 'zg2': 'zt1', 'zg3': 'zt1',
                               'zg4': 'zt2', 'zg5': 'zt2', 'zg6': 'zt2'}
QUESTIONS_TO_TEST_ACCUMULATION = [
    {
        "topicId": "zt1",
        "studyGuideId": "zg1",
        "id": "1",
        "isCorrect": True,
        "timeTaken": 12345
    },
    {
        "topicId": "zt1",
        "studyGuideId": "zg2",
        "id": "2",
        "isCorrect": False,
        "timeTaken": 12345
    },
    {
        "topicId": "zt1",
        "studyGuideId": "zg3",
        "id": "3",
        "isCorrect": True,
        "timeTaken": 12345
    },
    {
        "topicId": "zt2",
        "studyGuideId": "zg4",
        "id": "4",
        "isCorrect": False,
        "timeTaken": 12345
    },
    {
        "topicId": "zt2",
        "studyGuideId": "zg6",
        "id": "6",
        "isCorrect": True,
        "timeTaken": 12345
    }
]
EXPECTED_ACCUMULATED_STUDY_GUIDE_ALPHA_AND_BETA = {
    'zg1': {'alpha': 2., 'beta': 1.},
    'zg2': {'alpha': 1., 'beta': 2.},
    'zg3': {'alpha': 2., 'beta': 1.},
    'zg4': {'alpha': 1., 'beta': 2.},
    'zg5': {'alpha': 1., 'beta': 1.},
    'zg6': {'alpha': 2., 'beta': 1.}
}
EXPECTED_ACCUMULATED_TOPIC_ALPHA_AND_BETA = {
    'zt1': {'alpha': 3., 'beta': 2.},
    'zt2': {'alpha': 2., 'beta': 2.}
}