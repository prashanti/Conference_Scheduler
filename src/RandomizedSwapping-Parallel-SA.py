def populateschedulefromfile():
	schedule=[]
	schedulefile=sys.argv[1]
	with open(schedulefile) as f:
		schedule = json.load(f)
	return(schedule)

def populatetestschedule():
	schedule=[]
	alldocs=range(1,325)
	alldocs1=range(1,9)
	session1=[[1,2],[3,4]]
	session2=[[5,6],[7,8]]
	schedule.append(session1)
	schedule.append(session2)

def calculateintrasimilarity(timeslot, intrasimlist,scorematrix):
	for session in timeslot:
		for i in range (0, len(session)):
			for j in range(i+1, len(session)):
				doc1=session[i]
				doc2=session[j]
				intrasimlist.append(scorematrix[doc1-1][doc2-1])
				#print "Sim of "+ str(doc1) + " " + str(doc2) +" is "+ str(scorematrix[doc1-1][doc2-1])
	return intrasimlist

def calculateintersimilarity(timeslot, intersimlist,scorematrix):
	for i in range (0,len(timeslot)):
		for j in range (i+1,len(timeslot)):
			for p in range (0,len(timeslot[i])):
				for q in range(0, len(timeslot[j])):
					doc1=timeslot[i][p]
					doc2=timeslot[j][q]
					intersimlist.append(scorematrix[doc1-1][doc2-1])
					#print "Sim of "+ str(doc1) + " " + str(doc2) +" is "+ str(scorematrix[doc1-1][doc2-1])

	return intersimlist

def calculate(schedule,scorematrix):
	intersimlist=[]
	intrasimlist=[]
	for timeslot in schedule:
		intersimlist = calculateintersimilarity(timeslot, intersimlist,scorematrix)
		intrasimlist = calculateintrasimilarity(timeslot, intrasimlist,scorematrix)
	return intersimlist,intrasimlist

def populatescorematrix():
	scorematrix=[]
	pairwisescores=str(sys.argv[2])
	scorefile=open(pairwisescores,'r')
	for line in scorefile:
		rowscores=[]
		scores=line.split("\t")
		for score in scores:
			rowscores.append(float(score.strip()))
		scorematrix.append(rowscores)
	return scorematrix

def sort(schedule):
	sortedschedule=[]
	for timeslot in schedule:
		sortedtimeslot=[]
		for session in timeslot:
			sortedtimeslot.append(sorted(session))
		sortedschedule.append(sortedtimeslot)
	return(sortedschedule)

def randomflagizeschedulewithparameters(timeslots,sessions,talks):
	alldocs1=range(1,325)
	newschedule=[]
	for timeslot in range(1,timeslots+1):
		newtimeslot=[]
		for session in range(1,sessions+1):
			newsession=[]
			for talknumber in range(1,talks+1):
				randomflag=choice(alldocs1)
				alldocs1=filter(lambda a: a != randomflag, alldocs1)
				newsession.append(randomflag)
			newtimeslot.append(newsession)
		newschedule.append(newtimeslot)
	return(newschedule)			

def randomflagizeschedule(schedule):
	alldocs1=range(1,325)
	newschedule=[]
	for timeslot in schedule:
		newtimeslot=[]
		for session in timeslot:
			newsession=[]
			for talknumber in session:
				randomflag=choice(alldocs1)
				alldocs1=filter(lambda a: a != randomflag, alldocs1)
				newsession.append(randomflag)
			newtimeslot.append(newsession)
		newschedule.append(newtimeslot)
	return(newschedule)




def log_results(result):
	results.append(result)

def calculateprobability(prev_score,next_score,temperature):
    if next_score > prev_score:
        return 1.0
    else:
        return math.exp( -abs(next_score-prev_score)/temperature )

def kirkpatrick_cooling(start_temp,alpha):
    T=start_temp
    while True:
        yield T
        T=alpha*T


def worker(count,randomflag,schedule,scorematrix,iterations):

	cooling=kirkpatrick_cooling(50000,0.6)

	alldocs=range(1,325)
	intrasimlist=[]
	intersimlist=[]
	drdistribution=[]
	if randomflag == 1:
		schedule=randomflagizeschedule(schedule)

	
	intersimlist,intrasimlist = calculate(schedule,scorematrix)
	originalschedule = copy.deepcopy(schedule)
	intramean=numpy.mean(intrasimlist)
	intermean=numpy.mean(intersimlist)
	drmean=intramean/intermean
	

	intramedian=numpy.median(intrasimlist)
	intermedian=numpy.median(intersimlist)
	drmedian=intramedian/intermedian
	bestsolution=drmedian
	# print "Initial DR Mean " +str(drmean)
	# print "Initial DR Median "+ str(drmedian)
	
	drdistribution.append(round(drmedian,3))



	
	better=0
	for temperature in cooling:
		
		if better<iterations:

			
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

	 		
			if xsessionindex==ysessionindex and xtimeslotindex==ytimeslotindex:
				1
				
			else:
				better+=1
				tempschedule[ytimeslotindex][ysessionindex][yindex],tempschedule[xtimeslotindex][xsessionindex][xindex] = tempschedule[xtimeslotindex][xsessionindex][xindex], tempschedule[ytimeslotindex][ysessionindex][yindex] 
				
				intersimlist,intrasimlist = calculate(tempschedule,scorematrix)

				intramean=numpy.mean(intrasimlist)
				intermean=numpy.mean(intersimlist)
				newdrmean=intramean/intermean
							

				intramedian=numpy.median(intrasimlist)
				intermedian=numpy.median(intersimlist)
				newdrmedian=intramedian/intermedian
				probability=0
				
				if newdrmedian>bestsolution:
					bestsolution=newdrmedian
				probability=calculateprobability(drmedian,newdrmedian,temperature)
				
				randomnumber=random.random()
			
				
				if randomnumber < probability:
					schedule=copy.deepcopy(tempschedule)
					drmean=newdrmean
					drmedian=newdrmedian
					
					drdistribution.append(round(newdrmedian,3))
				else:
					
					drdistribution.append(round(drmedian,3))
				
		else:
			break

	print "Best Solution",count,bestsolution		
	return(count,drdistribution,round(drmedian,3))
				



def writetofile(ofileloc,results):
	x = [a[1] for a in sorted(results,key=lambda x:x[0])]
	rows = zip(*x)
	ofile = open(ofileloc, 'w');
	writer = csv.writer(ofile,delimiter='\t',)
	for item in rows:
   		writer.writerow(item)
	ofile.close()

def main():
	#python randomflagizedSwapping-Parallel-SA.py TestSchedule.txt PairwiseSimilarity.tsv 2 5 0 randomflag_Results_SA_5.tsv > TestResults.txt
	print cpu_count()
	runs=int(sys.argv[3])
	iterations=int(sys.argv[4])
	randomflag=int(sys.argv[5])
	ofile=str(sys.argv[6])

	pool = Pool(processes=cpu_count())
	schedule = populateschedulefromfile()
	scorematrix = populatescorematrix()

	for i in range(runs):
		pool.apply_async(worker, args = (i,randomflag,schedule,scorematrix,iterations,), callback = log_results)
	pool.close()
	pool.join()
	writetofile(ofile,results)
	
if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	import random
	from random import choice
	from datetime import datetime
	from multiprocessing import Process, Pool, cpu_count
	import time
	import csv
	import math
	


	results=[]
	start_time = time.time()
	main()
	print time.time() - start_time, "seconds"
	