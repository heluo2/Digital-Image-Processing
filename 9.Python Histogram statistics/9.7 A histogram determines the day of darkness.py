'''

通过直方图判断一幅图像是黑夜或白天
常见的方法是通过计算图像的灰度平均值、灰度中值或灰度标准差，再与自定义的阈值进行对比，从而判断是黑夜还是白天
(1)灰度平均值：该值等于图像中所有像素灰度值之和除以图像的像素个数。
(2)灰度中值：对图像中所有像素灰度值进行排序，然后获取所有像素最中间的值。
(3)灰度标准差：又常称均方差，是离均方差平方的算术平均数的平方根。标准差能反映一个数据集的离散程度，是总体各单位标准值与其平均数离差平方的
算术平均数的平方根。如果一幅图看起来灰蒙蒙的，那灰度标准差就小；如果一幅图看起来很鲜艳，那对比度就很大，标准差也大。

一种用来判断图象是白天还是黑夜的办法，其基本步骤如下
(1)读取原始图像，转换为灰度图，并获取图像的所有像素值。
(2)设置灰度阈值并计算该阈值以下的像素个数。
(3)设置比例参数，对比该参数低于该阈值的像素占比，如果低于参数则预测为白天，高于参数则预测为黑夜。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# # 函数：获取图像的灰度平均值
# def fun_mean(img, height, width):
# 	sum_img = 0
# 	for i in range(height):
# 		for j in range(width):
# 			sum_img = sum_img + int(img[i, j])
# 	mean = sum_img / (height * width)
# 	return mean
#
#
# # 函数：获取中位数
# def fun_median(data):
# 	length = len(data)
# 	data.sort()
# 	if (length % 2) == 1:
# 		z = length // 2
# 		y = data[z]
# 	else:
# 		y = (int(data[length // 2]) + int(data[length // 2 - 1])) / 2
# 	return y
#
#
# img = cv2.imread('lena.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = grayImage.shape[0]
# width = grayImage.shape[1]
# # 计算图像的灰度平均值
# mean = fun_mean(grayImage, height, width)
# print(mean)
# # 计算图像的灰度中位数
# value = grayImage.ravel()
# median = fun_median(value)
# print(median)
#
# # 计算图像的灰度标准差
# std = np.std(value, ddof=1)
# print(std)

'''
判断黑夜白天
'''


def func_judge(img):
	height = img.shape[0]
	width = img.shape[1]
	piexs_sum = height * width
	dark_sum = 0
	dark_prop = 0

	for i in range(height):
		for j in range(width):
			if img[i, j] < 50:
				dark_sum += 1
	print(dark_sum)
	print(piexs_sum)
	dark_prop = dark_sum * 1.0 / piexs_sum
	if dark_prop >= 0.8:
		print('This picture is dark!', dark_prop)
	else:
		print('This picture is bright!', dark_prop)


img = cv2.imread('dark.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([grayImage], [0], None, [256], [0, 255])
func_judge(grayImage)

plt.subplot(121)
plt.imshow(img_rgb, 'gray')
plt.axis('off')
plt.title('(a)')
plt.subplot(122)
plt.plot(hist, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)')

plt.show()
