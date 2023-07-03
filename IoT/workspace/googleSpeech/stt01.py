import speech_recognition as sr

r = sr.Recognizer()
# with sr.Michropone() as source:

with sr.AudioFile('output.wav') as source:
    audio = r.listen(source)
    print(r.recognize_google(audio, language='ko-KR'))
