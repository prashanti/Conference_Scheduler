Python_NLP
==========

----gensim-tfidf.py ------
This script operates on an example corpus with 9 documents and computes similarity between all pairs of documents.
The following measures of similarity are used :

1. A simple Term Frequency - Inverse Document Frequency matrix combined with cosine similarity. 
2. Latent Semantic Indexing model on the tfidf matrix combined with cosine similarity
3. Latent Dirichlet Allocation model on the tfidf matrix combined with cosine similarity

-----tfidf.py--------

This script uses Python's scikit-learn to compute cosine document similarity between all pairs of an example corpus. 
