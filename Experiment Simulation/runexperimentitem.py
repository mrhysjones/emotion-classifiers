# Code used to predict the emotions for a single item for a single participant
import glob
import os
import shutil
import re
import numpy as np

classifier_desc = 'distributed'
range_file = 'emotions.train.pca.range'
model_file = 'emotions.train.pca.model'

mu_file = 'pca_archive_mu.txt'
sigma_file = 'pca_archive_sigma.txt'
wt_file = 'pca_archive_wt.txt'

wt_v = [[float(x1) for x1 in x.split(",")] for x in open(wt_file)]
mu_v = [[float(x1) for x1 in x.split(",")] for x in open(mu_file)][0]
sigma_v = [[float(x1) for x1 in x.split(",")] for x in open(sigma_file)][0]

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

def test_folder(folder):
	test_frames = glob.glob(folder + '/*.jpg')
	sort_nicely(test_frames)
	folder_components = folder.split('/')
	participant_number = folder_components[-2]
	experiment_item = folder_components[-1]
	result_filename = '%s-%s-%s.txt' % (participant_number, experiment_item, classifier_desc)

	result_file = open(folder + '/' + result_filename, 'w')
	result_file.write('angry,contempt,disgust,fear,happy,sad,surprise,neutral \n')
	for frame in test_frames:
		frame_file = frame.split('/')[-1]
		shutil.copy(frame, frame_file)
		predictions = test_file(frame_file)
		if predictions is None: pass
		else: result_file.write(','.join(str(x) for x in predictions) + '\n')
	result_file.close()

def test_file(image):
	os.system("./face_tracker " + image)
	if not (os.path.exists(image[:image.index(".")] + ".vector")):
		clean_up(image)
		return None
	os.system("python v2test.py " + image[:image.index(".")] + ".vector")
	pca_data = open(image[:image.index(".")] + ".pca.test", "w")
	pca_data.write("1")
	for wt_id in range(17):
		total = 0
		for index in open(image[:image.index(".")] + '.test'):
			index = [float(x[x.index(":")+1:]) for x in index[2:].split(" ")]
			pca_data.write(" " + str(wt_id+1) + ":" + str(np.dot(np.array(wt_v[wt_id]), (np.array(index) - np.array(mu_v)) / np.array(sigma_v))))
	pca_data.write("\n")
	pca_data.close()
	os.system("./svm-scale -r " + range_file + " " + image[:image.index(".")] + ".pca.test >" + image[:image.index(".")] + ".pca.scale")
	os.system("./svm-predict -b 1 " + image[:image.index(".")] + ".pca.scale "  + model_file + " " + image[:image.index(".")] + ".pca.predict > /dev/null 2>&1")

	predict_file = open(image[:image.index(".")] + ".pca.predict")
	predict_contents = predict_file.readlines()

	results = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	for i in range(1, 9):
		key = int(predict_contents[0].split(' ')[i])
		val = float(predict_contents[1].split(' ')[i])
		results[key-1] = val
	clean_up(image)
	return results

def clean_up(image):
    base_name = image[:image.index(".")]
    if os.path.exists(base_name + '.jpg'):
        os.system("rm " + base_name + ".jpg")
    if os.path.exists(base_name + '_mirror.vector'):
        os.system("rm " + base_name + "_mirror.vector")
    if os.path.exists(base_name + '.vector'):
        os.system("rm " + base_name + ".vector")
    if os.path.exists(base_name + '.test'):
        os.system("rm " + base_name + ".test")
    if os.path.exists(base_name + '.pca.test'):
        os.system("rm " + base_name + ".pca.test")
    if os.path.exists(base_name + '.pca.scale'):
        os.system("rm " + image[:image.index(".")] + ".pca.scale")
    if os.path.exists(base_name + '.pca.predict'):
        os.system("rm " + image[:image.index(".")] + ".pca.predict")