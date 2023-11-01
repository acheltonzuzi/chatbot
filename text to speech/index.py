from gtts import gTTS

text='olá, eu sou Achelton Pambo'
tts=gTTS(text,lang='pt')
tts.save('texto.mp3')