# CALCULATION OF BINARY FEATURES

# 1: IF A TERM APPEAR IN A SENTENCE) 0 : DOESN'T APPEAR

import nltk
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

#NO OF TERMS
unique_tokens = []

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
    for x in filtered_sentence:
        if x not in unique_tokens:
            unique_tokens.append(x)
print("\n Total unique tokens are: "+str(len(unique_tokens)) +"\n")
print(unique_tokens)

print("\n BINARY FEATURES \n")

for i in range(len(unique_tokens)):
    BinaryFeature=[]
    for j in range(sencount):
        if ((unique_tokens[i]) in s[j]):        
            x=1
            BinaryFeature.append(1)    
        else:
            BinaryFeature.append(0)
    print(BinaryFeature)    


