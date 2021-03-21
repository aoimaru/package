import json
from . import searchMain
import datetime

def main() -> None:
	try:
		searchMain.Search.test("hello")

		jsonOpen = open("./tests/testData.json", mode="r")
		jsonData = json.load(jsonOpen)
		jsonOpen.close()
		items = searchMain.Search.moldSearch(jsonData, str)
		for item in items:
			print(item)
	except:
		data = {    
		"contents": {
			"start": datetime.datetime(2021, 3, 2, 6, 10, 30, 245000), 
			"end": datetime.datetime(2099, 10, 10, 10, 10, 10, 1000)
			},
		"contents2": {
			"start": datetime.datetime(2021, 3, 2, 6, 10, 30, 245000), 
			"end": datetime.datetime(2099, 10, 10, 10, 10, 10, 1000),
			"contents3": {
					"start": datetime.datetime(2021, 3, 2, 6, 10, 30, 245000), 
					"end": datetime.datetime(2099, 10, 10, 10, 10, 10, 1000)
				},
			"contents4": {
					"contents5": {
						"start": datetime.datetime(2021, 3, 2, 6, 10, 30, 245000), 
						"end": datetime.datetime(2099, 10, 10, 10, 10, 10, 1000)
						}
				}
			
			}
		}

		items = searchMain.Search.moldSearch(data, datetime.datetime)
		for item in items:
			print(item)