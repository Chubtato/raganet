import tensorflow.keras as keras
import os
model = keras.models.load_model('bestmodelsofar.hdf5')
# model.summary()

from pydub import AudioSegment

ragaclass = input("Input raga class:")
file = input("Input file name:")

sound = AudioSegment.from_wav(file)
sound = sound.set_channels(1)
sound.export("./YoutubeTest/test1" +  ".wav", format="wav")

import numpy as np
from wavsplittest import SplitWavAudioMubin
import librosa

split_wav = SplitWavAudioMubin('C:\\Users\\pande\\Documents\\Programming\\raganet\\YoutubeTest', "test1" +  ".wav")
split_wav.multiple_split(min_per_split=1)
os.remove("./YoutubeTest/test1.wav")

files = os.listdir('YoutubeTest')
youtubetest = open("youtubetest2.csv", "w")

for item in files:
    youtubetest.write(ragaclass)
    y, sr = librosa.load('./YoutubeTest/'+ item,sr=1000)
    if(len(y)==30000):
        for i in y:
            youtubetest.write(","+str(i))
        print('Done Writing',item,"length:",len(y),'in train with class',ragaclass)
        youtubetest.write('\n')
    os.remove("./YoutubeTest/" + item)

youtubetest.close()


myFile = np.genfromtxt('youtubetest2.csv', delimiter=',')



for recording in myFile:

    recording = np.array(recording)
    raga = recording[0]
    recording = recording[1:]
    recording = np.reshape(recording, (1, 30000))*100

    prediction = model.predict(recording)
    print(prediction)

    if(prediction[0][0]>prediction[0][1]):
        if(raga == 0):
            print("correct\n")
        else:
            print("wrong\n")

    if(prediction[0][0]<prediction[0][1]):
        if(raga == 1):
            print("correct\n")
        else:
            print("wrong\n")
    


