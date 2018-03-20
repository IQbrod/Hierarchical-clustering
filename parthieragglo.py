#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Group():
	def __init__(self,col,sim,ind):
		self.elem = col
		self.sim = sim
		self.ind = ind

	def __str__(self):
		return str(self.elem)+" => "+str(self.sim)+" ("+str(self.ind)+")"

class Node():
''' Inspired by : https://stackoverflow.com/questions/1894846/printing-bfs-binary-tree-in-level-order-with-specific-formatting'''
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __print__(self):
		curLevel = [self]
		while curLevel: #will break on leaves (=None)
			nextLevel = []
			for elem in curLevel:
				''' ADD PADDING BETWEEN ELEMENTS '''
				print elem.val+" " #Display element
				if elem.left:
					nextLevel.append(elem.left)
				if elem.right:
					nextLevel.append(elem.right)
			print
			curLevel = nextLevel

### MAIN ###
repMatrix = [[10 ,  6 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0],
			[6 ,  10 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0],
			[0 ,  0 ,  10 ,  5 ,  3 ,  3 ,  1 ,  1 ,  0],
			[0 ,  0 ,  5 ,  10 ,  1 ,  2 ,  1 ,  1 ,  0],
			[0 ,  0 ,  3 ,  1 ,  10 ,  4 ,  1 ,  2 ,  0],
			[0 ,  0 ,  3 ,  2 ,  4 ,  10 ,  1 ,  4 ,  0],
			[0 ,  0 ,  1 ,  1 ,  1 ,  1 ,  10 ,  1 ,  0],
			[0 ,  0 ,  1 ,  1 ,  2 ,  4 ,  1 ,  10 ,  0],
			[0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  10]]

# -- Display File as Matrix
print "Representation Matrix:"
for i in range(0,len(repMatrix)):
	print repMatrix[i]
print
	
# -- Initialization
'''Remove Self Similarity'''
worMatrix = repMatrix
for i in range(len(repMatrix)):
	worMatrix[i][i] = -1
'''Creation of differents clusters'''
groups = []
for i in range(len(repMatrix)):
	g = Group([i],max(worMatrix[i]),worMatrix[i].index(max(worMatrix[i])))
	groups.append(g)	
	#print g

for i in range(len(repMatrix)-1): #N-1 Merge
	## Get the max similarity => LIEN UNIQUE
	mx = -1
	index = [-1,-1]
	for j,gr in zip(range(len(groups)),groups):
		if mx < gr.sim: #Maximum Similarity
			mx = gr.sim
			index = [j,gr.ind]
	'''print "Found max: "+str(mx)+" @"+str(index)'''

	# Calculing group index
	gindex = [index[0],-1]
	for j in range(len(groups)):
		if index[1] in groups[j].elem:
			gindex[1] = j
	## Merging the two clusters
	dest = groups[gindex[0]] #TO UPGRADE
	source = groups[gindex[1]] #TO REMOVE
	# Update worMatrix
	for el in source.elem:
		for el2 in dest.elem:
			worMatrix[el][el2] = -1
			worMatrix[el2][el] = -1
	# Merge Elements
	disp = dest.elem
	dest.elem = dest.elem+source.elem
	groups.remove(source)
	# Update clusters'sim
	for g in groups:
		if (g.ind in source.elem):	
			g.ind = index[0]

	# Calculing max	
	mx = -1
	indx = -1
	for e in dest.elem:
		for i in range(len(worMatrix)):
			if worMatrix[e][i] > mx: #Found new max for cluster
				mx = worMatrix[e][i]
				indx = i
	dest.ind = indx
	dest.sim = mx
	print "Merged "+str(gindex)+":  "+str(disp)+" & "+str(source.elem)
	#print dest
