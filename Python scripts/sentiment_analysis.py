import csv

dict_positive = {}
dict_negative = {}
list_tweets = []
with open('data.txt') as tweetfile:
  tweets = [x.strip() for x in tweetfile.readlines()]
  for line in tweets:
    line = line.replace('\n','')
    line = line.replace('\r','')
    line = line.replace('Tweet:','')
    list_tweets.append(line)

list_positive_words=[]
with open('positive-words.txt') as posfile:
  list_positive_words = [positive.strip() for positive in posfile.readlines()]

list_negative_words=[]
with open('negative-words.txt',encoding="ISO-8859-1") as f:
  list_negative_words = [negative.strip() for  negative in f.readlines()]


dict_ab = []
with open('SentimentAnalysis.csv','w') as sentiment_analysis:
  sentiment = csv.writer(sentiment_analysis, lineterminator = '\n')
  sentiment.writerow(['Tweet','Message','Match','Polarity'])
  for i in range(len(list_tweets)):
      bag_words = {}
      tweet_words = list_tweets[i].split(" ")
      for word in range(len(tweet_words)):
        key = tweet_words[word]
        key = key.lower()
        if key in bag_words.keys():
          bag_words[key] = bag_words[key] + 1
        else:
          bag_words[key] = 1
      
      dict_ab.append(bag_words)
      positive_word_count=0
      negative_word_count=0
      neutral=0
      polarity="neutral"
      match_list=""
      positive_match_list =""
      negative_match_list = ""
      for key_list in bag_words.keys():
        if key_list in list_positive_words:
          positive_word_count=positive_word_count+1
          if key_list in dict_positive.keys():
            dict_positive[key_list] = dict_positive[key_list] + 1
          else:
            dict_positive[key_list] = 1
          positive_match_list=positive_match_list + key_list +","
        elif key_list in list_negative_words:
          negative_word_count=negative_word_count+1
          if key_list in dict_negative.keys():
            dict_negative[key_list] = dict_negative[key_list] + 1
          else:
            dict_negative[key_list] = 1
          negative_match_list=negative_match_list + key_list +","
        else:
          neutral=neutral+1   
      if(positive_word_count>negative_word_count):
        polarity="positive"  
        match_list=positive_match_list
      elif(positive_word_count<negative_word_count):
        polarity="negative"  
        match_list=negative_match_list
      else:
         match_list="NONE," 
      sentiment.writerow([i,list_tweets[i],match_list[:-1],polarity]);   

with open('Positive&Negative_tweets.csv','w') as fil:
  positive_file = csv.writer(fil, lineterminator = '\n')
  positive_file.writerow(['words','Count'])
  for key_list in dict_positive.keys():
    positive_file.writerow([key_list, dict_positive[key_list]])

  for key_list in dict_negative.keys():
    positive_file.writerow([key_list, dict_negative[key_list]])



