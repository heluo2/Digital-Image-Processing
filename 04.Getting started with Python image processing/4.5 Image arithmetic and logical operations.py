'''

图像的算法运算和逻辑运算包括图像的加法运算、图像减法运算、图像与运算、图像或运算、图像异或运算、图像非运算
1. 图像加法运算
主要有两种方法。第一种调用Numpy库实现，目标图像像素为两幅图像的像素之和。第二种是通过OpenCV调用add()函数实现。
dst=add(src1, src2, dst=None, mask=None, dtype=None)
(1)src1表示第一幅图的像素矩阵
(2)src2表示第二幅图的像素矩阵
(3)dst表示输出的图像，必须与输入图像具有相同大小和通道数
(4)mask表示可选操作掩码（8位单通道数组），用于指定要更改的输出数组的元素
(5)dtype表示输出数组的可选深度
当两幅图的像素值相加结果小于等于255时，输出图像直接赋值该结果，如果相加值大于255，则输出图像的像素结果设置为255

2. 图像减法运算
图像减法运算主要调用subtract()函数实现
dst=subtract(src1, src2, dst=None, mask=None, dtype=None)
(1)src1表示第一幅图的像素矩阵
(2)src2表示第二幅图的像素矩阵
(3)dst表示输出的图像，必须与输入图像具有相同大小和通道数
(4)mask表示可选操作掩码（8位单通道数组），用于指定要更改的输出数组的元素
(5)dtype表示输出数组的可选深度

3. 图像与运算
图像与运算是指两幅图像（灰度图像或彩色图像均可）的每个像素值进行二进制与操作，实现图像裁剪。
dst=bitwise_and(src1, src2, dst=None, mask=None)
(1)src1表示第一幅图的像素矩阵
(2)src2表示第二幅图的像素矩阵
(3)dst表示输出的图像，必须与输入图像具有相同大小和通道数
(4)mask表示可选操作掩码（8位单通道数组），用于指定要更改的输出数组的元素

4. 图像或运算
图像与运算是指两幅图像（灰度图像或彩色图像均可）的每个像素值进行二进制与操作，实现图像裁剪。
dst=bitwise_or(src1, src2, dst=None, mask=None)
(1)src1表示第一幅图的像素矩阵
(2)src2表示第二幅图的像素矩阵
(3)dst表示输出的图像，必须与输入图像具有相同大小和通道数
(4)mask表示可选操作掩码（8位单通道数组），用于指定要更改的输出数组的元素

5. 图像异或运算
如果两个值不相同你，则异或结果为1，如果两个值相同，则异或结果为0。
图像与运算是指两幅图像（灰度图像或彩色图像均可）的每个像素值进行二进制与操作，实现图像裁剪。
dst=bitwise_xor(src1, src2, dst=None, mask=None)
(1)src1表示第一幅图的像素矩阵
(2)src2表示第二幅图的像素矩阵
(3)dst表示输出的图像，必须与输入图像具有相同大小和通道数
(4)mask表示可选操作掩码（8位单通道数组），用于指定要更改的输出数组的元素

6. 图像非运算
图像非运算就是图像的像素反色处理。
dst=bitwise_not(src1, src2, dst=None, mask=None)
(1)src1表示第一幅图的像素矩阵
(2)src2表示第二幅图的像素矩阵
(3)dst表示输出的图像，必须与输入图像具有相同大小和通道数
(4)mask表示可选操作掩码（8位单通道数组），用于指定要更改的输出数组的元素

'''

import cv2
import numpy as np

# img = cv2.imread('lena.jpg')

# # 图像加法运算
# m = np.ones(img.shape, dtype='uint8') * 100
# result = cv2.add(img, m)
#
# cv2.imshow('original', img)
# cv2.imshow('result', result)

# # 图像减法运算
# m = np.ones(img.shape, dtype='uint8') * 100
# result = cv2.subtract(img, m)
#
# cv2.imshow('original', img)
# cv2.imshow('result', result)

# # 图像与运算
# img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
#
# rows, cols = img.shape[:2]
# print(rows, cols)
#
# circle = np.zeros((rows, cols), dtype='uint8')
# x = int(rows / 2)
# y = int(cols / 2)
# cv2.circle(circle, (x, y), 80, 255, -1)
# print(circle.shape)
# print(img.size, circle.size)
#
# result = cv2.bitwise_and(img, circle)
# cv2.imshow('original', img)
# cv2.imshow('circle', circle)
# cv2.imshow('result', result)

# # 图像或运算
# img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
#
# rows, cols = img.shape[:2]
# print(rows, cols)
#
# circle = np.zeros((rows, cols), dtype='uint8')
# x = int(rows / 2)
# y = int(cols / 2)
# cv2.circle(circle, (x, y), 80, 255, -1)
# print(circle.shape)
# print(img.size, circle.size)
#
# result = cv2.bitwise_or(img, circle)
# cv2.imshow('original', img)
# cv2.imshow('circle', circle)
# cv2.imshow('result', result)

# # 图像异或运算
# img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
#
# rows, cols = img.shape[:2]
# print(rows, cols)
#
# circle = np.zeros((rows, cols), dtype='uint8')
# x = int(rows / 2)
# y = int(cols / 2)
# cv2.circle(circle, (x, y), 80, 255, -1)
# print(circle.shape)
# print(img.size, circle.size)
#
# result = cv2.bitwise_xor(img, circle)
# cv2.imshow('original', img)
# cv2.imshow('circle', circle)
# cv2.imshow('result', result)

# 图像非运算
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

result = cv2.bitwise_not(img)
cv2.imshow('original', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
