import sounddevice
from scipy.io.wavfile import write
fs = 44100
second = int(input("enter the time duration in second: "))
print('recording...')


recording_voice = sounddevice.rec(int(second * fs), samplerate=fs,channels=2)
sounddevice.wait()

write("out.wav",fs,recording_voice)
print(" ...\nplease check it...")



