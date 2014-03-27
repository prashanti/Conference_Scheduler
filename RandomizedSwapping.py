
def populateschedule():
	global session1,session2,session3,session4,session5,session6,session7,session8,schedule,alldocs,alldocs1
	schedule=[]
	alldocs=range(1,325)
	alldocs1=range(1,325)
	session1=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]]
	session2=[[50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [60, 61, 62, 63, 64, 65, 66, 67, 68], [69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [79, 80, 81, 82, 83, 84, 85, 86], [87, 88, 89, 90, 91, 92, 93]]
	session3=[[94, 95, 96, 97, 98, 99, 100, 101, 102], [103, 104, 105, 106, 107, 108, 109, 110, 111, 112], [113, 114, 115, 116, 117, 118, 119, 120, 121, 122], [123, 124, 125, 126, 127, 128, 129, 130, 131, 132]]
	session4=[[133, 134, 135, 136, 137, 138, 139, 140, 141, 142], [143, 144, 145, 146, 147, 148, 149, 150, 151, 152], [153, 154, 155, 156, 157, 158, 159, 160, 161, 162], [163, 164, 165, 166, 167, 168, 169, 170, 171, 172], [173, 174, 175, 176, 177, 178, 179, 180, 181, 182]]
	session5= [[183, 184, 185, 186, 187, 188, 189, 190, 191, 192], [193, 194, 195, 196, 197, 198, 199, 200, 201], [202,203, 204, 205, 206, 207, 208, 209, 210, 211]]

	session6=[[212, 213, 214, 215, 216, 217, 218, 219, 220, 221], [222, 223, 224, 225, 226, 227, 228, 229, 230, 231], [232, 233, 234, 235, 236, 237, 238, 239, 240], [241, 242, 243, 244, 245, 246, 247, 248, 249, 250]]
	session7=[[251, 252, 253, 254, 255], [256, 257, 258, 259, 260, 261, 262, 263, 264], [265, 266, 267, 268, 269, 270, 271, 272, 273, 274], [275, 276, 277, 278, 279, 280, 281, 282, 283, 284]]
	session8=[[285, 286, 287, 288, 289, 290, 291, 292, 293, 294], [295, 296, 297, 298, 299, 300, 301, 302, 303, 304], [305, 306, 307, 308, 309, 310, 311, 312, 313, 314], [315, 316, 317, 318, 319, 320, 321, 322, 323, 324]]


	schedule.append(session1)
	schedule.append(session2)
	schedule.append(session3)
	schedule.append(session4)
	schedule.append(session5)
	schedule.append(session6)
	schedule.append(session7)
	schedule.append(session8)

def populatetestschedule():
	global session1,session2,schedule,alldocs,alldocs1
	schedule=[]
	alldocs=range(1,9)
	alldocs1=range(1,9)
	session1=[[1,2],[3,4]]
	session2=[[5,6],[7,8]]
	schedule.append(session1)
	schedule.append(session2)

def calculateintrasimilarity(timeslot):
	global intrasimlist
	#intrasimlist=[]
	# this is like [[1,2],[3,4],[5,6]]
	# do 1 2, 3 4, 5 6 and add 3 values to intralist
	for session in timeslot:
		for i in range (0, len(session)):
			for j in range(i+1, len(session)):
				doc1=session[i]
				doc2=session[j]
				intrasimlist.append(scorematrix[doc1-1][doc2-1])
				#print "Sim of "+ str(doc1) + " " + str(doc2) +" is "+ str(scorematrix[doc1-1][doc2-1])


def calculateintersimilarity(timeslot):
	global intersimlist
	#intersimlist=[]
	# this is like [[1,2,9],[3,4]]
	# do 1 3, 1 4, 2 3, 2 4, 9 3, 9 4 and add 6 values to list
	for i in range (0,len(timeslot)):
		for j in range (i+1,len(timeslot)):
			for p in range (0,len(timeslot[i])):
				for q in range(0, len(timeslot[j])):
					doc1=timeslot[i][p]
					doc2=timeslot[j][q]
					intersimlist.append(scorematrix[doc1-1][doc2-1])
					#print "Sim of "+ str(doc1) + " " + str(doc2) +" is "+ str(scorematrix[doc1-1][doc2-1])

def calculate(schedule):
	global intersimlist,intrasimlist
	intersimlist=[]
	intrasimlist=[]
	for timeslot in schedule:
		calculateintersimilarity(timeslot)
		calculateintrasimilarity(timeslot)


def populatescorematrix():
	global scorematrix
	pairwisescores=str(sys.argv[1])
	scorefile=open(pairwisescores,'r')
	for line in scorefile:
		rowscores=[]
		scores=line.split("\t")
		for score in scores:
			rowscores.append(float(score.strip()))
		scorematrix.append(rowscores)


def sort(schedule):
	sortedschedule=[]
	for timeslot in schedule:
		sortedtimeslot=[]
		for session in timeslot:
			sortedtimeslot.append(sorted(session))
		sortedschedule.append(sortedtimeslot)
	return(sortedschedule)



def randomalldocs():
	global alldocs1
	listoflist=[]
	i=0
	j=0
	while i<5:
		x=[]
		j=0
		while j<5:
			random=choice(alldocs1)
			alldocs1=filter(lambda a: a != random, alldocs1)
			x.append(random)
			j+=1
		listoflist.append(x)
		i+=1
	return listoflist 			

def randomizeschedule():
	global schedule,alldocs1
	newschedule=[]
	for timeslot in schedule:
		newtimeslot=[]
		for session in timeslot:
			newsession=[]
			for talknumber in session:
				random=choice(alldocs1)
				alldocs1=filter(lambda a: a != random, alldocs1)
				newsession.append(random)
			newtimeslot.append(newsession)
		newschedule.append(newtimeslot)
	schedule = copy.deepcopy(newschedule)







def main():
	count=str(sys.argv[2])
	random=str(sys.argv[3])


	global schedule,intrasimlist,intersimlist,alldocs
	populateschedule()
	populatescorematrix()
	if random is '1':
		
		drfile="Random_DR_Randomized_"+str(count)+".txt"
		swapfile="Random_Swap_Randomized_"+str(count)+".txt"
		bestdrout=open("Random_BestDR.txt",'a')
		startingschedulefile="Random_StartingSchedule.txt"
		startingschedule=open(startingschedulefile,'a')
		finalschedulefile="Random_BestSchedule.txt"
		finalschedule=open(finalschedulefile,'a')
		randomizeschedule()
	else:
		drfile="DR_Randomized_"+str(count)+".txt"
		swapfile="Swap_Randomized_"+str(count)+".txt"
		bestdrout=open("BestDR.txt",'a')
	drout=open(drfile,'w')
	swapout=open(swapfile,'w')
	if random is '1':
		
		startingschedule.write(count+"\t")
    	json.dump(schedule,startingschedule)
    	startingschedule.write("\n")
	calculate(schedule)
	originalschedule = copy.deepcopy(schedule)
	intramean=numpy.mean(intrasimlist)
	intermean=numpy.mean(intersimlist)
	drmean=intramean/intermean
	

	intramedian=numpy.median(intrasimlist)
	intermedian=numpy.median(intersimlist)
	drmedian=intramedian/intermedian
	#print "Initial DR Mean " +str(round(drmean,3))
	#print "Initial DR Median "+ str(round(drmedian,3))
	drout.write(str(round(drmedian,3))+"\n")
	#print "\n\n"

	
	better=0
	while (better<5000):

		
		tempschedule=copy.deepcopy(schedule)
		x=choice(alldocs)
		y=choice(alldocs)

		for timeslot in schedule:
			for session in timeslot:
				if x in session:
					xindex= session.index(x)
					xsessionindex= timeslot.index(session)
					xtimeslotindex=schedule.index(timeslot)

		for timeslot in schedule:
			for session in timeslot:
				if y in session:
					yindex=session.index(y)
					ysessionindex= timeslot.index(session)
					ytimeslotindex= schedule.index(timeslot)

		#DR Mean 4.02724661516
		#DR Median 5.54749218832
		# the talks to be swapped are in the same session. 
		if xsessionindex==ysessionindex and xtimeslotindex==ytimeslotindex:
			1

		else:
			better+=1
			tempschedule[ytimeslotindex][ysessionindex][yindex],tempschedule[xtimeslotindex][xsessionindex][xindex] = tempschedule[xtimeslotindex][xsessionindex][xindex], tempschedule[ytimeslotindex][ysessionindex][yindex] 
			
			calculate(tempschedule)
			intramean=numpy.mean(intrasimlist)
			intermean=numpy.mean(intersimlist)
			newdrmean=intramean/intermean
			

			intramedian=numpy.median(intrasimlist)
			intermedian=numpy.median(intersimlist)
			newdrmedian=intramedian/intermedian
			
			if newdrmedian > drmedian:
				
				#print "starting with"
				#print schedule
				schedule=copy.deepcopy(tempschedule)
				#print "Swapping "+str(x)+" "+str(y)
				swapout.write("Swapping "+str(x)+" "+str(y)+"\n")
				#print "DR Mean " +str(round(newdrmean,3))
				#print "DR Median "+ str(round(newdrmedian,3))
				#print "better schedule"
				#print schedule
				#print "\n\n"
				drmean=newdrmean
				drmedian=newdrmedian
				drout.write(str(round(newdrmedian,3))+"\n")
			else:
				# print "starting with"
				# print schedule
				# print "Swapped "+str(x)+" "+str(y)
				# print tempschedule
				# print "Not a better schedule"
				# print "Reverting schedule to"
				# print schedule
				# print "\n\n"
				1
				drout.write(str(round(drmedian,3))+"\n")
			
	
			
	finalschedule.write(count+"\t")
	json.dump(schedule,finalschedule)
	finalschedule.write("\n")

	bestdrout.write(str(count)+"\t"+str(round(drmedian,3))+"\n")
				

#Swapping 14 126
#DR Mean 4.05397611394
#DR Median 5.5756109202




if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	from random import choice
	from datetime import datetime
	scorematrix=[]
	session1=[]
	session2=[]
	session3=[]
	session4=[]
	session5=[]
	session6=[]
	session7=[]
	session8=[]
	schedule=[]
	alldocs1=[]
	intrasimlist=[]
	intersimlist=[]
	alldocs=[]
	main()
