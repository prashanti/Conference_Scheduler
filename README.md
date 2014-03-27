Python_NLP
==========
This project contains code to obtain pairwise similarity of talks from a conference. It also contains algorithms to schedule talks for the Evolution 2014 conference. 

Three topic models (LDA, LSI and TFIDF) were compared on different combinations of data (Abstracts+Titles, Titles+Keywords, Abstracts+Titles+Keywords) from the ESA 2013 conference. This comparison enabled us to make the decision on what data to gather for Evolution 2014. A write-up of this comparison is at https://www.writelatex.com/read/qdqqgpyfctgn

A randomized swapping algorithm is being explored to improve initial schedules. The algorithm starts from a real schedule and conducts 5000 iterations on the schedule to arrive at the best schedule. A write-up of this algorithm and others used for scheduling is at https://www.writelatex.com/read/vcygyjhpbzhj
