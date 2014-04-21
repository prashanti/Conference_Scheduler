
def main():
	schedulefile=sys.argv[1]
	schedules=open(schedulefile,'r')
	bestdr=0
	bestschedule=[]
	for line in schedules:
		line=line.split("\t")
		currentdr=float(line[1])
		if currentdr>bestdr:
			bestdr=currentdr
			bestschedule=line[2]
	print bestdr,bestschedule

if __name__ == "__main__":
	import sys
	import numpy
	import copy
	import json
	from random import choice
	from datetime import datetime
	from multiprocessing import Process, Pool, cpu_count
	import time
	import csv
	main()


