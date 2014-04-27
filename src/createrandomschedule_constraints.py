
def populateconstraints():
	with open("../Evolution2014Data/ConstraintMatrix.txt",'r') as constraints:
		for line in constraints:
			constraintmatrix = json.loads(line)
	constraints.close()
	return(constraintmatrix)

def populateabstractIDs():
	abstractIDs=[]
	abstracts=open("../Evolution2014Data/AbstractIDlist.txt",'r')
	for line in abstracts:
		abstractIDs.append(int(line.strip()))
	return(abstractIDs)




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
	idmap={}
	mapping=open("../Evolution2014Data/AbstractID2CorpusID.tsv","r")
	for line in mapping:
		if "AbstractID" not in line:
			idmap[int(line.split("\t")[1].strip())]=int(line.split("\t")[0].strip())
	return(idmap)

def randomizeschedule_variablesessions(timeslots,talkspersession,totalnumberoftalks):
	abstractIDs=populateabstractIDs()
	
	constraintmatrix=populateconstraints()
	print "constraints",len(constraintmatrix)
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
	
	print "timeslots",len(schedule)
	i=1
	for timeslots in schedule:
		print "timeslot",i,len(timeslots)
		sess=1
		for session in timeslots:
			if len(session) <5:
				print "session",sess,len(session)
			sess+=1
		i+=1

	schedule=converttoCorpusID(schedule)
	return(schedule)
def converttoCorpusID(schedule):
	idmap=maptocorpusID()
	for timeslot in schedule:
		for session in timeslot:
			for talk in session:
				CorpusID=idmap[talk]
				schedule[schedule.index(timeslot)][timeslot.index(session)][session.index(talk)]=CorpusID
	return(schedule)
def main():
	timeslots=int(sys.argv[1])
	talkspersession=int(sys.argv[2])
	totalnumberoftalks=int(sys.argv[3])
	outfile="../Evolution2014Data/RandomSchedule_Constraints_"+str(timeslots)+"_"+str(talkspersession)+".txt"
	print outfile
	out=open(outfile,'w')
	randomschedule=randomizeschedule_variablesessions(timeslots,talkspersession,totalnumberoftalks)

	json.dump(randomschedule,out)


if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	import math
	import string
	from random import choice
	main()
