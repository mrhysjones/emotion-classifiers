# Python script to obtain vectors of facial landmarks from emotion datasets, and to categorise these vectors into emotions
# First step in building a classifier pipeline

import shutil 
import os, sys, glob

# Emotion classes to consider in data
emotions = {
1: "Angry", 
2 : "Fear",
3 : "Happy",
4 : "Sadness"
}
data = {}

for x in range (1, 5):
	if not emotions[x] in data: data[emotions[x]] = []

# Obtain face data from GEMEP-FERA training data
print "Processing GEMEP-FERA database"
gemep_path = '../../../Datasets/GEMEP-FERA/training/'
for recording in os.listdir(gemep_path):
	if recording != '.DS_Store':
		for frame in glob.glob(gemep_path + recording + '/*.jpg'):
			frame = os.path.basename(frame)
			os.system("cp " + gemep_path + recording + '/' + frame + " . ; ./face_tracker " + frame + " ; mv " + frame[:frame.index(".")] + "* " + gemep_path + '/' + recording)
			components = frame.split('-')
			if components[1] == 'anger':
				data["Angry"].append(gemep_path + '/' + recording + '/' + frame.replace("jpg", "vector"))
	 			data["Angry"].append(gemep_path + '/' + recording + '/' + frame[:frame.index(".")] + "_mirror.vector")
	 		elif components[1] == 'fear':
				data["Fear"].append(gemep_path + '/' + recording + '/' + frame.replace("jpg", "vector"))
	 			data["Fear"].append(gemep_path + '/' + recording + '/' + frame[:frame.index(".")] + "_mirror.vector")	
	 		elif components[1] == 'joy':
				data["Happy"].append(gemep_path + '/' + recording + '/' + frame.replace("jpg", "vector"))
	 			data["Happy"].append(gemep_path + '/' + recording + '/' + frame[:frame.index(".")] + "_mirror.vector")
	 		elif components[1] == 'sadness':
				data["Sadness"].append(gemep_path + '/' + recording + '/' + frame.replace("jpg", "vector"))
	 			data["Sadness"].append(gemep_path + '/' + recording + '/' + frame[:frame.index(".")] + "_mirror.vector")
				
# Output vectors to emotion folders
print "Categorising vectors"
for emotion_id in data:
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)