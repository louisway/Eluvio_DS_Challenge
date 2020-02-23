import csv
import sys
import nltk
import string
import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
punctuation = string.punctuation
map = " "* len(punctuation)
translator = str.maketrans(punctuation,map)
#translator = str.maketrans(" ", " ", string.punctuation)
def tok_stop_lemm(title):
    title = title.lower()
    title = title.strip()
    title = title.replace('-','')
    title = title.replace('.','')
    title = title.replace('‘','')
    title = title.replace('’','')
    title = title.translate(translator)
    title = re.sub(r'\d+','',title)
    title = title.translate(translator)
    title = word_tokenize(title) 
    #title = [lemmatizer.lemmatize(word) for word in title]
    title = [stemmer.stem(word) for word in title]
    title = [word for word in title if word not in stop_words]
    return title
     
raw = open("../Eluvio_DS_Challenge.csv","r")
csv_reader = csv.reader(raw, delimiter= ",")
draft_output = open("../train_draft.dat","w")
output = open("../train.dat","w")


#processing line by line 
line = -1
for row in csv_reader:
    if line%5000 == 0:
        print(str(line) +" lines has been processed")

    if line >= 0:
        postext = tok_stop_lemm(row[4])
        if len(postext) == 0:
            line -= 1
        else:
            draft_output.write(' '.join(postext))
            draft_output.write("\n") 
    line += 1
raw.close()
draft_output.close()
draft_output = open("../train_draft.dat","r")
output.write(str(line))
output.write("\n")

while True:
    line = draft_output.readline()
    if not line:
        break
    output.write(line)
   
draft_output.close()
output.close()
os.remove("../train_draft.dat")
