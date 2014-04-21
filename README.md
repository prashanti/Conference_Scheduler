Automated_Conference_Scheduler
==========

Scheduling large conferences with several concurrent sessions manually is tedious and often results in sub-optimal schedules. Concurrent sessions need to be scheduled so as to maximize similarity of talks in the same session while minimizing overlap with talks in concurrent sessions. 

This project can automatically create optimal schedules for large conferences with concurrent sessions. The titles and abstracts from the conference submissions are analyzed using Topic Modeling algorithms such as Latent Semantic Indexing (LSI)to identify similar submissions. LSI analyzes a body of text and identifies latent topics in the text. The similarity between two talks/submissions is computed based on the distribution of latent topics for the two talks. The project consists of two steps:
1. Computing pairwise talk similarity using LSI
2.   



This project contains code to obtain pairwise similarity of talks from a conference. It also contains algorithms to schedule talks for the Evolution 2014 conference. 

Three topic models (LDA, LSI and TFIDF) were compared on different combinations of data (Abstracts+Titles, Titles+Keywords, Abstracts+Titles+Keywords) from the ESA 2013 conference. This comparison enabled us to make the decision on what data to gather for Evolution 2014. A write-up of this comparison is at https://www.writelatex.com/read/qdqqgpyfctgn

A randomized swapping algorithm is being explored to improve initial schedules. The algorithm starts from a real schedule and conducts 5000 iterations on the schedule to arrive at the best schedule. A write-up of this algorithm and others used for scheduling is at https://www.writelatex.com/read/vcygyjhpbzhj
