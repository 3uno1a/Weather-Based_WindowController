import cv2

image_file = './data/lena.jpg'
# image_file = '/data/lena.jpg'

img = cv2.imread(image_file)  # cv2.IMREAD_COLOR가 디폴트
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape)
# (512, 512, 3) (512, 512)
print(img.dtype, img2.dtype)
# uint8 uint8

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)


key = cv2.waitKey(1000)  # 키보드 입력 대기
# 시간 설정 가능 1초동안 키 입력 기다리기 --> 입력이 없으면 return -1

print(key)  # 키를 누르면 사진들이 사라짐
# 13 - 엔터키를 치면 엔터키 코드가 리턴




