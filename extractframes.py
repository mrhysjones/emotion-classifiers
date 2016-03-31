# Script to extract video frames from GEMEP-FERA dataset and to code the emotion data 

import os, glob, cv2

for subfolder in os.listdir('Datasets/GEMEP-FERA'):
	# Work out emotion 
	for vid in glob.glob('Datasets/GEMEP-FERA/' + subfolder + /.*avi):
		vidcap = cv2.VideoCapture(vid)
		count = 0;
		while success:
			success,image = vidcap.read()
			cv2.imwrite("%d.jpg" % count, image)     # save frame as JPEG file
			count += 1


