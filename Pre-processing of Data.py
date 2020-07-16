import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer

corpus_root = 'C:\MyData\PythonPractice\Mycorpus'
wordlists = PlaintextCorpusReader(corpus_root, 'resort.*\.txt')

print('\nFollowing file ids are there in this corpus: \n ')
print(wordlists.fileids())
print("\nNumber of sentences in the file are :")
print(len(wordlists.sents(fileids=['resort.txt'])))
print('\n Sentences are : \n') 
sentences=wordlists.sents(fileids='resort.txt')
print(sentences)
print('\n Words are : \n') 
print(wordlists.words('resort.txt'))
print('\n Sample (raw data) is: \n')
sample=wordlists.raw("resort.txt")
print(sample[0:100])

print('\n Tokenization \n')
word_tokens = word_tokenize(sample)
print('Number of tokens:'+ str(len(word_tokens))+'\n')
token_f=len(word_tokens)
print(word_tokens)

print('\n Removing PUNCTUATIONS \n')
word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
print('Number of tokens:'+ str(len(word_tokens))+'\n')
print(word_tokens)

print('\n Removing STOPWORDS Now \n')
stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in word_tokens if not w in stop_words]

#filtered_sentence = []
#
#for w in word_tokens:
#    if w not in stop_words:
#        filtered_sentence.append(w)
print('Number of tokens:'+ str(len(filtered_sentence))+'\n')
print(filtered_sentence)

print('\n Unique tokens\n ')
unique_tokens = []
for x in filtered_sentence:
    if x not in unique_tokens:
        unique_tokens.append(x)
print('Number of tokens:'+ str(len(unique_tokens))+'\n')
token_l=len(unique_tokens)
print(unique_tokens)

print('\n STEMMING Now \n')
ps = PorterStemmer()
for w in unique_tokens:
    print((ps.stem(w)).encode("utf-8"))

print('\n LEMMATIZING Now \n')
lemmatizer = WordNetLemmatizer()
for w in unique_tokens:
    print((lemmatizer.lemmatize(w)).encode("utf-8"))
    
#FREQUENCIES

wordfreq = []
for w in filtered_sentence:
    wordfreq.append(filtered_sentence.count(w))
print("\n Frequencies\n" + str(wordfreq) + "\n")
print("\n Pair wise --(Words,Frequences) \n" )
print(list(zip(filtered_sentence, wordfreq)))
print('\n'*2)

#DIMENSION REDUCTION

print("Initialing Number of tokens are :"+ str(token_f))
print("After Text Processing Number of tokens are :"+ str(token_l))
dimension_reduction_per=((token_f-token_l)/(token_f))*100
print("Dimension Reduction % :"+str(dimension_reduction_per))