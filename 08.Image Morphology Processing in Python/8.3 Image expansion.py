'''

图像膨胀是腐蚀操作的逆操作，类似于”领域扩张“，它将图像中高亮区域或白色部分进行扩张，其运行结果比原图的高亮区域更大。
用B对图像A进行膨胀处理，其中B是一个卷积模板，其形状为正方形或圆形，通过模板B与图像A进行卷积计算，扫描图像中的每一个像素点，
用模板元素与二值图像元素做与运算，如果都为0，那么目标像素点为0，否则为1。
从而计算B覆盖区域的像素最大值，并用该值 替换参考点的像素值实现图像膨胀。
图象被腐蚀处理后，将去除噪声，但同时会压缩图像，而图像膨胀操作可以去除噪声并保持原有形状。
在Python中，主要调用OpenCV的dilate()函数实现图像膨胀。
dst=dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
(1)src表示原始图像
(2)kernel表示卷积核
(3)iterations表示迭代次数，默认值为1，表示进行一次膨胀操作。
可以采用函数numpy.ones()创建卷积核

'''

import cv2
import numpy as np

src = cv2.imread('test02.png', cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
# 图像膨胀处理
erosion = cv2.dilate(src, kernel)

cv2.imshow('src', src)
cv2.imshow('result', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
