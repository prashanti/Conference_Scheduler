
# Usage :
#python createCorpus.py Copy\ of\ abstracts.21March.AllFields\ \(4\).txt
# Save as tab delimited txt in Excel
#:%s/CtrlV CtrlM (4times)/ /g
#:%s/CtrlV CtrlM (2times)/ /g
#%s/\r/\r/g
def main():
	inputfile=sys.argv[1]
	out=open("/Users/pmanda/Documents/Python_NLP/Evolution2014Data/Evolution2014-Corpus.txt",'w')
	awardfile=open("/Users/pmanda/Documents/Python_NLP/Evolution2014Data/Abstracts_awards.txt",'w')
	abstractIDfile=open("/Users/pmanda/Documents/Python_NLP/Evolution2014Data/AbstractIDlist.txt",'w')
	inp=open(inputfile,'r')
	abstract2corpus={}
	conversion=open("/Users/pmanda/Documents/Python_NLP/Evolution2014Data/AbstractID2CorpusID.tsv",'w')
	corpusID=1
	for line in inp:
		presentationtype=line.split("\t")[1]
		award=line.split("\t")[5].strip()
		abstractID=line.split("\t")[0].strip()
		if "considered" in award:
			awardfile.write(abstractID+"\n")

		if presentationtype.strip() == "Contributed Presentation":

			abstractIDfile.write(abstractID+"\n")
			abstract2corpus[corpusID]=int(abstractID)
			corpusID+=1
			title=line.split("\t")[2].strip()
			abstract=line.split("\t")[3].strip()
			title=title.replace("\n","")
			abstract=abstract.replace("\n","")
			abstract=abstract.replace("\r","")
			data=title+" "+abstract
			out.write(data+"\n")

	conversion.write("CorpusID\tAbstractID" + "\n"  )
	for corpusID in abstract2corpus:
		conversion.write(str(corpusID)+"\t"+str(abstract2corpus[corpusID])+"\n")
	awardfile.close()









if __name__ == "__main__":
	import sys
	main()