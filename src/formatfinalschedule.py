def maptoabstractID():
	#CorpusID	AbstractID
	idmap={}
	mapping=open("../Evolution2014Data/AbstractID2CorpusID.tsv","r")
	for line in mapping:
		if "AbstractID" not in line:
			idmap[int(line.split("\t")[0].strip())]=int(line.split("\t")[1].strip())
	return(idmap)
def populatetopics():
	corpusID2topics={}
	topics=open("../Evolution2014Data/TopicWords_400.txt",'r')
	corpusID=1
	for line in topics:
		corpusID2topics[corpusID]=line.strip()
		corpusID+=1
	return corpusID2topics

def main():
	date={}
	starttime={}
	endtime={}
	abstractID2sessioncode={}
	roomfile=sys.argv[1]
	schedulefile=sys.argv[2]
	numberoftalkspersession = int(sys.argv[3])+1
	with open(schedulefile) as f:
		schedule = json.load(f)
	out=open("../Evolution2014Results/session_import.tsv",'w')
	abimport=open("../Evolution2014Results/abstract_import.tsv",'w')
	conc=open("../Evolution2014Results/ConcurrentSchedules.xls",'w')
	room=open(roomfile,'r')
	count=0
	idmap=maptoabstractID()
	
	abimport.write("SessionID"	+"\t"+"SessionName"	+"\t"+"Orderof"	+"\t"+"AbTitle"	+"\t"+"AbStartTime"	+"\t"+"AbEndTime"	+"\t"+"AbID"	+"\t"+  "Top Words from Topics"+ "\t"+    "ProgramID"	+"\t"+"First1"	+"\t"+"Last1"+ "\t"+"Email1"	+"\t"+"Org1"+"\n")
	for line in room:
		data=line.split("\r")
	for line in data:
		if "Date" not in line:
			newdata=line.split("\t")
			date[count]=newdata[0]
			times=newdata[1].split("-")
			starttime[count]=times[0]
			endtime[count]=times[1]
			
			start=newdata[1].split("-")[0]
			end=newdata[1].split("-")[1]
			starttime[count]=start
			endtime[count]=end
			count+=1

	alphalist=list(string.ascii_lowercase)
	header="Session Code	Session_Number	Session_name	Description	Session_type	Chair_definition	Chair_name	Session_date	Session_start_time	Session_end_time	Location	"
	for talks in range(1,numberoftalkspersession):
		header=header+"ID"+str(talks)+"\t"
	out.write(header+"\n")
	timeslotcount=1
	for timeslot in schedule:
		timeslotindex= schedule.index(timeslot)
		timeslotcode=alphalist[timeslotindex]
		timeslotdate=date[timeslotindex]
		timeslotstarttime=starttime[timeslotindex]
		timeslotendtime=endtime[timeslotindex]
		conc.write("Timeslot_"+str(timeslotcount)+"\t")
		timeslotcount+=1
		for session in timeslot:
			printdata="\t"+""+"\t"+""+"\t"+""+"\t"+""+"\t"+""+"\t"+""+"\t"+str(timeslotdate)+"\t"+str(timeslotstarttime)+"\t"+str(timeslotendtime)+"\t"+""+"\t"
			sessionindex=timeslot.index(session)
			sessioncode=alphalist[sessionindex]
			alphacode=""
			alphacode=timeslotcode+sessioncode
			printdata=alphacode+printdata
			conc.write(alphacode+"\t")

			for talk in session:
				abstractID2sessioncode[idmap[talk]]=alphacode
				printdata=printdata+str(idmap[talk])+"\t"


			out.write(printdata+"\n")
		conc.write("\n")
	


	corpusID2topics=populatetopics()
	abstracts=open("../Evolution2014Data/Abstracts_Evolution2014.txt",'r')
	special=open("../Evolution2014Data/SpecialSymposia_List.txt",'r')
	specialsymposia2sessioncode={}
	for line in special:
		data=line.split("\t")
		specialsymposia2sessioncode[data[1].strip()]=data[0].strip()
	abstract2corpus = {v:k for k, v in idmap.items()}

	for line in abstracts:
		if "Presentation Type" not in line:
			abstract=line.split("\t")
			abID=int(abstract[0].strip())
			if abID in abstractID2sessioncode:
				sessionID=abstractID2sessioncode[abID]
			else:
				sessionID="Special"
				if abstract[7] is '':
					sessionID="Not Provided"
				else:
					sessionID=specialsymposia2sessioncode[abstract[7].strip()]
			sessionname=" " 
			orderof=" "
			abtitle=abstract[2].strip()
			abstarttime=" "
			abendtime=" "
			programID=" "
			first1=abstract[25].strip()
			last1=abstract[26].strip()
			email1=abstract[28].strip()
			org1=abstract[30].strip()
			if abID in abstract2corpus:
				topics=corpusID2topics[abstract2corpus[abID]]
				#print abID,abstract2corpus[abID],topics
			abimport.write(sessionID+"\t"+sessionname+"\t"+orderof+"\t"+abtitle+"\t"+abstarttime	+"\t"+abendtime+"\t"+str(abID)+"\t" +topics+"\t"   +programID+"\t"+first1	+"\t"+last1+"\t"+email1+"\t"+org1+"\n")

if __name__ == "__main__":
	import json
	import sys
	import string
	main()
