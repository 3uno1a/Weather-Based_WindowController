from gtts import gTTS

text = "Hello, 안녕하세요."
tts= gTTS(text=text, lang='ko')
tts.save('hello.mp3')
