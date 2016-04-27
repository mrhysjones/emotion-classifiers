import os
import csv
import sys 

items = ['bbc', 'chicken', 'dadjoke', 'guinness',
	'huffington', 'news', 'puppy', 'ybf']
classifier_desc = 'distributed'
no = 16

# Arrays to hold the raw measurements for each class 
for x in items:
	minlength = sys.maxint
	angry = []
	contempt = [] 
	disgust = []
	fear = []	
	happy = []
	neutral = []
	sadness = []
	surprise = []
	for p in os.listdir('Frames'):
		result_path = 'Frames/%s/%s/%s-%s-%s.txt' % (p, x, p, x, classifier_desc)
		with open(result_path, 'r') as f:
			reader = csv.reader(f)
			emotion_data = list(reader)
			if len(emotion_data) < minlength: minlength = len(emotion_data)
			a, c, d, f, h, n, sa, su = [], [], [], [], [], [], [], []
			for i in range(1, len(emotion_data)):
				a.append(emotion_data[i][0])
				c.append(emotion_data[i][1])
				d.append(emotion_data[i][2])
				f.append(emotion_data[i][3])
				h.append(emotion_data[i][4])
				sa.append(emotion_data[i][5])
				su.append(emotion_data[i][6])
				n.append(emotion_data[i][7])

			angry.append(a)
			contempt.append(c)
			disgust.append(d)
			fear.append(f)
			happy.append(h)
			neutral.append(n)
			sadness.append(sa)
			surprise.append(su)

	filename = 'distributed-results/%s-averages.txt' % (x)
	res = open(filename, 'w')
	print filename
	res.write('angry,contempt,disgust,fear,happy,sadness,surprise,neutral,\n')
	for y in range(0, minlength - 1):
		averages = []
		avga, avgc, avgd, avgf, avgh, avgn, avgsa, avgsu = 0, 0, 0, 0, 0, 0, 0, 0
		for z in range(0, no):
			avga += float(angry[z][y])
			avgc += float(contempt[z][y])
			avgd += float(disgust[z][y])
			avgf += float(fear[z][y])
			avgh += float(happy[z][y])
			avgn += float(neutral[z][y])
			avgsa += float(sadness[z][y])
			avgsu += float(surprise[z][y])

		averages.extend([avga/no, avgc/no, avgd/no, avgf/no, avgh/no, avgsa/no, avgsu/no, avgn/no])
		averagestr = ','.join(str(x) for x in averages) + '\n'
		res.write(averagestr)
