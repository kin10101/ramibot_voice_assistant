import whisper


model = whisper.load_model('base')
result = model.transcribe('audio/Asia Pacific College - Alma Mater Hymn.wav', fp16=False, language='english')
print(result)

#ffmpeg issue