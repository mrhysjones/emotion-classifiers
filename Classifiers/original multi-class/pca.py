# Python script to perform principle component analysis on the face distance measures


import random, os
import numpy as np
from matplotlib.mlab import PCA

data = []
for line in open("emotions.train"):
	data.append([])
	for el in line[2:].strip().split(" "):
		data[-1].append(float(el[el.index(":")+1:]))
	if len(data[-1]) != 86: data.remove(data[-1])

results = PCA(np.array(data))
	
archive = open("pca_archive_wt.txt", "w")
for v in results.Wt: archive.write(",".join([str(float(x)) for x in v]) + "\n")
archive.close()

archive = open("pca_archive_mu.txt", "w")
archive.write(",".join([str(float(x)) for x in results.mu]) + "\n")
archive.close()

archive = open("pca_archive_sigma.txt", "w")
archive.write(",".join([str(float(x)) for x in results.sigma]) + "\n")
archive.close()

fout = open("emotions.train.pca", "w")
for line in open("emotions.train"):
	temp = []
	for el in line[2:].strip().split(" "):
		temp.append(float(el[el.index(":")+1:]))
	fout.write(line[:2] + " ".join([str(str(i+1) + ":" + str(index)) for i, index in enumerate(results.project(np.array(temp), 0.001))]) + "\n") 
fout.close()