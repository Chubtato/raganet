from pydub import AudioSegment


# for i in range(11):
#     sound = AudioSegment.from_wav("./Desh/desh_" + str(i+1) + ".wav")
#     sound = sound.set_channels(1)
#     sound.export("./Desh/desh_mono_" + str(i+1) + ".wav", format="wav")

for i in range(12):
    sound = AudioSegment.from_wav("./Bhimpalasi/bhimpalasi_" + str(i+1) + ".wav")
    sound = sound.set_channels(1)
    sound.export("./Bhimpalasi/bhimpalasi_mono_" + str(i+1) + ".wav", format="wav")