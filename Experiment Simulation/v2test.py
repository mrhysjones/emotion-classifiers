from sys import argv 
import os, sys

def distance_between(n1, n2):
	return (abs(n1[0] - n2[0])**2 + abs(n1[1] - n2[1])**2)**0.5

def point_between(n1, n2):
	x = [n1[0], n2[0]]
	y = [n1[1], n2[1]]
	return (abs(x[0] - x[1])/2 + min(x), abs(y[0] - y[1])/2 + min(y))

if len(sys.argv) < 2 or not os.path.isfile(argv[1]): sys.exit()

i = 1
vertex = [0.0] + [(float(index.strip().split("   ")[0]), float(index.strip().split("   ")[1])) for index in open(argv[1])]

out_name = argv[1][::-1][argv[1][::-1].index(".")+1: ][::-1] if "." in argv[1] else argv[1]

fout = open(out_name + ".test", "w")

fout.write("1") # True

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
fout.close()
