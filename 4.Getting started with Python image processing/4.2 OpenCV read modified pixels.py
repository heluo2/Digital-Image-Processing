'''

OpenCV读取图像的像素值可以直接通过遍历图像的位置实现，如果是灰度图像则返回其灰度值，如果是彩色图像则返回B、G、R三个分量值。
灰度图像：返回值=图像[位置参数]
彩色图像：返回值=图像[位置元素，0|1|2]获取BGR三个通道像素

Numpy库读取像素和修改像素
读取像素调用item()函数实现，修改像素调用itemset()函数实现。
返回值=图像.item(位置参数)
图像.itemset(位置，新值)

'''

import cv2
import numpy as np

# 读取图像
img = cv2.imread('lena.jpg')

# # 读取像素
# test = img[88, 142]
# print('读取的像素值：', test)

# # 修改像素
# # img[88, 142] = [255, 255, 255]  # 单点像素
# img[100:300, 150:350] = [255, 255, 255]  # 区域
# # print('修改后的像素值：', test)
#
# # 分别获取RGB通道像素
# blue = img[88, 142, 0]
# green = img[88, 142, 1]
# red = img[88, 142, 2]
# print('蓝色分量', blue)
# print('绿色分量', green)
# print('红色分量', red)
#
# # 显示图像
# cv2.imshow('demo', img)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Numpy读取像素
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 1))

# Numpy修改像素
img.itemset((78, 100, 0), 100)
img.itemset((78, 100, 1), 100)
img.itemset((78, 100, 1), 100)
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 1))
