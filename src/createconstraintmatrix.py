
def populateabstractIDs():
	abstractIDs=[]
	abstracts=open("../Evolution2014Data/AbstractIDlist.txt",'r')
	for line in abstracts:
		abstractIDs.append(int(line.strip()))
	return(abstractIDs)

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


	for session in sessioncodes:
		for i in abstractIDs:

			if i in awardabstracts: # this is an award abstract
				
				if (session in timeslot_sessions[15]) or (session in timeslot_sessions[14]) or (session in timeslot_sessions[13]) or (session in timeslot_sessions[12]): # session is not safe for award abstract, do nothing
					1

				else: # session is safe for award abstract
					if i in constraints:
						constraints[int(i)].append(session)
					else:
						constraints[int(i)]=[]
						constraints[int(i)].append(session)

			else: # this is not an awards abstract, can schedule it in all sessions
				
				if i in constraints:
					constraints[int(i)].append(session)
				else:
					constraints[int(i)]=[]
					constraints[int(i)].append(session)
					
	for abstract in constraints:
		print abstract,len(constraints[abstract])


	constraintsfile=open("../Evolution2014Data/ConstraintMatrix.txt",'w')
	json.dump(constraints,constraintsfile)
	constraintsfile.close()



if __name__ == "__main__":
	import sys
	import json
	from operator import itemgetter
	main()