import pydub
from pydub import AudioSegment
from pydub.playback import play

# Load the MP3 file
song = AudioSegment.from_mp3("audio/Asia Pacific College - Alma Mater Hymn Short Ver.wav")
wakeSound = AudioSegment.from_mp3("audio/activate.wav")
endSound = AudioSegment.from_mp3("audio/deactivate.wav")


