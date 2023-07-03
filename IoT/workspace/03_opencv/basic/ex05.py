import cv2

cap = cv2.VideoCapture(0) # 0번 카메라

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 호출할 때


out1 = cv2.VideoWriter('./data/record0.mp4', fourcc, 20.0)
out2 = cv2.VideoWriter('./data/record1.mp4', fourcc, 20.0, isColor=False)
