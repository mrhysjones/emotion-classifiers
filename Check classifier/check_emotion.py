import os, sys
import numpy as np

def distance_between(n1, n2):
	return (abs(n1[0] - n2[0])**2 + abs(n1[1] - n2[1])**2)**0.5

def point_between(n1, n2):
	x = [n1[0], n2[0]]
	y = [n1[1], n2[1]]
	return (abs(x[0] - x[1])/2 + min(x), abs(y[0] - y[1])/2 + min(y))

# Facial landmarks to the normalised distance measures used by classifier
def v2test(vertex):
	container = []
	vertex = [0.0] + vertex

	left_eye 		= point_between(vertex[37], vertex[40])
	right_eye 		= point_between(vertex[43], vertex[46])
	between_eyes 	= distance_between(left_eye, right_eye)
	nose 			= point_between(vertex[31], vertex[34])

	for x in range(1, 17 + 1):  container.append(distance_between(vertex[x], nose) / between_eyes)
	for x in range(18, 22 + 1): container.append(distance_between(vertex[x], left_eye) / between_eyes)
	for x in range(23, 27 + 1): container.append(distance_between(vertex[x], right_eye) / between_eyes)
	for x in range(28, 31 + 1):	container.append(distance_between(vertex[x], nose) / between_eyes)
	for x in range(32, 36 + 1):	container.append(distance_between(vertex[x], right_eye) / between_eyes)
	for x in range(37, 42 + 1):	container.append(distance_between(vertex[x], left_eye) / between_eyes)
	for x in range(43, 48 + 1):	container.append(distance_between(vertex[x], right_eye) / between_eyes)
	for x in range(49, 66 + 1):	container.append(distance_between(vertex[x], nose) / between_eyes)

	container.append(distance_between(vertex[53], vertex[57]) / between_eyes)
	container.append(distance_between(vertex[52], vertex[58]) / between_eyes)
	container.append(distance_between(vertex[51], vertex[59]) / between_eyes)
	container.append(distance_between(vertex[49], vertex[55]) / between_eyes)
	container.append(distance_between(vertex[50], vertex[54]) / between_eyes)
	container.append(distance_between(vertex[60], vertex[56]) / between_eyes)
	container.append(distance_between(vertex[61], vertex[66]) / between_eyes)
	container.append(distance_between(vertex[62], vertex[65]) / between_eyes)
	container.append(distance_between(vertex[63], vertex[64]) / between_eyes)

	return container


image = '11.jpg'
image = image.strip().split("/")[-1]
os.system("./face_tracker " + image)
os.system("python v2test.py " + image[:image.index(".")] + ".vector")

wt_v = [[float(x1) for x1 in x.split(",")] for x in open("pca_archive_wt.txt")]
mu_v = [[float(x1) for x1 in x.split(",")] for x in open("pca_archive_mu.txt")][0]
sigma_v = [[float(x1) for x1 in x.split(",")] for x in open("pca_archive_sigma.txt")][0]

fout = open(image[:image.index(".")] + ".pca.test", "w")
for ext in [".test"]:
	if os.path.isfile(image[:image.index(".")] + ext):
		fout.write("1")
		for wt_id in range(17):
			total = 0
			for index in open(image[:image.index(".")] + ext):
				index = [float(x[x.index(":")+1:]) for x in index[2:].split(" ")]
				fout.write(" " + str(wt_id+1) + ":" + str(np.dot(np.array(wt_v[wt_id]), (np.array(index) - np.array(mu_v)) / np.array(sigma_v))))
		fout.write("\n")
fout.close()

model = 'emotions.train.pca.model'
clean_name = model[::-1][model[::-1].index("."): ][::-1]
os.system("./svm-scale -r \"" + clean_name + "range\" \"" + image[:image.index(".")] + ".pca.test\" > \"" + image[:image.index(".")] + ".pca.scale\"")
os.popen("./svm-predict -l 1 -b 1 \"" + image[:image.index(".")] + ".pca.scale\" \"" + clean_name + "model\" \"" + image[:image.index(".")] + ".pca.predict\"").read()

#os.system("rm " + image)
os.system("rm " + image[:image.index(".")] + ".vector")
os.system("rm " + image[:image.index(".")] + "_mirror.vector")
os.system("rm " + image[:image.index(".")] + ".test")
os.system("rm " + image[:image.index(".")] + "_mirror.test")
os.system("rm " + image[:image.index(".")] + ".pca.test")
os.system("rm " + image[:image.index(".")] + ".pca.scale")
#os.system("rm " + image[:image.index(".")] + ".pca.predict")
