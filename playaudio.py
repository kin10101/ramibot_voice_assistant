import pydub
from pydub import AudioSegment
from pydub.playback import play

# Load the MP3 file
song = AudioSegment.from_mp3("Asia Pacific College - Alma Mater Hymn Short Ver.wav")
wakeSound = AudioSegment.from_mp3("wakesound.wav")

louder_sound = wakeSound + 3

