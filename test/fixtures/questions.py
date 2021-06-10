VALID_QUESTION = {
    "id": "1",
    "text": "What will happen if a spray of perfume is released into one corner of a room?",
    "studyGuideId": "zc7k2nb",
    "topicId": "z2s8v9q",
    "options": [
        {
            "id": "1",
            "text": "Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis",
            "isCorrect": False
        },
        {
            "id": "2",
            "text": "Particles of the perfume will diffuse until they are spread evenly through the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room",
            "isCorrect": True
        },
        {
            "id": "3",
            "text": "The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room",
            "isCorrect": False
        }
    ]
}

NEXT_QUESTION = {
    "id": "1",
    "text": "What will happen if a spray of perfume is released into one corner of a room?",
    "studyGuideId": "zc7k2nb",
    "topicId": "z2s8v9q",
    "options": [
        {
            "id": "1",
            "text": "Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis",
            "isCorrect": False
        },
        {
            "id": "2",
            "text": "Particles of the perfume will diffuse until they are spread evenly through the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room",
            "isCorrect": True
        },
        {
            "id": "3",
            "text": "The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room",
            "isCorrect": False
        }
    ]
}

VALID_QUESTION_RESPONSE_NO_RESULTS = {
    'statusCode': 200,
    'body': {
        'nextQuestion': {
            "id": "1",
            "text": "What will happen if a spray of perfume is released into one corner of a room?",
            "studyGuideId": "zc7k2nb",
            "topicId": "z2s8v9q",
            "options": [
                {
                    "id": "1",
                    "text": "Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed",
                    "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis",
                    "isCorrect": False
                },
                {
                    "id": "2",
                    "text": "Particles of the perfume will diffuse until they are spread evenly through the room ",
                    "response": "Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room",
                    "isCorrect": True
                },
                {
                    "id": "3",
                    "text": "The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ",
                    "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room",
                    "isCorrect": False
                }
            ]
        },
        'results': []
    }
}

VALID_RESPONSE_WITH_RESULTS = {
    'statusCode': 200,
    'body': {
        'nextQuestion': {},
        'results': [
            {
                'studyGuideId': 'zc7k2nb',
                'topicId': 'z2s8v9q',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'z84jtv4',
                'topicId': 'z2s8v9q',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'zs8y4qt',
                'topicId': 'z2s8v9q',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'zt8t3k7',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'zxr7ng8',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'z3tgw6f',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'z8fkmsg',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            }
        ]
    }
}

VALID_SINGLE_QUESTION_ID_LIST = [{
    "id": "1"
}]

REPEATABLE_RESULTS = [
    {
      "studyGuideId": "z9vrjty",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 43.243243243601505,
      "confidenceScore": 53.670226553980136
    },
    {
      "studyGuideId": "zxtscj6",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 39.09465020636277,
      "confidenceScore": 49.24457647039768
    },
    {
      "studyGuideId": "zcpxfcw",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 66.93548387507578,
      "confidenceScore": 56.09365941850655
    },
    {
      "studyGuideId": "zsfpb82",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 43.243243243601505,
      "confidenceScore": 53.670226553980136
    },
    {
      "studyGuideId": "zpk2srd",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 52.32558139681658,
      "confidenceScore": 58.065867942003216
    },
    {
      "studyGuideId": "zxmmsrd",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 39.09465020636277,
      "confidenceScore": 49.24457647039768
    },
    {
      "studyGuideId": "zy98msg",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 39.09465020636277,
      "confidenceScore": 49.24457647039768
    },
    {
      "studyGuideId": "zgmpgdm",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 43.243243243601505,
      "confidenceScore": 53.670226553980136
    },
    {
      "studyGuideId": "zscrw6f",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 32.89473684415434,
      "confidenceScore": 56.21892790706553
    },
    {
      "studyGuideId": "z2ty97h",
      "topicId": "zcj78mn",
      "band": 2,
      "masteryScore": 43.243243243601505,
      "confidenceScore": 53.670226553980136
    },
    {
      "studyGuideId": "zgcrxfr",
      "topicId": "zxsyh39",
      "band": 2,
      "masteryScore": 38.70967715397743,
      "confidenceScore": 42.91140524345732
    },
    {
      "studyGuideId": "zwbyjty",
      "topicId": "zxsyh39",
      "band": 2,
      "masteryScore": 57.40740688263869,
      "confidenceScore": 43.324247389029914
    },
    {
      "studyGuideId": "zqsxrwx",
      "topicId": "zxsyh39",
      "band": 2,
      "masteryScore": 44.82758608559743,
      "confidenceScore": 45.98973602199733
    },
    {
      "studyGuideId": "z8npk2p",
      "topicId": "zxsyh39",
      "band": 2,
      "masteryScore": 38.70967715397743,
      "confidenceScore": 42.91140524345732
    },
    {
      "studyGuideId": "zg9rxfr",
      "topicId": "zxsyh39",
      "band": 2,
      "masteryScore": 44.82758608559743,
      "confidenceScore": 45.98973602199733
    },
    {
      "studyGuideId": "z3fsdxs",
      "topicId": "zxsyh39",
      "band": 2,
      "masteryScore": 46.11872134629721,
      "confidenceScore": 51.74424069388891
    },
    {
      "studyGuideId": "z9nr6yc",
      "topicId": "z398rwx",
      "band": 3,
      "masteryScore": 69.85294107719447,
      "confidenceScore": 61.99031206180028
    },
    {
      "studyGuideId": "zsf9pbk",
      "topicId": "z398rwx",
      "band": 3,
      "masteryScore": 69.85294107719447,
      "confidenceScore": 61.99031206180028
    },
    {
      "studyGuideId": "z2rmrwx",
      "topicId": "z398rwx",
      "band": 2,
      "masteryScore": 62.499999734342296,
      "confidenceScore": 37.53504465704821
    },
    {
      "studyGuideId": "z2jndxs",
      "topicId": "z398rwx",
      "band": 3,
      "masteryScore": 69.85294107719447,
      "confidenceScore": 61.99031206180028
    },
    {
      "studyGuideId": "ztr7b82",
      "topicId": "z398rwx",
      "band": 2,
      "masteryScore": 62.499999734342296,
      "confidenceScore": 37.53504465704821
    },
    {
      "studyGuideId": "z3h4h39",
      "topicId": "z398rwx",
      "band": 2,
      "masteryScore": 57.251908610875404,
      "confidenceScore": 47.393644491353804
    }
  ]
