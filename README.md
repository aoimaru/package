
# SearchEngine for JSON (自作パッケージ公開)
* json形式のデータから指定の型を持つkeyとvalueを再起的に取得します

[![Downloads](https://pepy.tech/badge/searchengineforjson)](https://pepy.tech/project/searchengineforjson)
[![Downloads](https://pepy.tech/badge/searchengineforjson/month)](https://pepy.tech/project/searchengineforjson)
[![Downloads](https://pepy.tech/badge/searchengineforjson/week)](https://pepy.tech/project/searchengineforjson)

# install
```bash
pip install SearchEngineForJSON
```
## ディレクトリ構造
```
|--packagingTutorial
|  |--SearchEngineForJSON
|  |  |--__init__.py
|  |  |--searchMain.py
|  |--setup.py
```

# Usage
```
from SearchEngineForJSON.searchMain import Search

Search.moldSearch(探索したいデータ, 探索したい型) -> [[key, value], []]
```

# Example
```
from SearchEngineForJSON.searchMain import Search

data = {
  "name1": "hello",
  "name2": {
    "name2-1": 2,
    "name2-2": "world"
  }
}

items = Search.moldSearch(data, str)

for item in items:
  print(item)
```
```
["name1", "hello"]
["name2.name2-2", "world"]


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
                    "listC-3-2": "world"
                }
            }
        ]
    }
}

items = Search.moldSearch(data, str)

for item in items:
    print(item)

['name1', 'Nakamura']
['name2.name2-1', 'Aoi']
['name2.name2-2.0', 'listA']
['name2.name2-2.1', 'listB']
['name2.name2-2.2.listC-1', 'listInDict1']
['name2.name2-2.2.listC-2', 'listInDict2']
['name2.name2-2.2.listC-3.listC-3-1', 'hello']
['name2.name2-2.2.listC-3.listC-3-2', 'world']


```


