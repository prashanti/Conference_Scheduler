def randomizeschedulewithparameters(timeslots,sessions,talkspersession,totalnumberoftalks):
	if sessions==0:
		schedule=randomizeschedule_variablesessions(timeslots,talkspersession,totalnumberoftalks)
		return schedule
	else:
		alldocs1=range(1,totalnumberoftalks+1)

		newschedule=[]
		for timeslot in range(1,timeslots+1):
			newtimeslot=[]
			for session in range(1,sessions+1):
				newsession=[]
				if len(alldocs1)<talkspersession:
					talkspersession=len(alldocs1)
				for talknumber in range(1,talkspersession+1):
					random=choice(alldocs1)
					alldocs1=filter(lambda a: a != random, alldocs1)
					newsession.append(random)
				newtimeslot.append(newsession)
			newschedule.append(newtimeslot)
		return(newschedule)	


def createrandomsession(talkspersession,alldocs1):
	newsession=[]
	for talknumber in range(1,talkspersession+1):
		random=choice(alldocs1)
		alldocs1=filter(lambda a: a != random, alldocs1)
		newsession.append(random)
	return(newsession,alldocs1)

def randomizeschedule_variablesessions(timeslots,talkspersession,totalnumberoftalks):
	maxsession=[14,14,14,14,14,14,14,14,14,14,14,14,10,10,10,10]
	alldocs1=range(1,totalnumberoftalks+1)

	schedule=[]
	
	for i in range(0,timeslots):
		timeslot=[]
		newsession,alldocs1=createrandomsession(talkspersession,alldocs1)
		timeslot.append(newsession)
		schedule.append(timeslot)
	#initial structure of schedule made with timeslots with one session each

	#populate one session per timeslot till we run out
	while (len(alldocs1)>0):
		
		for i in range(0,timeslots):
			if len(alldocs1)<talkspersession:
				talkspersession=len(alldocs1)
			if len(alldocs1)>0:	
				if ((len(schedule[i])<maxsession[i])):
					newsession,alldocs1=createrandomsession(talkspersession,alldocs1)
					schedule[i].append(newsession)
			else:
				break
	sum=0			
	for timeslot in schedule:
		print len(timeslot)
		for session in timeslot:
			print len(session)
		print "\n\n"
	print sum		
	return(schedule)
def main():
	
	timeslots=int(sys.argv[1])
	sessions=int(sys.argv[2])
	talkspersession=int(sys.argv[3])
	totalnumberoftalks=int(sys.argv[4])
	outfile="RandomSchedule_"+str(timeslots)+"_"+str(sessions)+"_"+str(talkspersession)+".txt"
	print outfile
	out=open(outfile,'w')
	randomschedule=randomizeschedulewithparameters(timeslots,sessions,talkspersession,totalnumberoftalks)
	json.dump(randomschedule,out)


if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	import math
	from random import choice
	main()
