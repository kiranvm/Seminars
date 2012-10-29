#!/usr/bin/env python

import random

with open ("test","r") as inf:
	data= inf.read()
	inf.close()

data= data.replace('\n',' ')
data= data.replace('\t','')
data=data.split()

def chooser ():
	num= random.randint(1,len(data))
	print data[num]

def loop():
	while(True):
		res=raw_input("Want to select a random person??")
		
		if res==('n') :
			exit()
		
		chooser ()

loop ()



