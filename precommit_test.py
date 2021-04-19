from SearchEngineForJSON.search import Search
import unittest

data = {
    "name1": "Nakamura",
    "name2": {
        "name2-1": "Aoi",
        "name2-2": [
            "listA",
            "listB",
            {
                True: "listInDict1",
                2: "listInDict2",
                2.2: {
                    "listC-3-1": "hello",
                    "listC-3-2": "world",
                    "listC-3-3": [
                        "Sunday",
                        "Monday",
                        "Tuesday"
                    ],
                    "listC-3-4": 5,
                    "listC-3-5": True,
                    "listC-3-6": False,
                    "listC-3-7": None
                },
                "->": "listInDict3",
                "->->": "listInDict4",
                "->->->": "listInDict5",
                "->hello": "listInDict6",
                "hello->": "listInDict7",
                "->hello->": "listInDict8",
                "he->llo": [
                    "in",
                    "out"
                ],
                "2.2": "string",
                "2.3": 2,
                "2.4": 2.2,
                "2.5": "listInDict6"
            },
            "listD",
            "listE"
        ],
        "name2-3": "python",
        "name2-4": [
            "Docker",
            "kubernetes",
            "Docker-compose"
        ]
    },
    "name3": "json",
    "name4": "search"
}

typeSearchAnswer = [
    ['name1', 'Nakamura'],
    ['name3', 'json'],
    ['name4', 'search'],
    ['name2->name2-1', 'Aoi'],
    ['name2->name2-3', 'python'],
    ['name2->name2-2->list(0)', 'listA'],
    ['name2->name2-2->list(1)', 'listB'],
    ['name2->name2-2->list(3)', 'listD'],
    ['name2->name2-2->list(4)', 'listE'],
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.2', 'string'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-1', 'hello'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-2', 'world'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(0)', 'Sunday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(1)', 'Monday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(2)', 'Tuesday'],
    ['name2->name2-2->list(2)->he(>)llo->list(0)', 'in'],
    ['name2->name2-2->list(2)->he(>)llo->list(1)', 'out'],
    ['name2->name2-4->list(0)', 'Docker'],
    ['name2->name2-4->list(1)', 'kubernetes'],
    ['name2->name2-4->list(2)', 'Docker-compose'],
]

getAllAnswear = [
    ['name1', 'Nakamura'],
    ['name3', 'json'],
    ['name4', 'search'],
    ['name2->name2-1', 'Aoi'],
    ['name2->name2-3', 'python'],
    ['name2->name2-2->list(0)', 'listA'],
    ['name2->name2-2->list(1)', 'listB'],
    ['name2->name2-2->list(3)', 'listD'],
    ['name2->name2-2->list(4)', 'listE'],
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.2', 'string'],
    ['name2->name2-2->list(2)->2.3', 2],
    ['name2->name2-2->list(2)->2.4', 2.2],
    ['name2->name2-2->list(2)->2.5', 'listInDict6'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-1', 'hello'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-2', 'world'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-4', 5],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-5', True],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-6', False],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-7', None],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(0)', 'Sunday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(1)', 'Monday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(2)', 'Tuesday'],
    ['name2->name2-2->list(2)->he(>)llo->list(0)', 'in'],
    ['name2->name2-2->list(2)->he(>)llo->list(1)', 'out'],
    ['name2->name2-4->list(0)', 'Docker'],
    ['name2->name2-4->list(1)', 'kubernetes'],
    ['name2->name2-4->list(2)', 'Docker-compose']
]


valueSearchAnswear = [
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]

subValueSearchAnswear = [
    ['name2->name2-2->list(0)', 'listA'],
    ['name2->name2-2->list(1)', 'listB'],
    ['name2->name2-2->list(3)', 'listD'],
    ['name2->name2-2->list(4)', 'listE'],
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]

startValueSearchAnswear = [
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]


endValueSearchAnswear = [
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]

keySearchAnswear = [
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]

subKeySearchAnswear = [
    ['name2->name2-2->list(2)->float(2.2)->listC-3-1', 'hello'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-2', 'world'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3', ['Sunday', 'Monday', 'Tuesday']],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-4', 5],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-5', True],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-6', False],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-7', None]
]

class Test(unittest.TestCase):
    def test_typeSearch(self):
        self.assertEqual(typeSearchAnswer, Search.typeSearch(data, str))

    def test_getAll(self):
        self.assertEqual(getAllAnswear, Search.getAll(data))


    def test_valueSearch(self):
        self.assertEqual(valueSearchAnswear, Search.valueSearch(data, "listInDict6"))
        self.assertEqual([], Search.valueSearch(data, "listInDict6gbar@urba@"))

    def test_subValueSearch(self):
        self.assertEqual(subValueSearchAnswear, Search.subValueSearch(data, "list"))
        self.assertEqual([], Search.subValueSearch(data, "lisgpewbu@piub4er"))

    def test_startValueSearch(self):
        self.assertEqual(startValueSearchAnswear, Search.startValueSearch(data, "listIn"))
        self.assertEqual([], Search.startValueSearch(data, "gh@reaugaburgbe@ru"))


    def test_endValueSearch(self):
        self.assertEqual(endValueSearchAnswear, Search.endValueSearch(data, "Dict6"))
        self.assertEqual([], Search.endValueSearch(data, "ga@oubvaourb@iu"))

    def test_keySearch(self):
        self.assertEqual(keySearchAnswear, Search.keySearch(data, "2.5"))
        self.assertEqual([], Search.keySearch(data, "anva@urav@u@ub"))

    def test_subKeySearch(self):
        self.assertEqual(subKeySearchAnswear, Search.subKeySearch(data, "stC-3-"))
        self.assertEqual([], Search.subKeySearch(data, "gns@otgnbs@eoutbjnr@[irn"))
        

if __name__ == "__main__":
    unittest.main()










