from pydub import AudioSegment
from pydub.playback import play
import requests

def get_emotion():
    # url = 'http://192.168.35.245:8000/api/emotion/'
    url = 'http://172.30.1.111:8000/api/emotion/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("API GET 요청 성공")
        return data[0]['emotion']
    else:
        print("API GET 요청 실패:", response.status_code)
        return None
    
def adjust_volume(audio_segment, volume_change):
    adjusted_audio = audio_segment + volume_change
    return adjusted_audio 


mp3_positive = "positive.mp3"
mp3_negative = "negative.mp3" 
volume_change = - 10

while True:
    emotion = get_emotion()
    if emotion == 1:
        mp3 = AudioSegment.from_file(mp3_positive, format="mp3")
        print("positive 음원 재생 중...")

    elif emotion == 0:
        mp3 = AudioSegment.from_file(mp3_negative, format="mp3")
        print("negative 음원 재생 중...")
        
    else:
        print("유효하지 않은 감정 값입니다.")
        continue

    adjusted_mp3 = adjust_volume(mp3, volume_change)
    play(adjusted_mp3)