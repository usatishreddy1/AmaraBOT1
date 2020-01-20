#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Meet Robo: your friend

#import necessary libraries
import io
import os
import random
import string # to process standard python strings
import warnings

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

from pathlib import Path

# uncomment the following only the first time
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only

test = Path('./hsbc-advance-platinum-cc-mitc.txt').read_text()
print(test)

data_dir = "D:/CodeGrind/Data/Formatted_Data/"

#Reading in the corpus
total_str = ''
for file in os.listdir(data_dir):
    filename = data_dir + "hsbc-advance-platinum-cc-mitc.txt"
    print(filename)
    data = open(filename, 'rt', encoding="utf-8", errors="ignore")
    text = data.read()
    data.close()
    total_str=total_str + "\n" + text


raw = text.lower()

#print(raw)

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response=''
    
    sent_filt_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_filt_tokens)
    #feature_names = tfidf.get_feature_names()
    #print(tfidf)
    vals = cosine_similarity(tfidf[-1], tfidf)
    #print(vals)
    #for a in vals[0]:
        #print(sent_tokens[int(a)])
    idx=vals.argsort()[0][-2]
    #print(idx)
    
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    
    
    
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_filt_tokens[idx]
        return robo_response






flag=True
print(" My name is BOT. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    tokens_user= LemNormalize(user_response)
    #print(tokens_user)
        
    #print(token_data)
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("BOT: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("BOT: "+greeting(user_response))
            else:
                
                sent_filt_tokens=[]  
                new_list=[]
                sent_list=[]
                Counter=0
                #print(raw)
                for line in raw.splitlines():
                    #print(line)
                    #print(line.split(":"))
                    key_words=line.split(":")[0]
                    sent=line.split(":")[1]
                    words=key_words.split(" ")
                    x=set(words) & set(tokens_user)
                    new_list.append(x)
                    sent_list.append(sent)
                
                m = max(new_list)
                #print(new_list)
                #print(m)
                match_index=[i for i, j in enumerate(new_list) if j == m]
                
                
                for x in match_index:
                    sent_filt_tokens.append(sent_list[x])                
                
                #print(sent_filt_tokens)
                
                print("BOT: ",end="")
                print(response(user_response))
                sent_filt_tokens.remove(user_response)
                
    else:
        flag=False
        print("BOT: Bye! take care..") 
