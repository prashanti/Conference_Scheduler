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



	constraints=[]
	temp_dict={}
	i=0
	
	# Ernst Mayr award constraint - cannot be in last day
	while (i<1548):
		temp_dict={}
		for session in sessioncodes:
			if i in awardabstracts:
				if (session in timeslot_sessions[15]) or (session in timeslot_sessions[14]) or (session in timeslot_sessions[13]) or (session in timeslot_sessions[12]):
					temp_dict[session]=0

				else:
					temp_dict[session]=1
			else:
				temp_dict[session]=1
		constraints.append(temp_dict)
		i+=1
	constraintsfile=open("../Evolution2014Data/ConstraintMatrix.txt",'w')
	print constraints
	json.dump(constraints,constraintsfile)
	constraintsfile.close()



if __name__ == "__main__":
	import sys
	import json
	main()