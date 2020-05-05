import csv, math
Canada_doc = 0
University_doc = 0
Halifax_doc = 0
CE_doc = 0
DU_doc = 0
document_array_canada = []

total_doc =484

for i in range(484):
	Canada_count = 0
	University_count = 0
	Halifax_count = 0
	CE_count = 0
	DU_count = 0
	filename ="newsapi_data"+str(i)+".txt"
	with open(filename, 'r', encoding = 'utf-8') as news_data:
		news = news_data.readline()
		news_words = news.split(" ")
		news_words = [x.lower() for x in news_words]
		for j in range(len(news_words)):
			if(news_words[j] == 'canada'):
				Canada_count = Canada_count+1
			if(news_words[j] == 'university'):
				University_count = University_count+1
			if(news_words[j] == 'halifax'):
				Halifax_count = Halifax_count+1
			if(j < len(news_words) and news_words[j] == 'canada' and news_words[j+1] == 'education'):
				CE_count = CE_count+1
			if(j < len(news_words) and news_words[j] == 'dalhousie' and news_words[j+1] == 'university'):
				DU_count = DU_count+1
		if(Canada_count>0):
			Canada_doc = Canada_doc+1
			canada_details = str(len(news_words)) +","+str(i) +","+str(Canada_count)
			document_array_canada.append(canada_details)
		if(University_count>0):
			University_doc = University_doc+1
		if(Halifax_count>0):
			Halifax_doc = Halifax_doc+1
		if(CE_count>0):
			CE_doc = CE_doc+1
		if(DU_count>0):
			DU_doc = DU_doc+1

canada_occurences = total_doc/Canada_doc
halifax_occurences = total_doc/Halifax_doc
university_occurences = total_doc/University_doc
#ce_occurences = total_doc/CE_doc
DU_occurences = total_doc/DU_doc

with open('SemanticAnalysis.csv','w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['Total documents',total_doc])
	writer.writerow(['Search Query','Document Containing Term(df)','Total documents(N)/number of  documents  term  appeared (df)','Log10(N/df)'])
	ndf_canada = str(total_doc)+"/"+str(Canada_doc)
	ndf_university = str(total_doc) + "/" + str(University_doc)
	ndf_halifax = str(total_doc) +"/" + str(Halifax_doc)
	ndf_du = str(total_doc) + "/" + str(DU_doc)
	ndf_ce = str(total_doc) + "/" +str(CE_doc)
	writer.writerow(['Canada',Canada_doc, ndf_canada, str(round(math.log10(canada_occurences),2))])
	writer.writerow(['University',University_doc, ndf_university, str(round(math.log10(university_occurences),2))])
	writer.writerow(['Halifax',Halifax_doc, ndf_halifax, str(round(math.log10(halifax_occurences),2))])
	writer.writerow(['Canada Education',CE_doc, ndf_ce , 'log10(infinity)'])
	writer.writerow(['Dalhousie University',DU_doc, ndf_du , str(round(math.log10(DU_occurences),2))])
maximum_frequency = 0
article_no = ''

with open('SemanticAnalysis2.csv','w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['Term', 'Canada'])
	writer.writerow(['Canada appeared in '+  str(Canada_doc) + ' documents', 'Total words(m)', 'Frequency(f)'])
	for i in range(Canada_doc):
		article_details = document_array_canada[i].split(",")
		writer.writerow(["Article #"+ article_details[1], article_details[0], article_details[2]])

		relative_frequency= int(article_details[2])/int(article_details[0])
		print(round(relative_frequency,2))

		if(relative_frequency>maximum_frequency):
			maximum_frequency=relative_frequency
			article_no = article_details[0]

artilce_filename = "newsapi_data" +str(article_no) + ".txt"
print(artilce_filename)

with open(artilce_filename,'r', encoding="utf-8") as articledata:
	articlewithmaxfreq = (articledata.readline())
	print(articlewithmaxfreq)