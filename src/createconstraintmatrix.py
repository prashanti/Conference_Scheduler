
def populateabstractIDs():
	abstractIDs=[]
	abstracts=open("../Evolution2014Data/AbstractIDlist.txt",'r')
	for line in abstracts:
		abstractIDs.append(int(line.strip()))
	return(abstractIDs)

def addtoconstraints(i,constraints,session):
	if i in constraints:
		constraints[int(i)].add(session)
	else:
		constraints[int(i)]=set()
		constraints[int(i)].add(session)
	return constraints

def printconstraintlength(constraintmatrix):
	lengthout=open("../Evolution2014Data/ConstraintList.txt",'w')
	for abstract in sorted(constraintmatrix, key=lambda k: len(constraintmatrix[k])):
		lengthout.write("abstractID"+"\t"+str(abstract)+"\t"+str(len(constraintmatrix[abstract]))+"\n")
	lengthout.close()

def main():
	awardfile=sys.argv[1]
	award=open(awardfile,'r')
	abstractIDs=populateabstractIDs()
	awardabstracts=[]
	sessioncodes=[]
	for line in award:
		awardabstracts.append(int(line.strip()))
	award.close()

	sessions=open("../Evolution2014Results/ConcurrentSessions.tsv",'r')
	timeslot_sessions=[]
	for line in sessions:
		temp=[]
		sessionlist=line.split("\t")
		for session in sessionlist:
			if "Time" not in session and session.strip() is not '':
				sessioncodes.append(session.strip())
				temp.append(session.strip())
		timeslot_sessions.append(temp)
	sessions.close()


	constraints={}
	temp_list=[]
	i=1
	
	# Ernst Mayr award constraint - cannot be in last day
	# Timeslots go from 0 to 15
	# in the below mention where you can't put them
	for session in sessioncodes:
		for i in abstractIDs:
			if i == 347:
				
				if (session not in timeslot_sessions[10]) and (session not in timeslot_sessions[11]) and (session not in timeslot_sessions[12]) and (session not in timeslot_sessions[13]) and (session not in timeslot_sessions[14]) and (session not in timeslot_sessions[15]):
						constraints=addtoconstraints(i,constraints,session)
			elif i == 768:
				
				if (session not in timeslot_sessions[14]) and (session not in timeslot_sessions[15]):
					constraints=addtoconstraints(i,constraints,session)


			elif i == 837:
				
				if (session not in timeslot_sessions[0]) and (session not in timeslot_sessions[1]) and (session not in timeslot_sessions[2]) and (session not in timeslot_sessions[3]) and (session not in timeslot_sessions[4]) and (session not in timeslot_sessions[5]) and (session not in timeslot_sessions[6]) and (session not in timeslot_sessions[7]) : 
						constraints=addtoconstraints(i,constraints,session)	

			elif i == 1361:
				
				if (session not in timeslot_sessions[12]) and (session not in timeslot_sessions[13]) and (session not in timeslot_sessions[14]) and (session not in timeslot_sessions[15]): 
						constraints=addtoconstraints(i,constraints,session)												
			elif i == 349:
				
				if (session not in timeslot_sessions[12]) and (session not in timeslot_sessions[13]) and (session not in timeslot_sessions[14]) and (session not in timeslot_sessions[15]): 
						constraints=addtoconstraints(i,constraints,session)

			elif i == 776:
				
				if (session not in timeslot_sessions[8]) and (session not in timeslot_sessions[9]) and (session not in timeslot_sessions[10]) and (session not in timeslot_sessions[11]) and (session not in timeslot_sessions[12]) and (session not in timeslot_sessions[13]) and (session not in timeslot_sessions[14]) and (session not in timeslot_sessions[15]): 
						#print "session",session
						constraints=addtoconstraints(i,constraints,session)

			elif i in awardabstracts: # this is an award abstract	
				if (session not in timeslot_sessions[15]) and (session not in timeslot_sessions[14]): 
					constraints=addtoconstraints(i,constraints,session)

			else: #these abstracts have no constraints

				constraints=addtoconstraints(i,constraints,session)
					
	


	constraintsfile=open("../Evolution2014Data/ConstraintMatrix.txt",'w')
	for x in constraints:
		constraints[x]=list(constraints[x])
		constraints[x].sort()
	json.dump(constraints,constraintsfile)

	printconstraintlength(constraints)

	

	constraintsfile.close()



if __name__ == "__main__":
	import sys
	import json
	from json import dumps, loads, JSONEncoder, JSONDecoder
	from operator import itemgetter
	main()