import cv2
from harrdetect import HarrDetect

image_file = "./data/face1.jpg"
image = cv2.imread(image_file)

cascade = HarrDetect('haarcascade_frontalface_default.xml')

face_list = cascade.detect(image)

if (len(face_list) > 0):
    cascade.draw_rect(image, face_list)
    cv2.imwrite("facedetect-output1.PNG", image)

else:
    print("no face")











