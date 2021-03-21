

""" SearchEngine for JSON
	
	Todo:
		* Practice
"""

class Search(object):
	""" SearchEngine for json

		Json形式のデータを検索するためのモジュール(小技)

		Attributes:
			None
	"""
	@classmethod
	def moldSearch(cls, documents, mold, name=None):
		""" SearchEngine for json by mold
			
			json形式のデータを型を基にvalueで検索
			指定の型のデータを取得可能

			Args:
				documents(dict(json)): 探索したいjson形式のデータ
				mold(型オブジェクト): 検索したい値の型を指定
				name(string): 呼び出し時不要, 指定必要なし

			returns:
				list: 値までの絶対パス(仮称)と値
		"""
		ans = [[key, value] for key, value in documents.items() if type(value) is mold]
		if name:
			answears = []
			for item in ans:
				answears.append([name+"."+item[0], item[1]])
		else:
			answears = ans

		req_docs = [[key, value] for key, value in documents.items() if isinstance(value, dict)]

		if name:
			req_answears = []
			for item in req_docs:
				req_answears.append([name+"."+item[0], item[1]])
		else:
			req_answears = req_docs

		if not req_answears:
			return answears
		else:
			for req_answear in req_answears:
				answears.extend(cls.moldSearch(documents=req_answear[1], mold=mold, name=req_answear[0]))
			return answears

	@staticmethod
	def test(string: str):
		print(string)





