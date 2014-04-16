import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import math
import gensim
from collections import Counter
from stemming.porter2 import stem
import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy as np
from gensim import corpora, models, similarities
import sys
import scipy.stats
from random import choice
session1=[]
allsessions=[]
################### Creating a set of stopwords
stoplist=set()
for line in open('stopwords.txt'):
	line=line.strip()
	stoplist.add(line.lower())
###################

notopics=30


#out = open('AllResults.txt','a')
dist = open('Distribution.txt','a')
dorandom=0

#inputfile='ESA-Corpus-Titles.txt'
#inputfile='ESA-Corpus-Titles+Abstracts.txt'
#inputfile='ESA-Corpus-Titles+Keywords-100topics.txt'
inputfile='ESA-Corpus-Titles+Abstracts+Keywords-100topics.txt'


tfidfclustersum=0
lsiclustersum=0
ldaclustersum=0
combinations=0
mastertfidfintercluster=0
masterlsiintercluster=0
masterldaintercluster=0


mastertfidfintracluster=0
masterlsiintracluster=0
masterldaintracluster=0

tfidfintermedianlist=[]
lsiintermedianlist=[]
ldaintermedianlist=[]

def evolutiontestsessions():
	global session1,session2
	session1=[[1,2],[3,4]]
	session2=[[5,6]]
	allsessions.append(session1)
	allsessions.append(session2)
	return allsessions
def evolutionsessions():
	global session1,session2,session3,session4,session5,session6,session7,allsessions
	session1=[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34], [35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46], [47, 48, 49, 50, 51], [52, 53, 54, 55, 56, 57], [58, 59, 60, 61], [62, 63, 64, 65, 66, 67], [68, 69, 70, 71, 72, 73], [74, 75, 76, 77, 78, 79], [80, 81, 82, 83, 84, 85], [86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96], [97, 98, 99, 100, 101], [102, 103, 104, 105, 106], [107, 108, 109, 110, 111], [112, 113, 114, 115, 116], [117, 118, 119, 120, 121, 122,123]]
	session2=[[124, 125, 126, 127, 128, 129], [130, 131, 132, 133, 134, 135], [136], [141, 142, 143, 144, 145, 146], [147, 148, 149, 150, 151, 152], [153, 154, 155, 156, 157, 158], [159, 160, 161, 162, 163], [164, 165, 166, 167, 168, 169], [170, 171, 172, 173, 174, 175], [176, 177, 178, 179, 180, 181], [182, 183, 184, 185, 186], [187, 188, 189, 190, 191, 192], [193, 194, 195, 196, 197, 198], [199, 200, 201, 202, 203, 204], [205, 206, 207, 208, 209, 210], [211, 212, 213, 214, 215, 216], [217, 218, 219, 220, 221, 222], [223, 224, 225, 226, 227, 228], [229, 230, 231, 232, 233], [234, 235, 236, 237, 238], [239, 240, 241, 242], [243, 244, 245, 246, 247], [248, 249, 250, 251, 252, 253]]
	session3=[[255, 256, 257, 258], [259, 260, 261, 262, 263, 264], [265, 266, 267, 268, 269, 270], [271, 272, 273, 274, 275, 276], [277, 278, 279, 280, 281, 282], [283, 284, 285, 286, 287, 288], [289, 290, 291, 292, 293], [294, 295, 296, 297, 298, 299], [300, 301, 302, 303, 304], [305, 306, 307, 308, 309, 310], [311, 312, 313, 314, 315, 316], [317, 318, 319, 320, 321, 322], [323, 324, 325, 326, 327, 328], [329, 330, 331, 332, 333, 334], [335, 336, 337, 338, 339], [340, 341, 342, 343, 344], [345, 346, 347, 348, 349, 350], [351, 352, 353, 354, 355, 356], [357, 358, 359, 360, 361, 362], [363, 364, 365, 366, 367, 368], [369, 370, 371, 372], [373, 374, 375, 376, 377, 378]]
	session4=[[379, 380, 381, 382, 383, 384], [379, 380, 381, 382, 383, 384], [390, 391, 392, 393, 394, 395], [396, 397, 398, 399, 400], [401, 402, 403, 404, 405, 406], [407, 408, 409, 410, 411, 412], [413, 414, 415, 416, 417], [418, 419, 420, 421], [422, 423, 424, 425, 426, 427], [428, 429, 430, 431, 432], [433, 434, 435, 436, 437, 438], [439, 440, 441, 442, 443, 444], [445, 446, 447, 448, 449, 450], [451, 452, 453, 454, 455, 456], [457, 458, 459, 460, 461, 462], [463, 464, 465, 466, 467, 468], [469, 470, 471, 472], [473, 474, 475, 476, 477, 478], [479, 480, 481, 482, 483], [484, 485, 486, 487, 488, 489], [490, 491, 492, 493, 494, 495], [496, 497, 498, 499, 500, 501], [502, 503, 504, 505, 506, 507]]
	session5=[[508, 509, 510, 511, 512, 513, 514], [515, 516, 517, 518, 519, 520], [521, 522, 523, 524, 525], [526, 527, 528, 529, 530], [531, 532, 533, 534, 535, 536], [537, 538, 539, 540, 541], [542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559], [560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577], [578, 579, 580, 581, 582, 583], [584, 585, 586, 587, 588, 589], [590, 591, 592, 593, 594, 595], [596, 597, 598, 599, 600, 601], [602, 603, 604, 605, 606], [607, 608, 609, 610, 611, 612], [613, 614, 615, 616, 617, 618], [619, 620, 621, 622, 623], [624, 625, 626, 627, 628], [629, 630, 631, 632, 633, 634], [635, 636, 637, 638, 639, 640], [641, 642, 643, 644], [645, 646, 647, 648, 649, 650], [651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668], [669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686]]
	session6=[[687, 688, 689, 690, 691, 692], [693, 694, 695, 696, 697, 698], [699, 700, 701, 702, 703, 704], [705, 706, 707, 708, 709, 710], [711, 712, 713, 714, 715, 716], [717, 718, 719, 720, 721, 722], [723, 724, 725, 726, 727, 728], [729, 730, 731, 732, 733, 734], [735, 736, 737, 738, 739], [740, 741, 742, 743, 744], [745, 746, 747, 748, 749, 750], [751, 752, 753, 754, 755, 756], [757, 758, 759, 760, 761, 762], [763, 764, 765, 766, 767, 768], [769, 770, 771, 772], [773, 774, 775, 776, 777, 778], [779, 780, 781, 782], [783, 784, 785, 786, 787, 788], [789, 790, 791, 792, 793, 794], [795, 796, 797, 798, 799], [800, 801, 802, 803, 804, 805]]
	session7=[[806, 807, 808, 809, 810], [811, 812, 813, 814, 815], [816, 817, 818, 819, 820], [821, 822, 823, 824, 825, 826], [827, 828, 829, 830], [832, 833, 834, 835, 836], [837, 838, 839, 840, 841, 842], [843, 844, 845, 846, 847, 848], [849, 850, 851, 852], [853, 854, 855, 856, 857], [858, 859, 860, 861, 862, 863], [864, 865, 866, 867], [868, 869, 870, 871, 872, 873], [874, 875, 876, 877, 878, 879], [880, 881, 882, 883, 884], [885, 886, 887, 888, 889, 890], [891, 892, 893, 894], [895, 896, 897, 898, 899, 900], [901, 902, 903, 904, 905, 906], [907, 908, 909, 910, 911], [912,913,914,915,916]]
	allsessions.append(session1)
	allsessions.append(session2)
	allsessions.append(session3)
	allsessions.append(session4)
	allsessions.append(session5)
	allsessions.append(session6)
	allsessions.append(session7)
def esasessions():
	global session1,session2,session3,session4,session5,session6,session7,session8,allsessions


	session1=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]]
	session2=[[50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [60, 61, 62, 63, 64, 65, 66, 67, 68], [69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [79, 80, 81, 82, 83, 84, 85, 86], [87, 88, 89, 90, 91, 92, 93]]
	session3=[[94, 95, 96, 97, 98, 99, 100, 101, 102], [103, 104, 105, 106, 107, 108, 109, 110, 111, 112], [113, 114, 115, 116, 117, 118, 119, 120, 121, 122], [123, 124, 125, 126, 127, 128, 129, 130, 131, 132]]
	session4=[[133, 134, 135, 136, 137, 138, 139, 140, 141, 142], [143, 144, 145, 146, 147, 148, 149, 150, 151, 152], [153, 154, 155, 156, 157, 158, 159, 160, 161, 162], [163, 164, 165, 166, 167, 168, 169, 170, 171, 172], [173, 174, 175, 176, 177, 178, 179, 180, 181, 182]]
	session5= [[183, 184, 185, 186, 187, 188, 189, 190, 191, 192], [193, 194, 195, 196, 197, 198, 199, 200, 201], [203, 204, 205, 206, 207, 208, 209, 210, 211]]

	session6=[[212, 213, 214, 215, 216, 217, 218, 219, 220, 221], [222, 223, 224, 225, 226, 227, 228, 229, 230, 231], [232, 233, 234, 235, 236, 237, 238, 239, 240], [241, 242, 243, 244, 245, 246, 247, 248, 249, 250]]
	session7=[[251, 252, 253, 254, 255], [256, 257, 258, 259, 260, 261, 262, 263, 264], [265, 266, 267, 268, 269, 270, 271, 272, 273, 274], [275, 276, 277, 278, 279, 280, 281, 282, 283, 284]]
	session8=[[285, 286, 287, 288, 289, 290, 291, 292, 293, 294], [295, 296, 297, 298, 299, 300, 301, 302, 303, 304], [305, 306, 307, 308, 309, 310, 311, 312, 313, 314], [315, 316, 317, 318, 319, 320, 321, 322, 323, 324]]
	allsessions.append(session1)
	allsessions.append(session2)
	allsessions.append(session3)
	allsessions.append(session4)
	allsessions.append(session5)
	allsessions.append(session6)
	allsessions.append(session7)
	allsessions.append(session8)
	return allsessions

def setevolution():
	the_list=evolutiontestsessions()
	return the_list
	

def setesa():
	the_list=esasessions()
	return the_list

def createsession():
	global allsessions
	the_list=allsessions
	return the_list

def createrandomsession(the_list):
	#the_list=createsession()
	alldocs=range(1,325)
	for matrix in the_list:
		for element in matrix:
			random=choice(alldocs)
			matrix[matrix.index(element)] = random
			alldocs=filter(lambda a: a != random, alldocs)
	return(the_list)

def createrandomsessionnew(session):
	randomsession=[]
	for outerlist in session:
		temp=[]
		for innerlist in session:
			if innerlist != []:
				random=choice(innerlist)
				temp.append(random)
				session=filter(lambda a: a != innerlist, session)
				innerlist=filter(lambda a: a != random, innerlist)
				session.append(innerlist)
		randomsession.append(temp)
	return(randomsession)

def randomalldocs():
	listoflist=[]
	i=0
	alldocs=range(1,324)
	j=0
	while i<5:
		x=[]
		j=0
		while j<10:
			random=choice(alldocs)
			alldocs=filter(lambda a: a != random, alldocs)
			x.append(random)
			j+=1
		listoflist.append(x)
		i+=1
	return listoflist

def intercluster(simlist,the_list,model):
	
	model=model.strip()
	global tfidfintermedianlist
	global lsiintermedianlist
	global ldaintermedianlist
	for x in the_list:
		for y in the_list:
			if set(x) != set(y):
				sum=0
				for doc1 in x:
					for doc2 in y:
						if model is "tfidf":
							tfidfintermedianlist.append(simlist[doc1-1][doc2-1])
						if model is "lsi":
							lsiintermedianlist.append(simlist[doc1-1][doc2-1])
						if model is "lda":
							ldaintermedianlist.append(simlist[doc1-1][doc2-1])	
		the_list=filter(lambda a: a != x, the_list)

def getkeywords():
	f = open('keywords-100topics.txt','w')
	for doc in corpus_lsi: 
		keywords=set()
		doc.sort(key=lambda tup: tup[1], reverse=True)
		#print doc[0][0] # this is the top topic for this document
		#print doc[1][0] # this is the next best topic for this document
		#print "this",doc
		i=0
		while (i<4):
			#print "index",doc[i][0]
			topicscore1=lsi.show_topic(doc[i][0], topn=2)
			keywords.add(topicscore1[0][1])
			keywords.add(topicscore1[1][1])
			i+=1
		f.write(' '.join(keywords))
		f.write("\n")





#the_list=setevolution()

masterlist=setesa()
#masterlist=setevolution()


################### 

dictionary = corpora.Dictionary([[stem(word) for word in line.lower().split()] for line in open(inputfile)])
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) 
dictionary.compactify() 
dictionary.save('./storeddictionary.dict') 


###################




###################### Corpus from a file

class MyCorpus(object):
	def __iter__(self):
		freq=Counter()
		for line in open(inputfile):
			words=line.lower().split()
			tmp=Counter()
			for word in words:
				word=stem(word).strip()
				if (tmp[word]!=1):
					freq[word] +=1
				tmp[word]=1


		for line in open(inputfile):
			# assume there's one document per line, tokens separated by whitespace
			newline=list()
			newline=[stem(word) for word in line.lower().split()]
			for word in newline:
				word=word.strip()
				if word in stoplist:
					newline = filter(lambda a: a != word, newline)
				if ((freq[word]==1) & (word not in stoplist)):
					newline = filter(lambda a: a != word, newline)
					1
			yield dictionary.doc2bow(newline)

corpus_memory_friendly = MyCorpus() 
corpora.MmCorpus.serialize('./storedcorpus.mm', corpus_memory_friendly) 

	###################


	################### Load the stored dictionary and corpu

dictionary = corpora.Dictionary.load('./storeddictionary.dict')
corpus = corpora.MmCorpus('./storedcorpus.mm')

	###################


# Creating Models here
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=notopics)
corpus_lsi = lsi[corpus_tfidf]

lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=notopics,passes=40) 
corpus_lda = lda[corpus_tfidf]



tfidfintramedianlist=[]
lsiintramedianlist=[]
ldaintramedianlist=[]
for the_list in masterlist:
	#the_list=createrandomsessionnew(the_list)
	if dorandom ==1:
		the_list=randomalldocs()
		#print the_list,"\n\n"
	for eachcluster in the_list:


		################### TFIDF
		tfidfsimlist=[]
		index = similarities.MatrixSimilarity(corpus_tfidf)
		docno=1
		cluster=eachcluster
		for doc in corpus_tfidf:
			sims = index[doc]
			tfidfsimlist.append(list(sims))
			testlist= list(enumerate(sims))
			#print testlist
			if docno in cluster:
				for item in cluster:
					if docno != item:
						#print "doing",docno,item
						#print "sim is",testlist[item-1][1]
						tfidfintramedianlist.append(testlist[item-1][1])
				cluster=filter(lambda a: a != docno, cluster)
			docno=docno+1


		###################



		################## LSI 
		lsisimlist=[]
		index = similarities.MatrixSimilarity(corpus_lsi)
		docno=1
		cluster=eachcluster
		for doc in corpus_lsi:
			sims = index[doc]
			lsisimlist.append(list(sims))
			testlist= list(enumerate(sims))
			if docno in cluster:
				for item in cluster:
					if docno != item:
						lsiintramedianlist.append(testlist[item-1][1])
				cluster=filter(lambda a: a != docno, cluster)
			docno=docno+1


		###################

		################### LDA
		ldasimlist=[] 
		index = similarities.MatrixSimilarity(corpus_lda)
		docno=1
		cluster=eachcluster
		for doc in corpus_lda:
			sims = index[doc]
			ldasimlist.append(list(sims))
			testlist= list(enumerate(sims))
			if docno in cluster:
				for item in cluster:
					if docno != item:
						ldaintramedianlist.append(testlist[item-1][1])
				cluster=filter(lambda a: a != docno, cluster)
			docno=docno+1


		


		###################

	intercluster(tfidfsimlist,the_list,"tfidf")
	intercluster(lsisimlist,the_list,"lsi")
	intercluster(ldasimlist,the_list,"lda")



# print "TFIDF  Within Cluster Mean", np.mean(tfidfintramedianlist)
# print "LSI  Within Cluster Mean", np.mean(lsiintramedianlist)
# print "LDA  Within Cluster Mean", np.mean(ldaintramedianlist)

# print "TFIDF  Between Cluster Mean", np.mean(tfidfintermedianlist)
# print "LSI  Between Cluster Mean", np.mean(lsiintermedianlist)
# print "LDA  Between Cluster Mean", np.mean(ldaintermedianlist)





# print "TFIDF  Within Cluster Median", np.median(tfidfintramedianlist)
# print "LSI  Within Cluster Median", np.median(lsiintramedianlist)
# print "LDA  Within Cluster Median", np.median(ldaintramedianlist)

#print np.median(tfidfintramedianlist)-np.percentile(tfidfintramedianlist,25),"\t",np.percentile(tfidfintramedianlist,75)-np.median(tfidfintramedianlist)
#print np.median(lsiintramedianlist)-np.percentile(lsiintramedianlist,25),"\t",np.percentile(lsiintramedianlist,75)-np.median(lsiintramedianlist)
#print np.median(ldaintramedianlist)-np.percentile(ldaintramedianlist,25),"\t",np.percentile(ldaintramedianlist,75)-np.median(ldaintramedianlist)
#print"\n\n"

# print "TFIDF  Between Cluster Median", np.median(tfidfintermedianlist)
# print "LSI  Between Cluster Median", np.median(lsiintermedianlist)
# print "LDA  Between Cluster Median", np.median(ldaintermedianlist)

#print np.median(tfidfintermedianlist)-np.percentile(tfidfintermedianlist,25),"\t",np.percentile(tfidfintermedianlist,75)-np.median(tfidfintermedianlist)
#print np.median(lsiintermedianlist)-np.percentile(lsiintermedianlist,25),"\t",np.percentile(lsiintermedianlist,75)-np.median(lsiintermedianlist)
#print np.median(ldaintermedianlist)-np.percentile(ldaintermedianlist,25),"\t",np.percentile(ldaintermedianlist,75)-np.median(ldaintermedianlist)

#print"\n\n" 
# print "TFIDF Median Ratio", np.median(tfidfintramedianlist)/np.median(tfidfintermedianlist)
# print "LSI Median Ratio", np.median(lsiintramedianlist)/np.median(lsiintermedianlist)
# print "LDA Median Ratio", np.median(ldaintramedianlist)/np.median(ldaintermedianlist)

#print"\n\n"

print "TFIDF Mean Ratio", np.mean(tfidfintramedianlist)/np.mean(tfidfintermedianlist)
print "LSI Mean Ratio", np.mean(lsiintramedianlist)/np.mean(lsiintermedianlist)
print "LDA Mean Ratio", np.mean(ldaintramedianlist)/np.mean(ldaintermedianlist)









tfidfintrase=scipy.stats.tstd(tfidfintramedianlist)/math.sqrt(len(tfidfintramedianlist))
tfidfinterse=scipy.stats.tstd(tfidfintermedianlist)/math.sqrt(len(tfidfintermedianlist))

lsiintrase=scipy.stats.tstd(lsiintramedianlist)/math.sqrt(len(lsiintramedianlist))
lsiinterse=scipy.stats.tstd(lsiintermedianlist)/math.sqrt(len(lsiintermedianlist))

ldaintrase=scipy.stats.tstd(ldaintramedianlist)/math.sqrt(len(ldaintramedianlist))
ldainterse=scipy.stats.tstd(ldaintermedianlist)/math.sqrt(len(ldaintermedianlist))

dist.write(inputfile+"\n")
dist.write("TFIDF" +"\n" + str(tfidfintramedianlist)+"\n")
dist.write("LSI" +"\n" + str(lsiintramedianlist)+"\n")
dist.write("LDA" +"\n" + str(ldaintramedianlist)+"\n")

#tfidf = open('TFIDF-Random.txt','a')
#lsi = open('LSI-Random.txt','a')
#lda = open('LDA-Random.txt','a')


#######
#Model	Mean_Similarity	STDE	Data	Similarity_Type
# tfidfstring="TFIDF"+"\t"+ str(np.mean(tfidfintramedianlist))+ "\t"+str(tfidfintrase)+"\t"+inputfile+ "\t" +"Intra_Session_Similarity"+"\n"
# tfidf.write(tfidfstring)

# tfidfstring="TFIDF"+"\t"+ str(np.mean(tfidfintermedianlist))+ "\t"+str(tfidfinterse)+"\t"+inputfile+ "\t" +"Inter_Session_Similarity"+"\n"
# tfidf.write(tfidfstring)

# ######

# lsistring="LSI"+"\t"+ str(np.mean(lsiintramedianlist))+ "\t"+str(lsiintrase)+"\t"+inputfile+ "\t" +"Intra_Session_Similarity"+"\n"
# lsi.write(lsistring)

# lsistring="LSI"+"\t"+ str(np.mean(lsiintermedianlist))+ "\t"+str(lsiinterse)+"\t"+inputfile+ "\t" +"Inter_Session_Similarity"+"\n"
# lsi.write(lsistring)
# #######

# ldastring="LDA"+"\t"+ str(np.mean(ldaintramedianlist))+ "\t"+str(ldaintrase)+"\t"+inputfile+ "\t" +"Intra_Session_Similarity"+"\n"
# lda.write(ldastring)

# ldastring="LDA"+"\t"+ str(np.mean(ldaintermedianlist))+ "\t"+str(ldainterse)+"\t"+inputfile+ "\t" +"Inter_Session_Similarity"+"\n"
# lda.write(ldastring)

#########
#getkeywords()
