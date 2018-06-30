# python VideoSave.py 1
# coding:utf-8
import numpy as np
import cv2

saveImg = False
cap = cv2.VideoCapture(0)

# 定义解码器并创建VideoWrite对象
# linux: XVID、X264; windows:DIVX
# 20.0指定一分钟的帧数
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output2.avi', fourcc, 10.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # frame = cv2.flip(frame, 3)

        # 写入帧
        if saveImg:
            out.write(frame)

        cv2.imshow('frame', frame)

        key = cv2.waitKey(10)
        if key == 27:
            break
        elif key == ord("s"):
            if saveImg:
                saveImg = False
            else:
                saveImg = True
            print saveImg
    else:
        break

# 释放内存
cap.release()
out.release()
cv2.destroyAllWindows()
