# -*- coding: utf-8 -*-
"""
BMCL BAEKSUWHAN
@author: lukious
"""

import sys, os, os.path
from scipy.io import wavfile
import pandas as pd
import random
import librosa
import numpy as np

# input_filename = input("Input file number:")
# if input_filename[-3:] != 'wav':
#     print('WARNING!! Input File format should be *.wav')
#     sys.exit()

# samrate, data = wavfile.read(str('./Desh/' + input_filename))
# print('Load is Done! \n')
def common_elements(list_1, list_2):
    a_set = set(list_1)
    b_set = set(list_2)
    if len(a_set.intersection(b_set)) > 0:
        return(True)
    return(False)

# print(final)
train = open("Raga11025sr_TRAIN.csv", "w")
test = open("Raga11025sr_TEST.csv", "w")

blist=os.listdir('Bhimpalasi')

random.shuffle(blist)
blisttrain = blist[:270]
blisttest = blist[270:362]

dlist=os.listdir('Desh')
random.shuffle(dlist)
dlisttrain = dlist[:270]
dlisttest = dlist[270:]
print (len(dlisttrain), len(blisttrain))
print (len(dlisttest), len(blisttest))

trainset = []
testset = []
for filename in blisttrain:
    trainset.append(filename)
for filename in dlisttrain:
    trainset.append(filename)
for filename in blisttest:
    testset.append(filename)
for filename in dlisttest:
    testset.append(filename)
random.shuffle(trainset)
random.shuffle(testset)

sampleRate = 11025
for filename in trainset:
    if "bhimpalasi" in filename:
        train.write("1")
        y, sr = librosa.load('./Bhimpalasi/'+ filename,sr=sampleRate)
        for i in y:
            train.write(","+str(i))
        print('Done Writing',filename,"length:",len(y),'in train with class 1')
        train.write('\n')
    else:
        train.write("2")
        y, sr = librosa.load('./Desh/'+ filename,sr=sampleRate)
        for i in y:
            train.write(","+str(i))
        print('Done Writing',filename,"length:",len(y),'in train with class 2')
        train.write('\n')

for filename in testset:
    if "bhimpalasi" in filename:
        test.write("1")
        y, sr = librosa.load('./Bhimpalasi/'+ filename,sr=sampleRate)
        for i in y:
            test.write(","+str(i))
        print('Done Writing',filename,"length:",len(y),'in test with class 1')
        test.write('\n')
    else:
        test.write("2")
        y, sr = librosa.load('./Desh/'+ filename,sr=sampleRate)
        for i in y:
            test.write(","+str(i))
        print('Done Writing',filename,"length:",len(y),'in test with class 2')
        test.write('\n')



# if len(wavData.columns) == 2:
#     print('Stereo .wav file\n')
#     wavData.columns = ['R', 'L']
#     stereo_R = pd.DataFrame(wavData['R'])
#     stereo_L = pd.DataFrame(wavData['L'])
#     print('Saving...\n')
#     stereo_R.to_csv(str(input_filename[:-4] + "_Output_stereo_R.csv"), mode='w')
#     stereo_L.to_csv(str(input_filename[:-4] + "_Output_stereo_L.csv"), mode='w')
#     # wavData.to_csv("Output_stereo_RL.csv", mode='w')
#     print('Save is done ' + str(input_filename[:-4]) + '_Output_stereo_R.csv , '
#                           + str(input_filename[:-4]) + '_Output_stereo_L.csv')

# elif len(wavData.columns) == 1:
#     print('Mono .wav file\n')
#     wavData.columns = ['M']

#     wavData.to_csv(str(input_filename[:-4] + "_Output_mono.csv"), mode='w')

#     print('Save is done ' + str(input_filename[:-4]) + '_Output_mono.csv')

# else:
#     print('Multi channel .wav file\n')
#     print('number of channel : ' + len(wavData.columns) + '\n')
#     wavData.to_csv(str(input_filename[:-4] + "Output_multi_channel.csv"), mode='w')

#     print('Save is done ' + str(input_filename[:-4]) + 'Output_multi_channel.csv')