
# Usage :
#python createCorpus.py Copy\ of\ abstracts.21March.AllFields\ \(4\).txt
# Save as tab delimited txt in Excel
#:%s/CtrlV CtrlM (4times)/ /g
#:%s/CtrlV CtrlM (2times)/ /g
#%s/\r/\r/g
def main():
	inputfile=sys.argv[1]
	out=open("/Users/pmanda/Documents/Python_NLP/Evolution2014Data/Evolution2014-Corpus.txt",'w')
	inp=open(inputfile,'r')
	abstract2corpus={}
	conversion=open("/Users/pmanda/Documents/Python_NLP/Evolution2014Data/AbstractID2CorpusID.tsv",'w')
	corpusID=1
	for line in inp:
		presentationtype=line.split("\t")[1]
		print line
		if presentationtype.strip() == "Contributed Presentation":

			abstractID=line.split("\t")[0].strip()
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









if __name__ == "__main__":
	import sys
	main()