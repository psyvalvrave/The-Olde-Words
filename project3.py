# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:04:23 2019

@author: zhech
"""
import urllib
from bs4 import BeautifulSoup
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize
from collections import Counter

   
url = "http://shakespeare.mit.edu/othello/full.html"
lem = WordNetLemmatizer()
words = set(words.words('en'))

with urllib.request.urlopen(url) as url_file:
    soup = BeautifulSoup(url_file,"lxml")
data = (soup.find_all(['blockquote','b','h3','H3']))#Extract all text with bp
raw_text = (i.text.lower() for i in data)
#tokenize, lemmatize
tok_text = (wordpunct_tokenize(w) for w in raw_text)
lem_text = (lem.lemmatize(w) for i in tok_text for w in i)#the tok_text is two dimensional
all_text = (w for w in lem_text if w not in words and w.isalpha())
number_text = Counter(all_text)#Use Counter to count
top25 = sorted(number_text, key=number_text.__getitem__, reverse=True)[:25]#general a list with top 25 words
print(top25)




