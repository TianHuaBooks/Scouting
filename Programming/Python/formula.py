import numpy as num
import re
import types
import matplotlib.pyplot as plt

def parse(f):
	pat = r'((\-?\d*)x([\-\+]?\d+)?)'
	lists = re.findall(pat, f)
	return lists

def derivative(l):
	d = []
	for i in range(0, len(l)):
		new_list = list(l)
		new_list[i] = (l[i][1], l[i][1])
		d.append(new_list)
	return d

def calc_one(l, x):
	results = 1.0
	for e in l:
		tmp = 0.0
		if len(e) > 2:
			if e[1]:
				tmp += float(e[1]) * x
			else:
				tmp += x
			tmp += float(e[2])	
		elif e[1]:
			#print 'e[1]', e[1] 
			tmp += float(e[1])	
		else:
			tmp = 1.0
		results *= tmp
	return results

def calc(l, x):
	results = 0.0
	for e in l:
		if isinstance(e, types.ListType):
			results += calc_one(e, x)
		else:
			results += calc_one(l, x)
			break;
	return results
		
def plot(minX, maxX, step, f):
	l = parse(f)
	listX = []
	listY = []
	for x in num.arange(minX, maxX, step):
		listX.append(x)
		listY.append(calc(l,x))
	plt.plot(listX, listY)
	plt.grid(True)
	plt.show()
	
def plotD(minX, maxX, step, f):
	l = parse(f)
	d = derivative(l)
	listX = []
	listY = []
	listD = []
	for x in num.arange(minX, maxX, step):
		listX.append(x)
		listY.append(calc(l,x))
		listD.append(calc(d,x))
	#print listD
	plt.plot(listX, listY, 'r', listX, listD, 'g')
	plt.grid(True)
	plt.show()
