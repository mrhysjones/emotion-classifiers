# Python script to obtain vectors of facial landmarks from emotion datasets, and to categorise these vectors into emotions
# First step in building a classifier pipeline

import shutil 
import os, sys, glob

# Emotion classes to consider in data
emotions = {
1: "Angry", 
2 : "Disgust",
3 : "Fear",
4 : "Happy",
5 : "Sadness",
6 : "Surprise", 
7 : "Natural"
}
data = {}

for x in range (1, 8):
	if not emotions[x] in data: data[emotions[x]] = []

# # Obtain face data for KDEF Database (http://www.emotionlab.se/resources/kdef)
print "Processing KDEF database"
for sequence in os.listdir("../../../Datasets/KDEF"):
	if sequence != '.DS_Store':
		for face in glob.glob("../../../Datasets/KDEF/" + sequence + '/*.JPG'):
			face = os.path.basename(face)
			if face[6] == "S":
				os.system("cp ../../../Datasets/KDEF/" + sequence + "/" + face + " . ; ./face_tracker " + face + " ; mv " + face[:face.index(".")] + "* ../../../Datasets/KDEF/" + sequence + "/")
				if face[4:6] == "AF":
					data["Fear"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Fear"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "AN":
					data["Angry"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Angry"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "DI":
					data["Disgust"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Disgust"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "HA":
					data["Happy"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Happy"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "NE":
					data["Natural"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Natural"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "SA":
					data["Sadness"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Sadness"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "SU":
					data["Surprise"].append("../../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Surprise"].append("../../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")

# Output vectors to emotion folders
print "Categorising vectors"
for emotion_id in data:
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)