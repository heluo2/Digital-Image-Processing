'''

图像融合处理是指将两幅或两幅以上的图像信息融合到一幅图像上，融合的图像含有更多的信息，更方便人们观察或计算机处理。
图像融合是在图像加法的基础上增加了系数和亮度调节量，与图像加法的主要区别如下：
(1)图像加法：目标图像=图像1+图像2
(2)图像融合：目标图像=图像1×系数1+图像2×系数2+亮度调节量
在OpenCV种，图像融合主要调用addWeight()函数实现，两幅融合图像的像素大小必须一致，参数gamma不能省略
dst=addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
dst=src1*alpha+src2*beta+gamma

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

src1 = cv2.imread('lena.jpg')
src2 = cv2.imread('people.jpg')

result = cv2.addWeighted(src1, 0.6, src2, 0.8, 0)

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
