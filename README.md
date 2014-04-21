Automated_Conference_Scheduler
==========

Scheduling large conferences with several concurrent sessions manually is tedious and often results in sub-optimal schedules. Concurrent sessions need to be scheduled so as to maximize similarity of talks in the same session while minimizing overlap with talks in concurrent sessions. 

This project can automatically create optimal schedules for large conferences with concurrent sessions. The titles and abstracts from the conference submissions are analyzed using Topic Modeling algorithms such as Latent Semantic Indexing (LSI)to identify similar submissions. LSI analyzes a body of text and identifies latent topics in the text. The similarity between two talks/submissions is computed based on the distribution of latent topics for the two talks. The project consists of the following two steps


1. Computing pairwise talk similarity using LSI
2. Assigning talks to sessions to create an optimal schedule

Once the pairwise talk similarity is computed using LSI, the scores are used to guide assignment of talks to schedules. Randomized swapping algorithms create initial schedules with the required number of tidmeslots, concurrent sessions and talks per session. These initial schedules are incrementally improved by swapping two randomly selected talks from the schedule and observing whether the new schedule is better than the previous one. The swapping process is continued till no improvement is observed in the schedules. The algorithm is run several times with different initial schedules and the best schedule is picked from the improved schedules from each run. We have explored two randomized swapping algorithms: one that only accepts schedules that are better (hill climbing model) and another that accepts schedules that are worse with some probability (simulated annealing model). 

Schedules created during the swapping operations are assessed using an objective function called Discrimination Ratio (DR). The DR is the ratio of the mean intra-session similarity and inter-session session similarity. A good schedule has high intra-session similarity and low inter-session similarity. Therefore, the higher the DR, the better a schedule is. 

The code in this project was tested using submissions from the Ecological Society of America's 2013 meeting (http://eco.confex.com/eco/2013/webprogram/ORGORALS.html). It is curently being used to create schedules for the Evolution 2014 conference (http://evolution2014.org/). 
