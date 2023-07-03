from gtts import gTTS
from io import BytesIO
import speech_recognition as sr
from pydub import AudioSegment

text = "안녕하세요. 반갑습니다."

def save(self, savefile):
# …
    with open(str(savefile), "wb") as f:
        self.write_to_fp(f)
        log.debug("Saved to %s", savefile)

def save2(self, f):
    self.write_to_fp(f)


mp3 = BytesIO()
tts= gTTS(text=text, lang='ko')
tts.save2(mp3)  # mp3로저장
mp3.seek(0)

wav = BytesIO()
sound = AudioSegment.from_file(mp3, format="mp3")
sound.export(wav, format="wav")
wav.seek(0)

r = sr.Recognizer()

with sr.AudioFile(wav) as source:
    audio = r.listen(source)
    print(r.recognize_google(audio, language='ko-KR'))
