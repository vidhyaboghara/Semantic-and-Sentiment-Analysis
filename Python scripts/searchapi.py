import os
import tweepy as tw
import pandas as pd
import csv
import re

ACCESS_TOKEN = "1187470800376467456-5LYkhuELpEQSeRuRF0iFcJEmIyGFsp"
ACCESS_TOKEN_SECRET = "V8wUMMPPbjuDQSegknnscugLuPMtVZCnrZ7WSs3BE8mq4"
CONSUMER_KEY = "FrYXuABcw1B5aIdvIiaJWCaFv"
CONSUMER_KEY_SECRET = "LYLykuTyJ9GH0yZTITGj1uyu92hndsd1Uxzy5fdQFLCmDXOlDd"

auth = tw.OAuthHandler(CONSUMER_KEY ,CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth, wait_on_rate_limit=True)
date_since = "2018-11-16"

hashtag_list = 'Canada OR University OR Dalhousie University OR Halifax OR Canada Education'

tweets = tw.Cursor(api.search,
              q=hashtag_list,
              lang="en",
              since=date_since).items(3000)



with open('data.txt','w+',encoding = 'utf-8') as file:
	
	for i in tweets:
		j = i.text
		j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',j)
		j = j.strip()
		data = 'ID: '+ i.id_str+ ' Tweet: ' + j+ ' Time: '+ str(i.created_at) +' location : '+str(i.place)+ '\n'
		file.write(data)

