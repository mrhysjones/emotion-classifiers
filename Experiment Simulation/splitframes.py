# Script to extract the raw video frames from the experiment video - to
# test other classifiers

import os, glob, cv2

result_path = '../Result data/Participant data/'

for subfolder in os.listdir(result_path):
    print subfolder
    if os.path.isdir(result_path + subfolder):
        video_path = result_path + subfolder + '/Video'
        frame_path = 'Frames/' + subfolder
        if not os.path.exists(frame_path):
            os.mkdir(frame_path)

        for vid in os.listdir(video_path):
            if vid.endswith('.mp4'):
                experiment_item = vid.split('.')[0]
                experiment_frame_path = frame_path + '/' + experiment_item
                if not os.path.exists(experiment_frame_path):
                    os.mkdir(experiment_frame_path)

                vidcap = cv2.VideoCapture(video_path + '/' + vid)
                count = 0
                success = True
                while success:
                    success,image = vidcap.read()
                    if success:
                        file_name =  '%d.jpg' % (count + 1)
                        cv2.imwrite('%s/%s' % (experiment_frame_path, file_name), image)
                        count += 1
