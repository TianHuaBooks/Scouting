import numpy as np
from operator import itemgetter

#Import firstname and lastname lists
lastnames = [ line.strip() for line in open('lastnames.txt') ]
firstnames = [ line.strip() for line in open('names.txt') ]

#Get a first name
def getFirstName(i):
	if (i < len(firstnames)):
		return firstnames[i]
	else:
		return firstnames[np.random.randint(len(firstnames))]
		
#Get a last name
def getLastName(i):
	if (i < len(lastnames)):
		return lastnames[i]
	else:
		return lastnames[np.random.randint(len(lastnames))]
		
#Create n number of students with scores
def create(n):
	list = []
	for i in range(n):
		firstname = getFirstName(i)
		lastname = getLastName(i)
		english = np.random.randint(70,100)
		math = np.random.randint(40,100)
		science = np.random.randint(60,100)
		total = english + math + science
		list.append((firstname, lastname, english, math, science, total))
	slist = sorted(list, key=itemgetter(5), reverse=True)
	return slist
		

