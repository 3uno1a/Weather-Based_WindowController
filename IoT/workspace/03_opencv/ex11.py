# 화소 접근 흑백 영상 
import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[120, 200] = 0
print(img[100:110, 200:210])  # ROI 접근 (관심영역 region of interest)

# for y in range(100, 400):
#     for x in range(200, 300):
#         img[y, x] = 0

img[100:400, 200:300] = 0 # ROI 접근

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()




