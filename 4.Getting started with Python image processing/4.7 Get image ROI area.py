'''

ROI(region of interest)表示感兴趣区域，是指从被处理图像以方框、圆形、椭圆、不规则多边形等方式勾勒出需要处理的区域。
通过各种算子(Operator)和函数求得ROI区域，广泛应用于热点地图、人脸识别、图像分割等领域。

'''

import cv2
import numpy as np

# # 获取ROI区域并显示
# img = cv2.imread('lena.jpg')
#
# face = np.ones((200, 200, 3))
# cv2.imshow('demo', img)
# face = img[200:400, 200:400]
# cv2.imshow('face', face)

# 提取lena脸部轮廓融合至一幅新的图像中
img = cv2.imread('../第4章 Python图像处理入门/lena.jpg')
test = cv2.imread('../第4章 Python图像处理入门/people.jpg')
face = np.ones((150, 150, 3))
cv2.imshow('demo', img)

face = img[200:350, 200:350]
test[250:400, 250:400] = face
cv2.imshow('result', test)

cv2.waitKey(0)
cv2.destroyAllWindows()
