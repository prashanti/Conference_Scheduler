def populateschedulefromfile():
	schedule=[]
	schedulefile=sys.argv[1]
	with open(schedulefile) as f:
		schedule = json.load(f)
	return(schedule)

def populatetestschedule():
	schedule=[]
	alldocs=range(1,9)
	alldocs1=range(1,9)
	session1=[[1,2],[3,4]]
	session2=[[5,6],[7,8]]
	schedule.append(session1)
	schedule.append(session2)

def roundoff(number):
	rounded=round(number,3)
	return rounded

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

def initializeschedule(timeslots):
	maxsession=[14,14,14,14,14,14,14,14,14,14,14,13,10,10,10,10]
	schedule=[]
	for time in xrange(0,timeslots):
		schedule.append([])
		for sess in xrange(0,maxsession[time]):
			schedule[time].append([])
	return(schedule)

def maptocorpusID():
	#CorpusID	AbstractID
	reverseidmap={}
	mapping=open("../Evolution2014Data/AbstractID2CorpusID.tsv","r")
	for line in mapping:
		if "AbstractID" not in line:
			reverseidmap[int(line.split("\t")[1].strip())]=int(line.split("\t")[0].strip())
	return(reverseidmap)

def maptoabstractID():
	#CorpusID	AbstractID
	idmap={}
	mapping=open("../Evolution2014Data/AbstractID2CorpusID.tsv","r")
	for line in mapping:
		if "AbstractID" not in line:
			idmap[int(line.split("\t")[0].strip())]=int(line.split("\t")[1].strip())
	return(idmap)

def populateabstractIDs():
	abstractIDs=[]
	abstracts=open("../Evolution2014Data/AbstractIDlist.txt",'r')
	for line in abstracts:
		abstractIDs.append(int(line.strip()))
	return(abstractIDs)

def randomizeschedule_variablesessions(timeslots,talkspersession,totalnumberoftalks,constraintmatrix):

	abstractIDs=populateabstractIDs()

	schedule=initializeschedule(timeslots)
	
	fullsessionlist=set()
	alphalist=list(string.ascii_lowercase)
	
	for abstract in sorted(constraintmatrix, key=lambda k: len(constraintmatrix[k])):
		availablesessions=constraintmatrix[abstract]
		randomsession=choice(availablesessions)
		while randomsession in fullsessionlist:
			randomsession=choice(availablesessions)	
	
		
		timeslotcode=alphalist.index(list(randomsession)[0])+1
		sessioncode=alphalist.index(list(randomsession)[1])+1
		schedule[timeslotcode-1][sessioncode-1].append(int(abstract))
		if len(schedule[timeslotcode-1][sessioncode-1])==talkspersession:
			fullsessionlist.add(randomsession)
	print "here"
	schedule=converttoCorpusID(schedule)
	return(schedule)

def converttoCorpusID(schedule):
	reverseidmap=maptocorpusID()
	for timeslot in schedule:
		for session in timeslot:
			for talk in session:
				CorpusID=reverseidmap[talk]
				schedule[schedule.index(timeslot)][timeslot.index(session)][session.index(talk)]=CorpusID
	return(schedule)

def sort(schedule):
	sortedschedule=[]
	for timeslot in schedule:
		sortedtimeslot=[]
		for session in timeslot:
			sortedtimeslot.append(sorted(session))
		sortedschedule.append(sortedtimeslot)
	return(sortedschedule)

def populateconstraints():
	with open("../Evolution2014Data/ConstraintMatrix.txt",'r') as constraints:
		for line in constraints:
			constraintmatrix = json.loads(line)
	constraints.close()
	return(constraintmatrix)




def log_results(result):
	results.append(result)


def worker(count,random,schedule,scorematrix,iterations,timeslots,talkspersession,totalnumberoftalks):
	constraintmatrix=populateconstraints()
	intrasimlist=[]
	intersimlist=[]
	drdistribution=[]
	idmap=maptoabstractID()
	print "Run",random
	if random == 1:
		schedule=randomizeschedule_variablesessions(timeslots,talkspersession,totalnumberoftalks,constraintmatrix)

	corpusID2sessioncode= mapcorpusID2sessioncode(schedule)	

	intersimlist,intrasimlist = calculate(schedule,scorematrix)

	intramean=numpy.mean(intrasimlist)
	intermean=numpy.mean(intersimlist)
	drmean= roundoff(intramean/intermean)	
	drdistribution.append(drmean)
	alldocs=range(1,1034)

	
	better=0
	while (better<iterations):

		
		tempschedule=copy.deepcopy(schedule)
		x=choice(alldocs)
		y=choice(alldocs)
		print x,y
	
		ss1=corpusID2sessioncode[int(x)]
		ss2=corpusID2sessioncode[int(y)]
		print "before",corpusID2sessioncode[int(x)],corpusID2sessioncode[int(y)]
		
		newsessionlist1=constraintmatrix[str(idmap[x])]
		newsessionlist2=constraintmatrix[str(idmap[y])]
		
		if ss1 in newsessionlist2 and ss2 in newsessionlist1:
		

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
				print "Yes"
				corpusID2sessioncode[int(x)]=ss2
				corpusID2sessioncode[int(y)]=ss1
				print "after",corpusID2sessioncode[int(x)],corpusID2sessioncode[int(y)]
				better+=1
				tempschedule[ytimeslotindex][ysessionindex][yindex],tempschedule[xtimeslotindex][xsessionindex][xindex] = tempschedule[xtimeslotindex][xsessionindex][xindex], tempschedule[ytimeslotindex][ysessionindex][yindex] 
				
				intersimlist,intrasimlist = calculate(tempschedule,scorematrix)

				intramean=numpy.mean(intrasimlist)
				intermean=numpy.mean(intersimlist)
				newdrmean=roundoff(intramean/intermean)
				if newdrmean > drmean:
					
					schedule=copy.deepcopy(tempschedule)
				
					drmean=newdrmean
					drdistribution.append(newdrmean)
				else:
				
					drdistribution.append(drmean)
	
	return(count,drdistribution,drmean,schedule)
				
def mapcorpusID2sessioncode(schedule):
	alphalist=list(string.ascii_lowercase)
	corpusID2sessioncode={}
	timeslotcount=1
	for timeslot in schedule:
		timeslotindex= schedule.index(timeslot)
		timeslotcode=alphalist[timeslotindex]
		for session in timeslot:
			sessionindex=timeslot.index(session)
			sessioncode=alphalist[sessionindex]
			alphacode=""
			alphacode=timeslotcode+sessioncode
			for talk in session:
				corpusID2sessioncode[talk]=alphacode.strip()

	return(corpusID2sessioncode)



def writetofile(ofileloc,results):
	x = [a[1] for a in sorted(results,key=lambda x:x[0])]
	rows = zip(*x)
	
	ofile = open(ofileloc, 'w');
	schedulefileloc="Schedule_"+ofileloc
	schedulefile=open(schedulefileloc,'w')
	writer = csv.writer(ofile,delimiter='\t',)
	for item in rows:
   		writer.writerow(item)
   	for i in range(0,len(results)):
   		resultstuple=results[i]
   		schedulefile.write(str(resultstuple[0])+"\t"+str(resultstuple[2])+"\t")
   		json.dump(resultstuple[3],schedulefile)
   		schedulefile.write("\n")
	ofile.close()
	schedulefile.close()


def main():
	
	print cpu_count()
	runs=int(sys.argv[3])
	iterations=int(sys.argv[4])
	random=int(sys.argv[5])
	ofile=str(sys.argv[6])
	timeslots=int(sys.argv[7])
	talkspersession=int(sys.argv[8])
	totalnumberoftalks=int(sys.argv[9])
	pool = Pool(processes=cpu_count())
	schedule = populateschedulefromfile()
	scorematrix = populatescorematrix()
	for i in range(runs):
		pool.apply_async(worker, args = (i,random,schedule,scorematrix,iterations,timeslots,talkspersession,totalnumberoftalks), callback = log_results)
	pool.close()
	pool.join()
	writetofile(ofile,results)
	
if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	from random import choice
	from datetime import datetime
	from multiprocessing import Process, Pool, cpu_count
	import time
	import csv
	import string


	results=[]
	start_time = time.time()
	main()
	print time.time() - start_time, "seconds"
	