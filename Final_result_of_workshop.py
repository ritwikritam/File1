# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 09:48:18 2019

@author: Ritwik Sinha
"""


import requests

weburl = requests.get('https://www.moneycontrol.com/').text
print(weburl)

from bs4 import BeautifulSoup

soup = BeautifulSoup(weburl,'html.parser')
sub_links = soup.find('div', {"class" : "clearfix tabs_news_container"})
print(sub_links)
para = sub_links.find('p')
print(para.get_text())

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(para.get_text())
print(tokenized_word)
tag = nltk.pos_tag(tokenized_word)
print(tag)

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
pos_word_list=[]
neg_word_list=[]
neu_word_list=[]
final_text = para.get_text().split(" ")
for word in final_text:
    if(sid.polarity_scores(word)['compound'])>=0.2:
        pos_word_list.append(word)
    elif(sid.polarity_scores(word)['compound'])<=-0.2:
        neg_word_list.append(word)
    else:
        neu_word_list.append(word)
    print(neu_word_list)