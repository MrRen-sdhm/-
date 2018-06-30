# coding:utf8

# 固定尺寸缩放
# image = cv2.resize(image, (224, 224))
# 按比例缩放
# image1 = cv2.resize(image, (0, 0), fx=zoom, fy=zoom,
#                                 interpolation=cv2.INTER_NEAREST)

import cv2
import os
import numpy as np
import imutils
import shutil
from imutils import paths

imagePath_in = "./images/origion/"
imagePath_out = "./images/resize/"


print "[Info] rebuild output folder..."
shutil.rmtree(imagePath_out)
os.mkdir(imagePath_out)

imagePaths = sorted(list(paths.list_images(imagePath_in)))

for imagePath in imagePaths:
    basename = os.path.basename(imagePath)
    spliname = os.path.splitext(basename)[0]

    image = cv2.imread(imagePath)

    # 跳过无法读取的图片
    try:
        height, width, channle = image.shape
    except AttributeError:
        print AttributeError
        continue

    # 对太宽的图片进行中心剪裁
    if float(width) / float(height) > 4.0 / 3.0:
        w = int(height * 4.0 / 3.0)
        x0 = (int)((width - w) / 2)
        y0 = 0
        image = image[y0:y0 + height, x0:x0 + w]
        print '[Info] clip_width:', basename
        print image.shape

    # 对太高的图片进行中心剪裁
    elif float(height) / float(width) > 4.0 / 3.0:
        h = int(width * 4.0 / 3.0)
        x0 = 0
        y0 = (int)((height - h) / 2)
        image = image[y0:y0 + h, x0:x0 + width]
        print '[Info] clip_height:', basename
        print image.shape

    # 更新shape
    height, width, channle = image.shape

    # 太宽，按照宽度缩放
    if width > 640:
        zoom = 640.0 / width
        # 无法缩放即跳过
        try:
            image = cv2.resize(image, (0, 0), fx=zoom, fy=zoom,
                               interpolation=cv2.INTER_NEAREST)
        except:
            continue
        print '[Info] resize:', basename
        print image.shape

    # 更新shape
    height, width, channle = image.shape

    # 太高，按照高度缩放
    if height > 480:
        zoom = 480.0 / height
        # 无法缩放即跳过
        try:
            image = cv2.resize(image, (0, 0), fx=zoom, fy=zoom,
                               interpolation=cv2.INTER_NEAREST)
        except:
            continue
        print '[Info] resize:', basename
        print image.shape

    # 更新shape
    height, width, channle = image.shape

    # 图片尺寸合适的进行保存
    if (width >= 400 and height >= 280) or (width >= 280 and height >= 400):
        cv2.imwrite(imagePath_out + spliname + '.jpg', image)
        print '[Info] save:', basename
