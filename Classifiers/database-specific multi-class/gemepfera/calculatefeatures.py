# Python script to calculate the distance measures (features) for all of the tracked face data
# 
import os

# Supporting method to calculate distance between two points
def distance_between(n1, n2):
	return (abs(n1[0] - n2[0])**2 + abs(n1[1] - n2[1])**2)**0.5

# Supporting method to calculate midpoint of two points
def point_between(n1, n2):
	x = [n1[0], n2[0]]
	y = [n1[1], n2[1]]
	return (abs(x[0] - x[1])/2 + min(x), abs(y[0] - y[1])/2 + min(y))

emotions = {
	"Angry"	: 1,
	"Fear" : 2,
	"Happy" : 3,
	"Sadness" : 4
}

data = {}
fout = open("emotions.train", "w")
for name in ["Happy", "Sadness", "Angry", "Fear"]:
	data[str(emotions[name])] = []
	for sequence in os.listdir('Face data/' + name):
		data[str(emotions[name])].append([])
		for entry in open('Face data/' + name + "/" + sequence):
			x, y = [float(a) for a in entry.strip().replace("   ", " ").split(" ")]
			data[str(emotions[name])][-1].append((x, y))

for key in data:
	for index in range(len(data[key])):
		i = 1
		vertex = [0.0] + data[key][index]

		fout.write(key)

		left_eye = point_between(vertex[37], vertex[40])
		right_eye = point_between(vertex[43], vertex[46])
		between_eyes = distance_between(left_eye, right_eye)
		nose = point_between(vertex[31], vertex[34])
		for x in range(1, 17 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], nose) / between_eyes))
			i += 1
		for x in range(18, 22 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], left_eye) / between_eyes))
			i += 1
		for x in range(23, 27 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], right_eye) / between_eyes))
			i += 1
		for x in range(32, 36 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], nose) / between_eyes))
			i += 1
		for x in range(37, 42 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], left_eye) / between_eyes))
			i += 1
		for x in range(43, 48 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], right_eye) / between_eyes))
			i += 1
		for x in range(49, 66 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], nose) / between_eyes))
			i += 1
		for x in range(0, 5):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[18+x], vertex[27-x]) / between_eyes))
			i += 1
		for x in range(23, 27 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], nose) / between_eyes))
			i += 1
		for x in range(18, 22 + 1):
			fout.write(" " + str(i) + ":" + str(distance_between(vertex[x], nose) / between_eyes))
			i += 1

		fout.write(" " + str(i) + ":" + str(distance_between(vertex[53], vertex[57]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[52], vertex[58]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[51], vertex[59]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[49], vertex[55]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[50], vertex[54]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[60], vertex[56]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[61], vertex[66]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[62], vertex[65]) / between_eyes))
		i += 1
		fout.write(" " + str(i) + ":" + str(distance_between(vertex[63], vertex[64]) / between_eyes))
		fout.write("\n")
