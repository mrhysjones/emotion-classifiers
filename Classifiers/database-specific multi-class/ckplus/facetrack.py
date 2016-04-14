# Python script to obtain vectors of facial landmarks from emotion datasets, and to categorise these vectors into emotions
# First step in building a classifier pipeline

import shutil 
import os, sys, glob

# Emotion classes to consider in data
emotions = {
1: "Angry", 
2 : "Contempt",
3 : "Disgust",
4 : "Fear",
5 : "Happy",
6 : "Sadness",
7 : "Surprise"
}
data = {}

# Obtain face data from CK+ Database (http://www.consortium.ri.cmu.edu/ckagree/)
print "Processing CK+ database"
for sequence in os.listdir("../../../Datasets/CK+/Emotion"):
	if sequence != '.DS_Store':
		for episode in os.listdir('../../../Datasets/CK+/Emotion/' + sequence):
			if episode != '.DS_Store':
				for index in glob.glob("../../../Datasets/CK+/Emotion/" + sequence + "/" + episode + "/*.txt"):
					index = os.path.basename(index)
					index = index[:index.index("_emotion")]
					for i, index_content in enumerate(open("../../../Datasets/CK+/Emotion/" + sequence + "/" + episode + "/" + index + "_emotion.txt")):
						emotion = emotions[int(float(index_content.strip()))]
	 					if not emotion in data: data[emotion] = []
						os.system("cp ../../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".png . ; ./face_tracker " + index + ".png ; mv " + index + "* ../../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/")
						data[emotion].append("../../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".vector")
						data[emotion].append("../../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + "_mirror.vector")

# Output vectors to emotion folders
print "Categorising vectors"
for emotion_id in data:
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)