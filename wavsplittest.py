from pydub import AudioSegment
import math

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * timepersplit * 1000
        t2 = to_min * timepersplit * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / timepersplit)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


timepersplit = 30

# for i in range(11):
#     folder = 'C:\\Users\\pande\\Documents\\Programming\\raganet\\Desh'
#     file = 'desh_mono_' + str(i+1) + '.wav'
#     split_wav = SplitWavAudioMubin(folder, file)
#     split_wav.multiple_split(min_per_split=1)

# for i in range(12):
#     folder = 'C:\\Users\\pande\\Documents\\Programming\\raganet\\Bhimpalasi'
#     file = 'bhimpalasi_mono_' + str(i+1) + '.wav'
#     split_wav = SplitWavAudioMubin(folder, file)
#     split_wav.multiple_split(min_per_split=1)
 
