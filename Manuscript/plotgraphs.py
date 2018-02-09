def parseif(datafile):
	min_max=[]
	x=[]
	for line in datafile:
		x.append(float(line.split("\t")[1]))
	endingerror=2*(np.std(x)/math.sqrt(len(x)))
	return np.mean(x),endingerror	

def plotbestschedules_ESA(figuredir):

	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/Hill/ESAGreedyResults_Hill.tsv',skiprows=0)

	greedy_hill=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	greedy_hill_error=[startingerror,endingerror]




	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/Hill/ESAILPResults_Hill.tsv',skiprows=0)
	ilp_hill=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	ilp_hill_error=[startingerror,endingerror]




	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/Hill/ESAResults_Hill_RandomSwapping.tsv',skiprows=0)
	
	random_hill=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	random_hill_error=[startingerror,endingerror]


	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/Hill/ESAResults_Hill_RealSwapping.tsv',skiprows=0)
	manual_hill=[np.min(x[0]),np.max(x[0]),np.min(x[len(x)-1]),np.max(x[len(x)-1])]
	manual_hill=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	manual_hill_error=[startingerror,endingerror]



	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/SA/ESAResults_SARealSwapping.txt',skiprows=0)
	manual_sa=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	manual_sa_error=[startingerror,endingerror]
	manualstarting=np.mean(x[0])

	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/SA/ESAResults_SARandomSwapping.txt',skiprows=0)
	random_sa=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	random_sa_error=[startingerror,endingerror]
	randomstarting=np.mean(x[0])
	randomstartingerror=startingerror

	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/SA/ESAILPResults_SA.txt',skiprows=0)
	ilp_sa=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	ilp_sa_error=[startingerror,endingerror]
	ilpstarting=np.mean(x[0])


	x=np.loadtxt('../ESA-TestData/ESAResults/FullDRDistributions/SA/ESAGreedyResults_SA.txt',skiprows=0)
	greedy_sa=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	greedy_sa_error=[startingerror,endingerror]
	greedystarting=np.mean(x[0])
	

	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-Hill/Schedule_ESAGreedyResults_HillIntraFirst.txt')
	endingmean,endingerror=parseif(datafile)
	greedy_hill_if=[greedystarting, endingmean]
	greedy_hill_if_error=[0,endingerror]


	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-Hill/Schedule_ESAILPResults_HillIntraFirst.txt')
	endingmean,endingerror=parseif(datafile)
	ilp_hill_if=[greedystarting, endingmean]
	ilp_hill_if_error=[0,endingerror]



	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-Hill/Schedule_ESAResults_HillIntraFirst_RandomSwapping.txt')
	
	endingmean,endingerror=parseif(datafile)
	random_hill_if=[randomstarting, endingmean]
	random_hill_if_error=[randomstartingerror,endingerror]

	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-Hill/Schedule_ESAResults_HillIntraFirst_RealSwapping.txt')
	endingmean,endingerror=parseif(datafile)
	manual_hill_if=[manualstarting, endingmean]
	manual_hill_if_error=[0,endingerror]

	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-SA/Schedule_ESAGreedyResults_SAIntraFirst.txt')
	endingmean,endingerror=parseif(datafile)
	greedy_sa_if=[greedystarting, endingmean]
	greedy_sa_if_error=[0,endingerror]



	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-SA/Schedule_ESAILPResults_SAIntraFirst.txt')
	endingmean,endingerror=parseif(datafile)
	ilp_sa_if=[ilpstarting, endingmean]
	ilp_sa_if_error=[0,endingerror]
	print(endingerror)


	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-SA/Schedule_ESAResults_SAIntraFirst_RealSwapping.txt')
	endingmean,endingerror=parseif(datafile)
	manual_sa_if=[manualstarting, endingmean]
	manual_sa_if_error=[0,endingerror]

	datafile=open('../ESA-TestData/ESAResults/AllSchedules/IF-SA/Schedule_ESAResults_SAIntraFirstRandomSwapping.txt')
	endingmean,endingerror=parseif(datafile)
	random_sa_if=[randomstarting, endingmean]
	random_sa_if_error=[randomstartingerror,endingerror]


	# 

	mean_y_hill=[random_hill[1],manual_hill[1],greedy_hill[1],ilp_hill[1]]
	mean_y_sa=[random_sa[1],manual_sa[1],greedy_sa[1],ilp_sa[1]]
	mean_y_if_hill=[random_hill_if[1],manual_hill_if[1],greedy_hill_if[1],ilp_hill_if[1]]
	mean_y_if_sa=[random_sa_if[1],manual_sa_if[1],greedy_sa_if[1],ilp_sa_if[1]]
	
	error_meany_hill=[random_hill_error[1],manual_hill_error[1], greedy_hill_error[1],ilp_hill_error[1]]
	error_meany_sa=[random_sa_error[1],manual_sa_error[1], greedy_sa_error[1],ilp_sa_error[1]]
	error_meany_if_hill=[random_hill_if_error[1],manual_hill_if_error[1], greedy_hill_if_error[1],ilp_hill_if_error[1]]
	error_meany_if_sa=[random_sa_if_error[1],manual_sa_if_error[1], greedy_sa_if_error[1],ilp_sa_if_error[1]]
	
	error_starting_hill=[randomstartingerror,0,0,0]
	error_starting=[randomstartingerror,0,0,0]
	error_starting_if_hill=[randomstartingerror,0,0,0]
	error_starting_if_sa=[randomstartingerror,0,0,0]



	starting=[0.99,3.105,4.154,5.068]
	xlabels=['Random','Manual','Greedy','ILP']
	x=[1,2,3,4]
	lines=[]
	legendlabels=[]
	fig, ax = plt.subplots()
	

	lines.append(plt.scatter(x,starting,color='blue',s=20))
	(_, caps, _)=ax.errorbar(x,starting,yerr=error_starting,ls='none',color='blue',capsize=4)
	legendlabels.append('Starting schedules')

	lines.append(plt.scatter(x,mean_y_hill,color='orange',s=20))
	(_, caps, _)=ax.errorbar(x,mean_y_hill,yerr=error_meany_hill,ls='none',color='orange',capsize=4)
	legendlabels.append(r'$HC_A$')

	lines.append(plt.scatter(x,mean_y_sa,color='green',s=20))
	(_, caps, _)=ax.errorbar(x,mean_y_sa,yerr=error_meany_sa,ls='none',color='green',capsize=4)
	legendlabels.append(r'$SA_A$')

	lines.append(plt.scatter(x,mean_y_if_hill,color='red',s=20))
	(_, caps, _)=ax.errorbar(x,mean_y_if_hill,yerr=error_meany_if_hill,ls='none',color='red',capsize=4)
	legendlabels.append(r'$HC_B$')


	lines.append(plt.scatter(x,mean_y_if_sa,color='purple',s=20))
	(_, caps, _)=ax.errorbar(x,mean_y_if_sa,yerr=error_meany_if_hill,ls='none',color='purple',capsize=4)
	legendlabels.append(r'$SA_B$')


	ax.set_xticks(x, minor=False)
	ax.set_xticklabels(xlabels)
	plt.legend(lines,legendlabels,loc='lower right', frameon=False, prop={'size': 12},numpoints=1,scatterpoints=1)
	
	ax.set_xlabel('Schedule creation algorithm')
	ax.set_ylabel('Mean discrimination ratio')
	plt.savefig(figuredir+"ESA-Comparison.eps",dpi=1200)



def plotbestschedules_Evolution(figuredir):


	x=np.loadtxt('../Evolution2014FINAL/FinalResults/Hill/Results_Hill.tsv',skiprows=0)
	random_hill=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	random_hill_error=[startingerror,endingerror]


	x=np.loadtxt('../Evolution2014FINAL/FinalResults/HillConstraints/Results_HillConstraints.tsv',skiprows=0)
	random_hill_constraints=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	random_hill_constraints_error=[startingerror,endingerror]


	x=np.loadtxt('../Evolution2014FINAL/FinalResults/SA/Results_SA.txt',skiprows=0)
	random_sa=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	random_sa_error=[startingerror,endingerror]

	
	x=np.loadtxt('../Evolution2014FINAL/FinalResults/SAConstraints/Results_SAConstraints.tsv',skiprows=0)

	random_sa_constraints=[np.mean(x[0]),np.mean(x[len(x)-1])]
	startingmean=np.mean(x[0])

	startingerror=2*(np.std(x[0])/math.sqrt(len(x[0])))
	endingerror=2*(np.std(x[len(x)-1])/math.sqrt(len(x[len(x)-1])))
	random_sa_constraints_error=[startingerror,endingerror]



	datafile=open('../Evolution2014FINAL/FinalResults/HillIntraFirst/Schedule_Results_HillIntraFirst.tsv')
	endingmean,endingerror=parseif(datafile)
	random_hill_if=[startingmean,endingmean]
	random_hill_if_error=[startingerror,endingerror]

	

	datafile=open('../Evolution2014FINAL/FinalResults/HillIntraFirstConstraints/Schedule_Results_HillIntraFirstConstraints.txt')
	endingmean,endingerror=parseif(datafile)
	random_hill_if_constraints=[startingmean,endingmean]
	random_hill_if_constraints_error=[startingerror,endingerror]


	datafile=open('../Evolution2014FINAL/FinalResults/SAIntraFirst/Schedule_Results_SAIntraFirst-7mil.txt')
	endingmean,endingerror=parseif(datafile)
	random_sa_if=[startingmean,endingmean]
	random_sa_if_error=[startingerror,endingerror]

	datafile=open('../Evolution2014FINAL/FinalResults/SAIntraFirstConstraints/Schedule_Results_SAIntraFirstConstraints-7mil.txt')
	endingmean,endingerror=parseif(datafile)
	random_sa_if_constraints=[startingmean,endingmean]
	random_sa_if_constraints_error=[startingerror,endingerror]



	xlabels=['Random', 'Random with Constraints']


	mean_hc=[random_hill[1],random_hill_constraints[1]]
	mean_sa=[random_sa[1],random_sa_constraints[1]]
	

	mean_if_hill=[random_hill_if[1],random_hill_if_constraints[1]]

	mean_if_sa=[random_sa_if[1],random_sa_if_constraints[1]]

	
	error_hill=[random_hill_error[1],random_hill_constraints_error[1]]
	error_sa=[random_sa_error[1],random_sa_constraints_error[1]]
	
	error_if_hill=[random_hill_if_error[1], random_hill_if_constraints_error[1]]
	error_if_sa=[random_sa_if_error[1], random_sa_if_constraints_error[1]]



	starting=[random_hill[0],random_hill_constraints[0]]

	error_starting_hill=[random_hill_error[0],random_hill_constraints_error[0]]
	error_starting_sa=[random_sa_error[0],random_sa_constraints_error[0]]
	error_starting_if_hill=[random_hill_if_error[0],random_hill_if_constraints_error[0]]
	error_starting_if_sa=[random_sa_if_error[0],random_sa_if_constraints_error[0]]

	
	x=[1,2]
	lines=[]
	legendlabels=[]
	fig, ax = plt.subplots()
	

	lines.append(plt.scatter(x,starting,color='blue',s=20))
	(_, caps, _)=ax.errorbar(x,starting,yerr=error_starting_sa,ls='none',color='blue',capsize=4)
	legendlabels.append('Starting schedules')


	lines.append(plt.scatter(x,mean_hc,color='orange',s=20))
	(_, caps, _)=ax.errorbar(x,mean_hc,yerr=error_hill,ls='none',color='orange',capsize=4)
	legendlabels.append('HC_A')

	lines.append(plt.scatter(x,mean_sa,color='green',s=20))
	(_, caps, _)=ax.errorbar(x,mean_sa,yerr=error_sa,ls='none',color='green',capsize=4)
	legendlabels.append('SA_A')

	lines.append(plt.scatter(x,mean_if_hill,color='red',s=20))
	(_, caps, _)=ax.errorbar(x,mean_if_hill,yerr=error_if_hill,ls='none',color='red',capsize=4)
	legendlabels.append('HC_B')

	lines.append(plt.scatter(x,mean_if_sa,color='purple',s=20))
	(_, caps, _)=ax.errorbar(x,mean_if_sa,yerr=error_if_sa,ls='none',color='purple',capsize=4)
	legendlabels.append('SA_B')


	ax.set_xticks(x, minor=False)
	ax.set_xticklabels(xlabels)
	plt.legend(lines,legendlabels,loc='upper center', frameon=False, prop={'size': 12},numpoints=1,scatterpoints=1)
	ax.set_xlabel('Schedule creation algorithm')
	ax.set_ylabel('Mean discrimination ratio')
	plt.savefig(figuredir+"Evolution-Comparison.eps",dpi=1200)



def main():
	figuredir="../Manuscript/Figures/"
	plotbestschedules_ESA(figuredir)
	plotbestschedules_Evolution(figuredir)

if __name__ == "__main__":
	import matplotlib
	matplotlib.rcParams.update({'font.size': 18})
	import matplotlib.pyplot as plt
	import sys
	import pandas
	import numpy as np
	import math
	main()