def main():
	awardfile=sys.argv[1]
	award=open(awardfile,'r')
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
		
		i=1
		while (i<=1548):
			if i in awardabstracts: # this is an award abstract
				if (session in timeslot_sessions[15]) or (session in timeslot_sessions[14]) or (session in timeslot_sessions[13]) or (session in timeslot_sessions[12]): # session is not safe for award abstract, do nothing
					1

				else: # session is safe for award abstract
					if session in constraints:
						constraints[session].append(i)
					else:
						constraints[session]=[]
						constraints[session].append(i)

			else: # this is not an awards abstract, can schedule it in all sessions
				if session in constraints:
					constraints[session].append(i)
				else:
					constraints[session]=[]
					constraints[session].append(i)
			i+=1
		print session,len(constraints[session])			



	constraintsfile=open("../Evolution2014Data/ConstraintMatrix.txt",'w')
	json.dump(constraints,constraintsfile)
	constraintsfile.close()



if __name__ == "__main__":
	import sys
	import json
	main()