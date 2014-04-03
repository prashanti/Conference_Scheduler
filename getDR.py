


def populatescorematrix():
	scorematrix = []
	pairwisescores=str(sys.argv[1])
	scorefile=open(pairwisescores,'r')
	for line in scorefile:
		rowscores=[]
		scores=line.split("\t")
		for score in scores:
			rowscores.append(float(score.strip()))
		scorematrix.append(rowscores)
	return scorematrix

def calculateintrasimilarity(timeslot,intrasimlist,scorematrix):		
	for session in timeslot:
		for combo in itertools.combinations(session,2):
			doc1=combo[0]
			doc2=combo[1]
			intrasimlist.append(scorematrix[doc1-1][doc2-1])
	return(intrasimlist)


def calculateintersimilarity(timeslot,intersimlist,scorematrix):

	for i in range (0,len(timeslot)):
		for j in range (i+1,len(timeslot)):
			for p in range (0,len(timeslot[i])):
				for q in range(0, len(timeslot[j])):
					doc1=timeslot[i][p]
					doc2=timeslot[j][q]
					intersimlist.append(scorematrix[doc1-1][doc2-1])
	return(intersimlist)


def calculate(schedule,scorematrix):

	intersimlist=[]
	intrasimlist=[]
	for timeslot in schedule:
		intersimlist= calculateintersimilarity(timeslot,intersimlist,scorematrix)
		intrasimlist= calculateintrasimilarity(timeslot,intrasimlist,scorematrix)
	return(intrasimlist,intersimlist)


def main():
	infile=sys.argv[2]
	f=open(infile,'r')
	schedule=[]
	with open(infile) as f:
		schedule = json.load(f)
	scorematrix=populatescorematrix()
	intrasimlist,intersimlist= calculate(schedule,scorematrix)
	intramedian=numpy.median(intrasimlist)
	intermedian=numpy.median(intersimlist)
	intramean=numpy.mean(intrasimlist)
	intermean=numpy.mean(intersimlist)
	drmean=intramean/intermean
	drmedian=intramedian/intermedian
	print "Drmedian ",round(drmedian,3)
	print "Drmean ",round(drmean,3)
	


if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	from random import choice
	from datetime import datetime
	from multiprocessing import Process, Pool, cpu_count
	import time
	import itertools
	start_time = time.time()
	main()