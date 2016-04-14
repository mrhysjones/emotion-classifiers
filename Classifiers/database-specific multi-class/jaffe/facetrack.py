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

# Obtain face data from JAFFE Database (http://www.kasrl.org/jaffe.html)
print "Processing JAFFE database"
for face in glob.glob('../../../Datasets/jaffe/*.jpeg'):	
	face = os.path.basename(face)
	os.system("cp ../../../Datasets/jaffe/" + face + " . ; ./face_tracker " + face + " ; mv " + face[:face.index(".")] + "* ../../../Datasets/jaffe/")
	if face[3:5] == "FE":
		data["Fear"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Fear"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "AN":
		data["Angry"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Angry"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "DI":
		data["Disgust"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Disgust"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "HA":
		data["Happy"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Happy"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "NE":
		data["Natural"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Natural"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "SA":
		data["Sadness"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Sadness"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "SU":
		data["Surprise"].append("../../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Surprise"].append("../../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")

# Output vectors to emotion folders
print "Categorising vectors"
for emotion_id in data:
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)