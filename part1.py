import wave

# Audio Signal Parameters
# - number of channels (mono audio)
# - sample width
# - framerate/sample_rate: 44,100 Hz
# - number of frames
# - values of a frame

test = wave.open("pyaudiolib\Hello Fine Schyte ho.wav", "rb")
print("num channels: " + str(test.getnchannels()))
print("sample width channels: " + str(test.getsampwidth()))
print("framerate: :" + str(test.getframerate()))
print("num frames!!!: " + str(test.getnframes()))
print("parameters here: " + str(test.getparams()))

# calc time of audio
t_audio = test.getnframes()/test.getframerate()
print(t_audio)

frames = test.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

new_test = wave.open("hawk_tuah.wav", "wb")

new_test.setnchannels(1)
new_test.setsampwidth(1)
new_test.setframerate(48000)
new_test.writeframes(frames)
new_test.close()