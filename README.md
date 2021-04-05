
# SearchEngine for JSON (自作パッケージ公開練習)
* json形式のデータから指定の型を持つkeyとvalueを再起的に取得します


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
```


