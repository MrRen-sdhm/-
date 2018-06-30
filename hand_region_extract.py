import cv2
import numpy as np
import imutils

images = cv2.imread("./images/3.jpg")
cv2.imshow('images', images)
cv2.imwrite("images.jpg", images)
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# _, Thre1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# image, contours, hierarchy = cv2.findContours(Thre1.copy(),
#                                               cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
# cv2.imshow('Three', frame)

frame = cv2.cvtColor(images, cv2.COLOR_BGR2YCR_CB)
Y = cv2.split(frame)[0]
Cr = cv2.split(frame)[1]
Cb = cv2.split(frame)[2]

cv2.imshow('Frame', frame)
cv2.imwrite("frame.jpg", frame)
# cv2.imshow('Y', Y)
cv2.imshow('Cr', Cr)
cv2.imwrite("Cr.jpg", Cr)
# cv2.imshow('Cb', Cb)
blur = cv2.GaussianBlur(Cr, (5, 5), 5)

ret, Thre = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY)
cv2.imshow('Thre', Thre)
# apply a series of erosions and dilations to the mask
# using an elliptical kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
skinMask = cv2.morphologyEx(Thre, cv2.MORPH_OPEN, kernel)
cv2.imshow('skin', skinMask)
cv2.imwrite("skinMask.jpg", skinMask)

# skinMask = cv2.cvtColor(skinMask, cv2.COLOR_GRAY2BGR)
outimg = cv2.bitwise_and(images.copy(), images.copy(), mask=skinMask)
cv2.imshow('outimg', outimg)
cv2.imwrite("outimg.jpg", outimg)

image, contours, hierarchy = cv2.findContours(skinMask.copy(),
                                              cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# find contour with max area
cnt = max(contours, key=lambda x: cv2.contourArea(x))

# create bounding rectangle around the contour (can skip below two lines)
x, y, w, h = cv2.boundingRect(cnt)
# cv2.rectangle(images, (x, y), (x + w, y + h), (0, 0, 255), 0)

cv2.drawContours(images, [cnt], -1, (0, 0, 255), 2)
cv2.imwrite("contours.jpg", images)

# cv2.imshow('Gray', images)

# cv2.drawContours(Cb, contours, -1, (0, 0, 255),
#                  2)
key = cv2.waitKey(0) & 0xFF
