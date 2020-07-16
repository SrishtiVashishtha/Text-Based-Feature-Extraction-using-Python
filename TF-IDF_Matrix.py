# CALCULATION OF TF VALUES

# TF_IDF= TF*IDF

import nltk
import math
from decimal import *
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

corpus_root = 'C:\MyData\PythonPractice\Mycorpus'
wordlists = PlaintextCorpusReader(corpus_root, 'resort.*\.txt')

print('\nFollowing file ids are there in this corpus: \n ')
print(wordlists.fileids())
print("\nNumber of sentences in the file are :")
sencount=len(wordlists.sents(fileids=['resort.txt']))
print(sencount)
print('\n Sentences are : \n') 
sentences=wordlists.sents(fileids='resort.txt')
print(sentences)
sample=wordlists.raw("resort.txt")
s=sample.split('.')

#   NUMBER OF TIMES A TERM APPEAR IN EACH SENTENCE

#   NUMBER OF TERMS IN  EACH SENTENCE

wordfreq = []
term_freq=[]
terms_count_doc=[]

for i in range(sencount):
    print("\n Sentence "+ str(i+1))
    print(s[i])
#print('\n Tokenization \n')
    word_tokens = word_tokenize(s[i])
#print('\n Removing PUNCTUATIONS')
    word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
#print('\n Removing STOPWORDS Now')
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    for w in filtered_sentence:
        wordfreq.append(filtered_sentence.count(w))
    print("\n Pair wise --(Words,Frequences) for Sentence"+ str(i+1)+ "\n" )
    print(list(zip(filtered_sentence, wordfreq)))
    fs, wf =  zip(*(list(zip(filtered_sentence, wordfreq))))
    print("\n Number of times a term appear in sentence "+str(i+1)+"\n")
    print(wf)
    term_freq.append(wf)
    unique_tokens = []
    for x in filtered_sentence:
        if x not in unique_tokens:
            unique_tokens.append(x)
    print('\n Number of tokens:'+ str(len(unique_tokens)))
    print(unique_tokens)
    terms_count_doc.append(len(unique_tokens))
print("\n Numbers of terms in each sentence is :")
print(terms_count_doc)
print("\n Numbers of times a term appear in sentences 1-10 \n")
print(term_freq)
    
# TF for each term

for i in range(sencount):
    TF=[]
    for j in range(len(term_freq[i])):
        x=((term_freq[i])[j])/(terms_count_doc[i])
        TF.append(x)
    print("\n TF values for  Sentence : "+ str(i+1))
    print(TF)
    
# CALCULATION OF IDF VALUES 

# IDF= log(N/n) N : NUMBER OF DOCUMENTS n : NUMBER OF DOCUMENTS A TERM HAS APPEARED IN

#N : no of sentences
N=sencount
unique_tokens = []
for i in range(sencount):
#print('\n Tokenization \n')
    word_tokens = word_tokenize(s[i])
#print('\n Removing PUNCTUATIONS')
    word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
#print('\n Removing STOPWORDS Now')
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)   
    for x in filtered_sentence:
        if x not in unique_tokens:
            unique_tokens.append(x)
print("\n Total unique tokens are: "+str(len(unique_tokens)) +"\n")
print(unique_tokens)

# n : NUMBER OF DOCUMENTS A TERM HAS APPEARED IN

count=[]
for i in range(len(unique_tokens)):
    x=0
    for j in range(N):
        if unique_tokens[i] in s[j]:
            x=x+1
            count.append(x) 
    
    print("\n Number of sentences  " + str(unique_tokens[i])+" has appeared in :"+ str(x))
count=count[5:]
print("\n Combined Number of Sentences a term has appeared in :  \n")
print(count)

#   IDF Values
IDF=[]
for i in range(len(unique_tokens)):
    x=math.log10(N/(count[i]))
    print("\n IDF value of " +str(unique_tokens[i])+ " is : " + str(x))
    IDF.append(x)

#   COMBINED TF MATRIX
TFM=[]
for i in range(sencount):
    for j in range(len(term_freq[i])):
        x=((term_freq[i])[j])/(terms_count_doc[i])
        TFM.append(x)
print("\n COMBINED REPRESENTATION of TF Values : \n ")
print(TFM)
    
#   COMBINED IDF MATRIX
IDFM=[]
for i in range(len(unique_tokens)):
    x=math.log10(N/(count[i]))
    IDFM.append(x)
print("\n COMBINED REPRESENTATION of IDF Values : \n ")
print(IDFM)

#   COMBINED TF-IDF MATRIX
#TF_IDF = TF* IDF
TF_IDF=[]

for i in range(len(unique_tokens)):
            TF_IDF.append(TFM[i]*IDF[i])
            
print("\n COMBINED REPRESENTATION of TF-IDF Values : \n ")
print(TF_IDF)