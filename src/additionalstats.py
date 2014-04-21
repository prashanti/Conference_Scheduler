 
def computesessionsessionsim(session,scorematrix):
	simmatrix=[]
	for i in range (0, len(session)):
		templist=[]
		for j in range(0, len(session)):
			doc1=session[i]
			doc2=session[j]
			templist.append(scorematrix[doc1-1][doc2-1])
		simmatrix.append(templist)
	return(simmatrix)



def compareintersim(session1,session2,scorematrix):
	intertemplist=[]
	for i in session1:
		for j in session2:
			intertemplist.append(scorematrix[i-1][j-1])
	average=numpy.mean(intertemplist)
	return(average)			




def computeaverageintersessionsim(schedule,scorematrix):
	newschedule=[]
	codes=[]
	out=open('../Evolution2014Results/AverageInterSessionSimilarity.txt','w')
	
	alphalist=list(string.ascii_lowercase)	
	for timeslot in schedule:
		timeslotindex=schedule.index(timeslot)
		timeslotcode=alphalist[timeslotindex]
		for session in timeslot:
			sessionindex=timeslot.index(session)
			sessioncode=alphalist[sessionindex]
			alphacode=timeslotcode+sessioncode
			codes.append(alphacode)
			newschedule.append(session)
	out.write("Session"+"\t")
	for code in codes:
		out.write(code+"\t")
	out.write("\n\n")				
	for i in range(0,len(newschedule)):
		out.write(codes[i]+"\t")
		for j in range(0,len(newschedule)):
			avgsim=compareintersim(newschedule[i],newschedule[j],scorematrix)
			out.write(str(avgsim)+"\t")
		out.write("\n")

def populatecorpusID2abstractIDmapping():
	inp=open("../Evolution2014Data/AbstractID2CorpusID.tsv",'r')
	abstractID2corpusID={}
	for line in inp:
		if "AbstractID" not in line:
			abstractID2corpusID[int(line.split("\t")[0].strip())]=int(line.split("\t")[1].strip())
	return abstractID2corpusID

def main():
	alphalist=list(string.ascii_lowercase)
	schedulefile=sys.argv[1]
	scorematrix=populatescorematrix()
	abstractID2corpusID=populatecorpusID2abstractIDmapping()
	with open(schedulefile) as f:
		schedule = json.load(f)
	computeaverageintersessionsim(schedule,scorematrix)
	for timeslot in schedule:
		timeslotindex=schedule.index(timeslot)
		timeslotcode=alphalist[timeslotindex]
		for session in timeslot:
			talkorder=[]
			for talk in session:
				talkorder.append(abstractID2corpusID[talk])
			
			sessionindex=timeslot.index(session)
			sessioncode=alphalist[sessionindex]
			alphacode=timeslotcode+sessioncode
			simmatrix=computesessionsessionsim(session,scorematrix)
			out=open("../Evolution2014Results/SessionSimilarity/Session_"+str(alphacode)+ "_Similarity.txt",'w')
			out.write("Abstract ID"+"\t")
			for talk in talkorder:
				out.write(str(talk)+"\t")
			out.write("\n")
			rowcount=0
			for row in simmatrix:
				out.write(str(talkorder[rowcount])+"\t")
				rowcount+=1
				for score in row:
					out.write(str(score)+"\t")
				out.write("\n")	



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

if __name__ == "__main__":
	import json
	import sys
	import string
	import numpy
	main()