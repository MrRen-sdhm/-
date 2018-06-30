# coding:utf8
# 此脚本可通过滑块调节纯色图片的三个通道值，并可保存生成的纯色图片
import cv2
import numpy as np
import time

# 当调节滑块时，调用这个函数。这个没有使用到
def do_nothing(x):
    pass


# 创建黑图像
img = np.zeros((480, 640, 3), np.uint8)
cv2.namedWindow('image')
# 创建滑块,注册回调函数
cv2.createTrackbar('R', 'image', 0, 255, do_nothing)
cv2.createTrackbar('G', 'image', 0, 255, do_nothing)
cv2.createTrackbar('B', 'image', 0, 255, do_nothing)

while(1):
    # 获得滑块的位置
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    # 设置图像颜色
    img[:] = [b, g, r]

    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("s"):
        cv2.imwrite('bgr_' + str(b) + '_' + str(g) + '_' + str(r) + '.jpg', img)


cv2.destroyAllWindows()
