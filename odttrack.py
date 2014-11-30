#Aditya Ponukumati
#Word Tracker
#November 26, 2014


#Tracks most commonly used words in .txt (for now) files


import os

d = {}

def partition(f):
	fopen = open(f, "r")
	while True:
		word = fopen.readline()
		ind = word.strip().split(" ")
		if not word:
			break
		imp(ind)
	fopen.close()

def cleanse(s):
	s = s.translate(None, '~()[]{}~!?,.;:')
	s = s.replace("\xe2\x80\x9d", "")
	s = s.replace("\xe2\x80\x98", "")
	s = s.replace("\xe2\x80\x9c", "")
	s = s.replace("\xe2\x80\x99", "")
	return s.lower()

def imp(words):
	for X in words:
		X = cleanse(X)
		if X not in d.keys():
			d[X] = 1
		else:
			d[X] += 1

def scan(f):
	if f.endswith(".txt"):
		partition(f)
	elif f.endswith(".odt"):
		temp = "completelyrandomfilepleasedonthaveme.txt"
		os.system("unoconv -ftxt -o" + temp + " " + f)
		partition(temp)
		os.system("rm " + temp)
	else:
		return

lfile = os.listdir("./")

print lfile

for X in lfile:
	print X
	scan(X)

q = sorted(d.items(), key=lambda x: x[1]) #http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

for Z in reversed(q):
	print Z

print "Program end"
