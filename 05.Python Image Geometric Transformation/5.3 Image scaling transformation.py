'''

图像缩放(image scaling)是指对数字图像的大小进行调整的过程。在Python中，图像缩放主要调用resize()函数实现。
dst=resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
(1)src表示原始图像
(2)dsize表示图像缩放的大小
(3)result表示图像结果
(4)fx表示图像x轴方向缩放大小的倍数
(5)fy表示图像y轴方向缩放大小的倍数
(6)interpolation表示变换方法。
CV_INTER_NN表示近邻插值；CV_INTER_LINEAR表示双线性插值（缺省使用）；
CV_INTER_AREA表示使用像素关系重采样，当图像缩小时，该方法可以避免波纹出现，当图像放大时，类似于CV_INTER_NN；
CV_INTER_CUBIC表示立方插值

常见图像缩放的两种方式如下所示
(1)result=cv2.resize(src,(160,160))
(2)result=cv2.resize(src,None,fx=0.5,fy=0.5)

'''

import cv2
import numpy as np

# img = cv2.imread('lena.jpg')
# result = cv2.resize(img, (200, 100))
#
# cv2.imshow('original', img)
# cv2.imshow('result', result)

# # 原始图像像素乘以缩放系数进行图像变换
# src = cv2.imread('lena.jpg')
# rows, cols = src.shape[:2]
# result = cv2.resize(src, (int(cols * 0.6), int(rows * 1.2)))
#
# cv2.imshow('src', src)
# cv2.imshow('result', result)

# (fx,fy)
src = cv2.imread('lena.jpg')
rows, cols = src.shape[:2]
print(rows, cols)

result = cv2.resize(src, None, fx=0.3, fy=0.3)
cv2.imshow('src', src)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
