#setting up microphone parameters
#how many bytes of data per chunk of audio processed
import pyaudio

FRAMES_PER_BUFFER = 3200

#port audio input\output bit integer format. default
FORMAT = pyaudio.paInt16
#we only need the input audio coming from one place.
CHANNELS = 1
#rate in hz of incoming audio
RATE = 16000

p = pyaudio.PyAudio
#starts recording, creating variables and assigning parameters
stream = p.open(format = FORMAT, channels= CHANNELS, rate= RATE, input= True,frames_per_buffer= FRAMES_PER_BUFFER)

print(p.get_default_output_device_info())