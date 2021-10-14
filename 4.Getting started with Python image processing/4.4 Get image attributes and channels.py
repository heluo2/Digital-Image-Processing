'''

4.4.1图像属性
图像最常见的属性包括三个：图像形状(shape)、像素大小(size)和图像类型(dtype)。
1.shape
通过shape关键字获取图像的形状，返回包括行数、列数、通道数的元组。其中灰度图像返回行数和列数，彩色图像返回行数、列数和通道数。
2.size
通过size关键字获取图像的大小，其中灰度图像返回行数×列数，彩色图像返回行数×列数×通道数。
3.dtype
通过关键字dtype获取图像的数据类型，通常返回uint8.

4.4.2图像通道处理
OpenCV通过split()函数和merge()函数实现对图像通道的处理。
图像通道处理包括通道分离和通道合并。
1.split()函数
OpenCV读取的彩色图像由蓝色(B)、绿色(G)、红色(R)三原色组成，每一种颜色可以认为是一个通道分量。
split()函数用于将一个多通道数组分离成三个单通道
split(m, mv=None)
1）m表示输入的多通道数组
2）mv表示输出的数组或vector容器

2.merge()函数
该函数是split()函数的逆向操作，将多个数组合成一个通道的数组，从而实现图像通道的合并。

'''

import cv2
import numpy
import numpy as np

img = cv2.imread('lena.jpg')

# 分离通道
# print(img.shape)  # 图像形状
# print(img.size)  # 像素大小
# print(img.dtype)  # 图像的数据类型
# cv2.imshow('demo', img)

# b, g, r = cv2.split(img)
# cv2.imshow('B', b)
# cv2.imshow('G', g)
# cv2.imshow('R', r)

# 合并通道
# b, g, r = cv2.split(img)
# m = cv2.merge([b, g, r])
# cv2.imshow('merge', m)

rows, cols, chn = img.shape
b = cv2.split(img)[0]
g = np.zeros((rows, cols), dtype=img.dtype)
r = np.zeros((rows, cols), dtype=img.dtype)
m = cv2.merge([b, g, r])
cv2.imshow('demo', m)

cv2.waitKey(0)
cv2.destroyAllWindows()
