import wave

import whisper
import pyaudio

"""
NOTE:
OUTPUT FROM THIS IS SLOW PROBABLY DUE TO DEVICE LIMITATION EG. NO GPU.

"""

# Set up the microphone input
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Listening...")

frames = []
seconds = 3
for i in range(0, int(RATE / CHUNK * seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

print("recording stopped")

stream.stop_stream()
stream.close()
audio.terminate()

audiofile = wave.open("output.wav", "wb")
audiofile.setnchannels(CHANNELS)
audiofile.setsampwidth(audio.get_sample_size(FORMAT))
audiofile.setframerate(RATE)
audiofile.writeframes(b''.join(frames))
audiofile.close()

model = whisper.load_model("base")
result = model.transcribe("output.wav")

print(result["text"])
