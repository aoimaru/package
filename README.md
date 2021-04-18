
# SearchEngine for JSON (自作パッケージ公開)
* json形式のデータから条件に従ったkeyとvalueを再起的に取得します

[![Downloads](https://pepy.tech/badge/searchengineforjson)](https://pepy.tech/project/searchengineforjson)
[![Downloads](https://pepy.tech/badge/searchengineforjson/month)](https://pepy.tech/project/searchengineforjson)
[![Downloads](https://pepy.tech/badge/searchengineforjson/week)](https://pepy.tech/project/searchengineforjson)


<img alt="Run pytest" src="https://github.com/aoimaru/packagingTutorial/workflows/Upload Python Package/badge.svg"></a>
# install
```bash
pip install SearchEngineForJSON
```
## ディレクトリ構造
```
|--packagingTutorial
|  |--SearchEngineForJSON
|  |  |--__init__.py
|  |  |--search.py
|  |--setup.py
```

# Usage
```
import SearchEngineForJSON

SearchEngineForJSON.Search.typeSearch(探索したいデータ, 探索したい型) -> [[key, value], []]
SearchEngineForJSON.Search.getAll(探索したいデータ) -> [[key, value], []]
SearchEngineForJSON.Search.valueSearch(探索したいデータ, 探索したい値) -> [[key, value], []]
SearchEngineForJSON.Search.typeSearch(探索したいデータ, 探索したい型) -> [[key, value], []]
SearchEngineForJSON.Search.typeSearch(探索したいデータ, 探索したい型) -> [[key, value], []]

```

# Example
```
import SearchEngineForJSON

data = {
    "name1": "Nakamura",
    "name2": {
        "name2-1": "Aoi",
        "name2-2": [
            "listA",
            "listB",
            {
                "listC-1": "listInDict1",
                "listC-2": "listInDict2",
                "listC-3": {
                    "listC-3-1": "hello",
                    "listC-3-2": "world",
                    "listC-3-3": [
                        "Sunday",
                        "Monday",
                        "Tuesday"
                    ],
                    "listC-3-4": 5,
                    "listC-3-5": True
                }
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
    }
}

items = SearchEngineForJSON.Search.typeSearch(data, str)

for item in items:
    print(item)
```
```
['name1', 'Nakamura']
['name2.name2-1', 'Aoi']
['name2.name2-3', 'python']
['name2.name2-2.0', 'listA']
['name2.name2-2.1', 'listB']
['name2.name2-2.3', 'listD']
['name2.name2-2.4', 'listE']
['name2.name2-2.2.listC-1', 'listInDict1']
['name2.name2-2.2.listC-2', 'listInDict2']
['name2.name2-2.2.listC-3.listC-3-1', 'hello']
['name2.name2-2.2.listC-3.listC-3-2', 'world']
['name2.name2-2.2.listC-3.listC-3-3.0', 'Sunday']
['name2.name2-2.2.listC-3.listC-3-3.1', 'Monday']
['name2.name2-2.2.listC-3.listC-3-3.2', 'Tuesday']
['name2.name2-4.0', 'Docker']
['name2.name2-4.1', 'kubernetes']
['name2.name2-4.2', 'Docker-compose']
```


