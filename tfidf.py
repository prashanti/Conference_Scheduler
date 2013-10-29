import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from math import sqrt
import gensim
from sklearn.svm import SVC
import os
import numpy
# Source http://pyevolve.sourceforge.net/wordpress/?p=2497
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer

train_set = ("The sky is blue.", "The sun is bright.")

test_set = ("The sun in the sky is bright.",
"We can see the shining sun, the bright sun.")
stopWords = stopwords.words('english')
count_vectorizer = CountVectorizer(stop_words=stopWords, min_df=1)
#count_vectorizer = CountVectorizer(min_df=1)
count_vectorizer.fit_transform(train_set)
print "Vocabulary:", count_vectorizer.vocabulary_

# Vocabulary: {'blue': 0, 'sun': 1, 'bright': 2, 'sky': 3}

freq_term_matrix = count_vectorizer.transform(test_set)
print freq_term_matrix.todense()


######################################### TF-IDF

from sklearn.feature_extraction.text import TfidfTransformer

tfidf = TfidfTransformer(norm="l2")
tfidf.fit(freq_term_matrix)

print "IDF:", tfidf.idf_

# IDF: [ 0.69314718 -0.40546511 -0.40546511  0.        ]

###################################### Transform frequency matrix to tf-idf matrix
tf_idf_matrix = tfidf.transform(freq_term_matrix)
print tf_idf_matrix.todense()





####################################### Compute cosine similarity
#documents = [open(f) for f in text_files]
#tfidf = TfidfVectorizer().fit_transform(documents)
#documents = (
#"The sky is blue",
#"The sun is bright",
#"The sun in the sky is bright",
#"We can see the shining sun, the bright sun"
#)
documents = ("Human machine interface for lab abc computer applications",
	"A survey of user opinion of computer system response time", 
	"The EPS user interface management syste ",
	"System and human system engineering testing of EPS",
	"Relation of user perceived response time to error measurement",
	"The generation of random binary unordered trees",
	"The intersection graph of paths in trees",
	"Graph minors IV Widths of trees and well quasi ordering",
	"Graph minors A survey"
	)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words=stopWords)
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print tfidf_matrix.shape
#(4, 11)

from sklearn.metrics.pairwise import cosine_similarity
print cosine_similarity(tfidf_matrix[0:9], tfidf_matrix)
#array([[ 1.        ,  0.36651513,  0.52305744,  0.13448867]])


