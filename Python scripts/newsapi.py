import pprint
import requests
import re

secret = 'ee3b516efc134a1e84719ecf0771892f'

url = 'https://newsapi.org/v2/everything?'

keywords = ["Canada","University","Dalhousie University","Halifax","Canada Education"]

k = 0
for keyword in keywords:

	parameters = {
		'q' : keyword,
		'pageSize' : 100,
		'apiKey' : secret
	}

	response = requests.get(url,params = parameters)
	response_json = response.json()

	
	for i in response_json['articles']:
		filename = "newsapi_data" + str(k) + ".txt"
		with open(filename,'w+',encoding = 'utf-8') as file:
			datanews = "title : " + str(i['title']) +" Content : " + str(i['content']) + " Description : " + str(i['description']) 
			datanews = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',datanews)
			file.write(datanews)
		k=k+1


