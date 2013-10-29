import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from math import sqrt
import gensim
from sklearn.svm import SVC
import os
import numpy
from nltk.corpus import stopwords

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications","A survey of user opinion of computer system response time", "The EPS user interface management syste ","System and human system engineering testing of EPS","Relation of user perceived response time to error measurement","The generation of random binary unordered trees","The intersection graph of paths in trees","Graph minors IV Widths of trees and well quasi ordering","Graph minors A survey"]

 # remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]

 # remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]for text in texts]
#print texts
dictionary = corpora.Dictionary(texts)
#dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference
#print dictionary

#print dictionary.token2id


corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('./deerwester.mm', corpus) # store to disk, for later use
#print corpus

print "Next"

###################### Corpus from a file

class MyCorpus(object):
	def __iter__(self):
		for line in open('mycorpus.txt'):
			# assume there's one document per line, tokens separated by whitespace
			yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
for vector in corpus_memory_friendly: # load one vector into memory at a time
	1
	#print vector
corpora.MmCorpus.serialize('./deerwester1.mm', corpus_memory_friendly) # store to disk, for later use
#print corpus





# Create dictionary without loading everything in memory
dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
 # remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
dictionary.save('./deerwester.dict') # store the dictionary, for future reference

#print dictionary
#print dictionary.token2id

##### At this stage, we have a corpus and a vector representation of the corpus. Decide what model/transformation to use now. 



dictionary = corpora.Dictionary.load('./deerwester.dict')
corpus = corpora.MmCorpus('./deerwester1.mm')
#print corpus

#####TFIDF
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	1
	#print "Doc",doc



############## This part computes Similarity based on TFIDF values-- WORKING

## NOTE: In the TfIdf representation, any documents which do not share any common features with vec at all get a similarity score of 0.0.
index = similarities.SparseMatrixSimilarity(corpus_tfidf, num_features=12)
for doc in corpus_tfidf:
	sims = index[doc]
	print "TFIDF Sim",sorted(enumerate(sims), key=lambda item: -item[1])

##############







####### LSI
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=5) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
lsi.print_topics(5)

############## This part computes Similarity based on LSI values-- WORKING
index = similarities.MatrixSimilarity(corpus_lsi)
#printing which documnet belongs in which topic
for doc in corpus_lsi:
	sims=index[doc]
	print "LSI Sim",sorted(enumerate(sims), key=lambda item: -item[1])

##############

####### LDA
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=5,passes=10) # initialize an LSI transformation
corpus_lda = lda[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
lda.print_topics(5)

############## This part computes Similarity based on LSI values-- WORKING
index = similarities.MatrixSimilarity(corpus_lda)
#printing which documnet belongs in which topic
for doc in corpus_lda:
	sims=index[doc]
	print "LDA Sim",sorted(enumerate(sims), key=lambda item: -item[1])

##############

##### Similarity
###################### Corpus from a file
index = similarities.MatrixSimilarity(lsi[corpus])
class MyCorpus(object):
	def __iter__(self):
		for line in open('mycorpus.txt'):
			# assume there's one document per line, tokens separated by whitespace
			yield dictionary.doc2bow(line.lower().split())




corpus_memory_friendly1 = MyCorpus() # doesn't load the corpus into memory!
index = similarities.MatrixSimilarity(lsi[corpus])
for vector in corpus_memory_friendly1: # load one vector into memory at a time
	vec_lsi = lsi[vector]
	sims = index[vec_lsi]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	#print sims 



