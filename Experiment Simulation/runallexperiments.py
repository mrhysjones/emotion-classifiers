from runexperimentitem import *
import os

# Runs through each experiment participant/item and
# produces a CSV file of predictions

for p in os.listdir('Frames'):
    for subfolder in os.listdir('Frames/' +  p):
        if os.path.isdir('Frames/' + p + '/' + subfolder):
            print 'Processing Frames/' + p + '/' + subfolder
            test_folder('Frames/' + p + '/' + subfolder)
