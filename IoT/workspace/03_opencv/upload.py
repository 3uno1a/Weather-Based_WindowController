import requests

file_name = 'filename.mp4'
file_path = './' + file_name

# data = {
#     'file_name' : file_name
# }

# files = {
#     'sec_file' : open(file_path, 'rb')
# }

# response = requests.post('http://127.0.0.1:8000/iot/upload/', 
#                         data=data, files=files)
# data = response.json()

# if data['result'] == 'success':
#     print('upload 성공')
# else:
#     print('실패')

UPLOAD_URL = 'http://192.168.35.245:8000/iot/upload/'
INTRUSION_URL = 'http://192.168.35.245:8000/iot/intrusion/'

def notify_intrusion():     # 카톡 메세지
    response = requests.get(INTRUSION_URL)
    res = response.json()

    if res['result'] == 'success':
        return True
    else:
        return False

def upload(file_path):
    file_name = file_path.split('/')[-1]   # 제일 마지막의 element가 파일명
    data = {'file_name': file_name}
    files = {'sec_file': open(file_path, 'rb')}   # 파일을 binary 모드로 열어

    response = requests.post(UPLOAD_URL, 
                             data = data, files = files)  # 서버에 http POST로 업로드
    res = response.json()

    if res['result'] == 'success':
        return True
    else:
        return False

