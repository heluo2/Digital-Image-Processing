'''

图像阈值化(binarization)旨在剔除掉图像中一些低于或高于一定值的像素，从而提取图像中的物体，将图像的背景和噪声区分开。
图像阈值化可以理解为一个简单的图像分割操作，阈值又称为临界值，它的目的是确定出一个范围，然后这个范围内的像素点使用同一种方法处理，
而阈值之外的部分则使用另一种方法处理或保持原样。
灰度化处理后的图像，每个像素都只有一个灰度值，其大小表示明暗程度。阈值化处理可以将图像中的像素划分为两类颜色，常见的阈值化算法为
Gray(i,j)=255,Gray(i,j)>=T
Gray(i,j)=0,Gray(i,j)<T
当某个像素点的灰度Gray(i,j)小于阈值T时，其像素设置为0，表示黑色；当灰度Gray(i,j)大于或等于阈值T时，其像素值为255，表示白色。
在Python中的OpenCv库中，提供了固定阈值化函数threshold()和自适应阈值化函数adaptiveThreshold()，将一幅图像进行阈值化处理。

7.3.1固定阈值化处理
OpenCv中提供了函数threshold()实现固定阈值化处理
det=threshold(src, thresh, maxval, type, dst=None)
(1)src表示输入图像的数组，8位或32浮点类型的多通道数。
(2)thresh表示阈值
(3)maxval表示最大值，当参数阈值类型type选择cv2.THRESH_BINARY或cv2.THRESH_BINARY_INV时，该参数为阈值类型的最大值。
(4)type表示阈值类型
(5)dst表示输出的阈值化处理后的图像，其类型和通道数与src一致。
threshold(Gray, 127, 255, cv2.THRESH_BINARY)
大于阈值的像素点的灰度值设为最大值，小于阈值的像素点灰度值设定为0
threshold(Gray, 127, 255, cv2.THRESH_BINARY_INV)
大于阈值的像素点的灰度值设为0，小于阈值的像素点灰度值设定为255
threshold(Gray, 127, 255, cv2.THRESH_TRUNC)
小于阈值的像素点的灰度值不改变，反之将像素点的灰度值设定为该阈值
threshold(Gray, 127, 255, cv2.THRESH_TOZERO)
小于阈值的像素点的灰度值不改变，大于阈值的部分，将像素点的灰度值设定为0
threshold(Gray, 127, 255, cv2.THRESH_TOZERO_INV)
大于阈值的像素点的灰度值不改变，小于阈值的部分，将像素点的灰度值设定为0

1.二进制阈值化
该函数的原型为threshold(Gray, 127, 255, cv2.THRESH_BINARY)
其方法首先要选定一个特定的阈值量，如127，再按照如下所示的规则进行阈值化处理
dst(x,y)=max val,src(x,y)>thresh
dst(x,y)=0      ,src(x,y)<=thresh

2.反二进制阈值化
该函数的原型为threshold(Gray, 127, 255, cv2.THRESH_BINARY_INV)
其方法首先要选定一个特定的阈值量，如127，再按照如下所示的规则进行阈值化处理
dst(x,y)=0      ,src(x,y)>thresh
dst(x,y)=max val,src(x,y)<=thresh

3.截断阈值化
该函数的原型为threshold(Gray, 127, 255, cv2.THRESH_TRUNC)
图像中大于该阈值的像素点设定为该阈值，小于或等于该阈值的保持不变，如127
dst(x,y)=threshold,src(x,y)>thresh
dst(x,y)=src(x,y) ,src(x,y)<=thresh

4.阈值化为0
该函数的原型为threshold(Gray, 127, 255, cv2.THRESH_TOZERO)
dst(x,y)=src(x,y),src(x,y)>thresh
dst(x,y)=0       ,src(x,y)<=thresh
当前像素点的灰度值大于thresh阈值时，其像素点的灰度值保持不变；否则，像素点的灰度值设置为0。

5.反阈值化为0
该函数的原型为threshold(Gray, 127, 255, cv2.THRESH_TOZERO_INV)
dst(x,y)=0       ,src(x,y)>thresh
dst(x,y)=src(x,y),src(x,y)<=thresh
当前像素点的灰度值大于thresh阈值时，其像素点的灰度值设置为0；否则，像素点的灰度值保持不变。

7.3.2自适应阈值化处理
根据图像上的每一个小区域，计算与其对应的阈值，从而使得同一幅图像上的不同区域采用不同的阈值，在亮度不同的情况下得到更好的结果。
自适应阈值化处理在OpenCV中调用cv2.adaptiveThreshold()函数实现
dst=adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)
(1)src表示输入图像
(2)maxValue表示给像素赋值的满足条件的最大值
(3)adaptiveMethod表示要使用的自适应阈值算法，常见取值包括cv2.ADAPTIVE_THRESH_MEAN_C（阈值取邻域的平均值）
或cv2.ADAPTIVE_THRESH_GAUSSIAN_C（阈值取邻域的加权平均值，权重分布为一个高斯函数分布）
(4)thresholdType表示阈值类型，取值必须为THRESH_BINARY或THRESH_BINARY_INV
(5)blockSize表示计算阈值的像素邻域大小，取值为3、5、7等
(6)C表示一个常数，阈值等于平均值或者加权平均值减去这个常数
(7)dst表示输出的阈值化处理后的图像，其类型尺寸需与src一致。
当阈值类型为THRESH_BINARY时，其灰度图像转换为阈值化图像的计算公式为
dst(x,y)=maxValue,src>T(x,y)
dst(x,y)=0       ,src<=T(x,y)
其灰度图像转换为阈值化处理图像的计算公式：
dst(x,y)=        0,src>T(x,y)
dst(x,y)=maxValue,src<=T(x,y)

dst(x,y)为阈值化处理后的灰度值，T(x,y)为计算每个单独像素的阈值，其取值如下
(1)当adaptiveThreshold参数采用ADAPTIVE_THRESH_MEAN_C时，阈值T(x,y)为blockSize×blockSize
邻域内(x,y)减去参数C的平均值
(2)当adaptiveThreshold参数采用ADAPTIVE_THRESH_GAUSSIAN_C时，阈值T(x,y)为blockSize×blockSize
邻域内(x,y)减去参数C与高斯窗口交叉相关的加权总和。

'''

import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# src = cv2.imread('miao.jpg')
# Gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# # # 二进制阈值化处理
# # r, b = cv2.threshold(Gray, 127, 255, cv2.THRESH_BINARY)
#
# # # 反二进制阈值化
# # r, b = cv2.threshold(Gray, 127, 255, cv2.THRESH_BINARY_INV)
#
# # # 截断阈值化处理
# # r, b = cv2.threshold(Gray, 127, 255, cv2.THRESH_TRUNC)
#
# # # 阈值化为0处理
# # r, b = cv2.threshold(Gray, 127, 255, cv2.THRESH_TOZERO)
#
# # 反阈值化为0
# r, b = cv2.threshold(Gray, 127, 255, cv2.THRESH_TOZERO_INV)
#
# cv2.imshow('src', src)
# cv2.imshow('result', b)
# cv2.waitKey(0)
# cv2.destroyWindow()

'''
五种固定阈值化处理对比结果
'''
# img = cv2.imread('miao.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh1 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_TOZERO_INV)
#
# titles = ['(a)Gray Image', '(b)BINARY', '(c)BINARY_INV', '(d)TRUNC', '(e)TOZERO', '(f)TOZERO_INV']
# images = [grayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
# 	plt.subplot(2, 3, i + 1)
# 	plt.imshow(images[i], 'gray')
# 	plt.title(titles[i])
# 	plt.xticks()
# 	plt.yticks()
# plt.show()

'''
自适应阈值化处理
'''
img = cv2.imread('miao.jpg')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 固定值阈值化处理
r, thresh1 = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

# 自适应阈值化处理1
thresh2 = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# 自适应阈值化处理2
thresh3 = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
titles = ['(a)灰度图像', '(B)全局阈值', '(C)自适应平均阈值', '(D)自适应高斯阈值']
images = [grayImage, thresh1, thresh2, thresh3]
for i in range(4):
	plt.subplot(2, 2, i + 1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks()
	plt.yticks()
plt.show()
