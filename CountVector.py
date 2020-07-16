#   COUNT VECTOR MATRIX
#CALCULATION OF FREQUENCIES OF EACH TERM

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

#   NUMBER OF TIMES A TERM APPEAR IN EACH SENTENCE
wordfreq=[]
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
    #print("\n Pair wise --(Words,Frequences) for Sentence"+ str(i+1)+ "\n" )
    #print(list(zip(filtered_sentence, wordfreq)))
    fs, wf =  zip(*(list(zip(filtered_sentence, wordfreq))))
    print("\n Count Vector"+str(i+1)+"\n")
    print(wf)
    
# COUNT MATRIX
wordfreq=[]

print("\n COUNT VECTORS \n")
for i in range(sencount):
    word_tokens = word_tokenize(s[i])
    word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    for w in filtered_sentence:
        wordfreq.append(filtered_sentence.count(w))
    fs, wf =  zip(*(list(zip(filtered_sentence, wordfreq))))
    print(wf)