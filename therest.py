







###################### Corpus from a file

class MyCorpus(object):
	def __iter__(self):
		freq=Counter()
		for line in open('TestCorpus.txt'):
			words=line.lower().split()
			tmp=Counter()
			for word in words:
				if (tmp[word]!=1):
					freq[word] +=1
				tmp[word]=1

		for line in open('TestCorpus.txt'):
			# assume there's one document per line, tokens separated by whitespace
			newline=line.lower().split()
			for word in newline:
				word=word.strip()
				if word in stoplist:
					newline.remove(word)
					#print "Removing stop",word
				if ((freq[word]==1) & (word not in stoplist)):
					newline.remove(word)
					#print "Removing freq 1",word
					1
			#dictionary.doc2bow needs a list as input
			print "Newline",newline
			yield dictionary.doc2bow(newline)

corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
for vector in corpus_memory_friendly: # load one vector into memory at a time
	1
	#print vector
corpora.MmCorpus.serialize('./storedcorpus.mm', corpus_memory_friendly) # store to disk, for later use

###################


################### TFIDF
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	1
	#print "Doc",doc

# Similarity Computation
## NOTE: In the TfIdf representation, any documents which do not share any common features with vec at all get a similarity score of 0.0.
index = similarities.SparseMatrixSimilarity(corpus_tfidf, num_features=12)
for doc in corpus_tfidf:
	sims = index[doc]
	print "TFIDF Sim",sorted(enumerate(sims), key=lambda item: -item[1])

###################


################### LSI
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=5) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
lsi.print_topics(5)

# Similarity Computation
index = similarities.MatrixSimilarity(corpus_lsi)
#printing which documnet belongs in which topic
for doc in corpus_lsi:
	sims=index[doc]
	print "LSI Sim",sorted(enumerate(sims), key=lambda item: -item[1])

###################


################### LDA
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=5,passes=10) # initialize an LSI transformation
corpus_lda = lda[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
lda.print_topics(5)

# Similarity Computation
index = similarities.MatrixSimilarity(corpus_lda)
#printing which documnet belongs in which topic
for doc in corpus_lda:
	sims=index[doc]
	print "LDA Sim",sorted(enumerate(sims), key=lambda item: -item[1])

###################




