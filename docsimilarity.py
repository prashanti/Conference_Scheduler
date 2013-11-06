import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from math import sqrt
import gensim
from collections import Counter
import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy
from gensim import corpora, models, similarities


################### Creating a set of stopwords
stoplist=set()
for line in open('stopwords.txt'):
	line=line.strip()
	stoplist.add(line.lower())
###################
inputfile='Evolution-Corpus.txt'
#inputfile='TestCorpus.txt'
min=1132
max=1243  ### Add 1 to the parallel session number 
notopics=200
################### Create dictionary without loading everything in memory

dictionary = corpora.Dictionary(line.lower().split() for line in open(inputfile))
 # remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
dictionary.save('./storeddictionary.dict') # store the dictionary, for future reference
#print dictionary


###################

f = open('myfile.txt','w')
###################### Corpus from a file

class MyCorpus(object):
	def __iter__(self):
		freq=Counter()
		for line in open(inputfile):
			words=line.lower().split()
			tmp=Counter()
			for word in words:
				if (tmp[word]!=1):
					freq[word] +=1
				tmp[word]=1


		for line in open(inputfile):
			# assume there's one document per line, tokens separated by whitespace
			newline=list()
			newline=line.lower().split()
			for word in newline:
				word=word.strip()
				#f.write(word)
				#f.write("\n")
				if word in stoplist:
					newline = filter(lambda a: a != word, newline)
					#f.write(word)
					#f.write("\n")
				if ((freq[word]==1) & (word not in stoplist)):
					newline = filter(lambda a: a != word, newline)
					#f.write("Removing freq 1",word)
					1
			#dictionary.doc2bow needs a list as input
			#print "Newline",newline
			yield dictionary.doc2bow(newline)

corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
for vector in corpus_memory_friendly: # load one vector into memory at a time
	1
	#print "VECTOR",vector
corpora.MmCorpus.serialize('./storedcorpus.mm', corpus_memory_friendly) # store to disk, for later use

###################


################### Load the stored dictionary and corpus

# At this stage, we have a corpus and a vector representation of the corpus. Decide what model/transformation to use now. 

dictionary = corpora.Dictionary.load('./storeddictionary.dict')
corpus = corpora.MmCorpus('./storedcorpus.mm')
#print corpus
print dictionary.token2id
###################


################### TFIDF
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
corpus_tfidf = tfidf[corpus]
index = similarities.MatrixSimilarity(corpus_tfidf)
docno=1
clustersum=0
cluster =range(min, max)
for doc in corpus_tfidf:
	sims = index[doc]
	#print "TFIDF Sim",sorted(enumerate(sims), key=lambda item: -item[1])
	#print "Unsorted", list(enumerate(sims))
	testlist= list(enumerate(sims))
	if docno in cluster:
		for item in cluster:
			clustersum=clustersum+testlist[item-1][1]
		cluster=filter(lambda a: a != docno, cluster)
	docno=docno+1
print "TFIDF Cluster Sum",clustersum
print "\n\n"
###################



################### LSI
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=notopics) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
#print lsi.print_topics(notopics)

# Similarity Computation
index = similarities.MatrixSimilarity(corpus_lsi)
#printing which document belongs in which topic
docno=1
clustersum=0
cluster =range(min, max)
for doc in corpus_lsi:
	sims = index[doc]
	#print "TFIDF Sim",sorted(enumerate(sims), key=lambda item: -item[1])
	#print "Unsorted", list(enumerate(sims))
	testlist= list(enumerate(sims))
	if docno in cluster:
		for item in cluster:
			clustersum=clustersum+testlist[item-1][1]
		cluster=filter(lambda a: a != docno, cluster)
	docno=docno+1
print "LSI Cluster Sum",clustersum
print "\n\n"
###################


################### LDA
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=notopics,passes=10) # initialize an LSI transformation
corpus_lda = lda[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
#print lda.print_topics(notopics)
x=0
while x<200:
	print lda.print_topic(x, topn=2)
	x=x+1
# Similarity Computation
index = similarities.MatrixSimilarity(corpus_lda)
docno=1
clustersum=0
cluster =range(min, max)
for doc in corpus_lda:
	sims = index[doc]
	#print "TFIDF Sim",sorted(enumerate(sims), key=lambda item: -item[1])
	#print "Unsorted", list(enumerate(sims))
	testlist= list(enumerate(sims))
	if docno in cluster:
		for item in cluster:
			clustersum=clustersum+testlist[item-1][1]
		cluster=filter(lambda a: a != docno, cluster)
	docno=docno+1
print "LDA Cluster Sum",clustersum
print "\n\n"

###################

