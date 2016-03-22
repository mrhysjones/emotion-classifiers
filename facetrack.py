# Python script to obtain vectors of facial landmarks from emotion datasets, and to categorise these vectors into emotions
# First step in building a classifier pipeline

import shutil 
import os, sys

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

# Data source dependent - don't want to include in emotion class list but still want to initialise
data["Natural"] = [] 

# Used to output the _not vectors for particular emotions
everything = []

# Obtain face data from CK+ Database
print "Processing CK+ database"
for sequence in os.listdir("Datasets/CK+/Emotion"):
	if sequence != '.DS_Store':
		for episode in os.listdir("Datasets/CK+/Emotion/" + sequence):
			natural = True
			for index in os.listdir("Datasets/CK+/Emotion/" + sequence + "/" + episode):
				index = index[:index.index("_emotion")]
				natural = False
				for i, index_content in enumerate(open("Datasets/CK+/Emotion/" + sequence + "/" + episode + "/" + index + "_emotion.txt")):
					emotion = emotions[int(float(index_content.strip()))]
					if not emotion in data: data[emotion] = []
					os.system("cp Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".png . ; ./face_tracker " + index + ".png ; mv " + index + "* Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/")
					data[emotion].append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".vector")
					data[emotion].append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + "_mirror.vector")
					everything.append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".vector")
					everything.append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + "_mirror.vector")
					if natural: 
						for index in os.listdir("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode):
							if ".png" in index:
								os.system("cp Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + " . ; ./face_tracker " + index + " ; mv " + index[:index.index(".")] + "* Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/")
								data["Natural"].append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index[:index.index(".")] + ".vector")
								everything.append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index[:index.index(".")] + "_mirror.vector")		
							else:
								index = sorted(os.listdir("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode))[0]
								os.system("cp Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + " . ; ./face_tracker " + index + " ; mv " + index[:index.index(".")] + "* Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/")
								data["Natural"].append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index[:index.index(".")] + ".vector")
								everything.append("Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index[:index.index(".")] + "_mirror.vector")

# Obtain face data for KDEF Database
for sequence in os.listdir("Datasets/KDEF"):
	print "Processing KDEF database"
	if sequence != '.DS_Store':
		for episode in os.listdir("Datasets/KDEF/" + sequence):
			if episode[len(episode)-3:] == "JPG" and episode[6] == "S":
				os.system("cp Datasets/KDEF/" + sequence + "/" + episode + " . ; ./face_tracker " + episode + " ; mv " + episode[:episode.index(".")] + "* Datasets/KDEF/" + sequence + "/")
				if episode[4:6] == "AF":
					data["Fear"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Fear"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				elif episode[4:6] == "AN":
					data["Angry"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Angry"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				elif episode[4:6] == "DI":
					data["Disgust"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Disgust"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				elif episode[4:6] == "HA":
					data["Happy"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Happy"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				elif episode[4:6] == "NE":
					data["Natural"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Natural"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				elif episode[4:6] == "SA":
					data["Sadness"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Sadness"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				elif episode[4:6] == "SU":
					data["Surprise"].append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
					data["Surprise"].append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
				everything.append("Datasets/KDEF/" + sequence + "/" + episode.replace("JPG", "vector"))
				everything.append("Datasets/KDEF/" + sequence + "/" + episode[:episode.index(".")] + "_mirror.vector")
 
# Output vectors to emotion folders
for emotion_id in data:
	print "Categorising vectors"
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)

			if not os.path.exists(emotion_id + " not"): os.makedirs(emotion_id + " not")
			for index in set(everything) - set(data[emotion_id]):
				try:
					shutil.copy2(index, "Face data/" + emotion_id + " not")
				except:
					print("Error not:", index)   