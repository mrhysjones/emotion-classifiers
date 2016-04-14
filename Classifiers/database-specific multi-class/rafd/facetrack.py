# Python script to obtain vectors of facial landmarks from emotion datasets, and to categorise these vectors into emotions
# First step in building a classifier pipeline

import shutil 
import os, sys, glob

# Emotion classes to consider in data
emotions = {
1: "Angry", 
2 : "Contempt",
3 : "Fear",
4 : "Happy",
5 : "Sadness",
6 : "Surprise", 
7 : "Natural"
}
data = {}

for x in range (1, 8):
	if not emotions[x] in data: data[emotions[x]] = []

# Obtain face data from RaFD database (http://www.socsci.ru.nl:8180/RaFD2/RaFD?p=main)
print "Processing RaFD database"
for face in glob.glob('../../../Datasets/RaFD/*.jpg'):
	face = os.path.basename(face)
	os.system("cp ../../../Datasets/RaFD/" + face + " . ; ./face_tracker " + face + " ; mv " + face[:face.index(".")] + "* ../../../Datasets/RaFD/")
	components = face.split('_')
	if components[4] == 'angry':
		data["Angry"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Angry"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'contemptuous':
		data["Contempt"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Contempt"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'disgust':
		data["Disgust"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Disgust"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'fearful':
		data["Fear"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Fear"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'happy':
		data["Happy"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Happy"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'neutral':
		data["Natural"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Natural"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'sad':
		data["Sadness"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Sadness"].append("../../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'surprised':
		data["Surprise"].append("../../../Datasets/RaFD/" + face.replace("jpg", "vector"))

# Output vectors to emotion folders
print "Categorising vectors"
for emotion_id in data:
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)