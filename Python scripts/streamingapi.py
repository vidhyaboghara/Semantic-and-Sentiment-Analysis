import csv
Canada_count = 0
University_count = 0
Halifax_count = 0
CE_count = 0
DU_count = 0

for i in range(482):
	filename ="newsapi_data"+str(i)+".txt"
	with open(filename, 'r', encoding = 'utf-8') as news_data:
		news = news_data.readlines()
		news_words = news.split(" ")
		
			
