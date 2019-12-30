# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:26:11 2019

@author: Vatsav
"""
from nltk import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import re
import nltk
import json
import os

DataDir = "D:/CodeGrind/Data/Source_Data/"
ConvDir = "D:/CodeGrind/Data/Formatted_Data/"

# load data
#filename = 'D:\CodeGrind\Data\CodeGrindPdfToText\credit-card-guide.txt'
#filename = 'D:\CodeGrind\Data\cricket.txt'

#print(type(text))

# split into sentences


#for s in sentences :
#print(sentences[9:15])
#    print("")

#lemmer = WordNetLemmatizer()
#def LemTokens(tokens):
#    return [lemmer.lemmatize(token) for token in tokens]
#remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
#def LemNormalize(text):
#    return LemTokens(nltk.word_tokenize(cleansed_text.lower().translate(remove_punct_dict)))

#TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
#print(TfidfVec)

##Creating a list of stop words and adding custom stopwords
stop_words = set(stopwords.words("english"))



for file in os.listdir(DataDir):
    filename = DataDir + file
    data = open(filename, 'rt', encoding="ascii", errors="ignore")
    text = data.read()
    data.close()

    
    cleansed_text = text
    sentences = sent_tokenize(cleansed_text)
    
    sent_dict = {}
    
    writefile = ConvDir + file
    with open(writefile, 'w+') as file:
    
        for sent in sentences :
            print(sent + "1")
            
            corpus = []
            #for i in range(0, 3847):
            #Remove punctuations
            text = re.sub('[^a-zA-Z]', ' ', sent)
            
            text = re.sub(':',"", text)
            
            sent = re.sub(':','', sent)
            
            sent = re.sub('\.','', sent)
            
            sent = sent.strip().replace("\n"," ")
            
            #filt_sent = filter(lambda x: x in string.printable, sent)
            
            #print(filt_sent)
            
            #Convert to lowercase
            text = text.lower().strip().replace("\n"," ")
            
            #remove tags
            text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
            
            # remove special characters and digits
            text=re.sub("(\\d|\\W)+"," ",text)
            
            ##Convert to list from string
            text = text.split()
            
            ##Stemming
            ps=PorterStemmer()
            #Lemmatisation
            lem = WordNetLemmatizer()
            text = [lem.lemmatize(word) for word in text if not word in  
                    stop_words] 
            text = ",".join(text)
            #print(text)
            corpus.append(text)
            sent_dict[tuple(corpus)] = sent
            file.write("%s:%s\n" %(corpus,sent))

         
    
