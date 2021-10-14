'''

1. 概述
量化(quantization)是将图像像素点对应亮度的连续变化区间转换为单个特定值的过程，即将原始灰度图像的空间坐标幅度值离散化。
量化等级越多，图像层次越丰富，灰度分辨率越高，图像的质量也越好；量化等级越少，图像层次欠丰富，灰度分辨率越低，会出现图像轮廓分层的现象，
降低图像的质量。
如果量化等级为2，将使用两种灰度级表示原始图像的像素（0~255），灰度小于128的取0，大于等于128的取128。
如果量化等级为4，则将使用四种灰度等级表示原始图像的像素，新图像将分层为四种颜色，0~64取0，64~128取64，128~192取128，192~255取192.
Python图像量化处理相关代码操作，核心流程是建立一幅临时图像，然后循环遍历原始图像中所有的像素点，判断每个像素点应该属于的量化等级，
最后将临时图像显示。

2. 操作
建立一幅临时图像，然后循环遍历原始图像中所有像素点，判断每个像素点应该属于的量化等级，最后将临时图像显示。

3. K-Means聚类量化处理
基于K-Means聚类算法的量化处理，它能够将彩色图像RGB像素点进行颜色分割和颜色量化。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('lena.jpg')
# # cv2的图像对象使用的是bgr, plt绘图显示图像对象使用的是 rgb
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# height = img.shape[0]
# width = img.shape[1]
#
# new_img1 = np.zeros((height, width, 3), np.uint8)
# new_img2 = np.zeros((height, width, 3), np.uint8)
# new_img3 = np.zeros((height, width, 3), np.uint8)
# # 图像量化等级为2的量化操作
# for i in range(height):
# 	for j in range(width):
# 		for k in range(3):
# 			if img[i, j][k] < 128:
# 				gray = 0
# 			else:
# 				gray = 128
# 			new_img1[i, j][k] = np.uint8(gray)
# # 图像量化等级为4的量化操作
# for i in range(height):
# 	for j in range(width):
# 		for k in range(3):
# 			if img[i, j][k] < 64:
# 				gray = 0
# 			elif img[i, j][k] < 128:
# 				gray = 64
# 			elif img[i, j][k] < 192:
# 				gray = 128
# 			else:
# 				gray = 192
# 			new_img2[i, j][k] = np.uint8(gray)
# # 图像量化等级为8的量化操作
# for i in range(height):
# 	for j in range(width):
# 		for k in range(3):
# 			if img[i, j][k] < 32:
# 				gray = 0
# 			elif img[i, j][k] < 64:
# 				gray = 32
# 			elif img[i, j][k] < 96:
# 				gray = 64
# 			elif img[i, j][k] < 128:
# 				gray = 96
# 			elif img[i, j][k] < 160:
# 				gray = 128
# 			elif img[i, j][k] < 192:
# 				gray = 160
# 			elif img[i, j][k] < 224:
# 				gray = 192
# 			else:
# 				gray = 224
# 			new_img3[i, j][k] = np.uint8(gray)
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
#
# titles = ['原始图像', '量化-L2', '量化-L4', '量化-L8']
# images = [img, new_img1, new_img2, new_img3]
# for i in range(4):
# 	plt.subplot(2, 2, i + 1)
# 	plt.imshow(images[i], 'gray')
# 	plt.title(titles[i])
# 	plt.xticks([])
# 	plt.yticks([])
# plt.show()

# K-Means聚类算法
img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 图像二位像素转换为一维像素
data = img.reshape((-1, 3))
data = np.float32(data)
# 定义中心(type,max_iter,epsilon)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 设置标签
flags = cv2.KMEANS_RANDOM_CENTERS
# K-Means聚类聚集成四类
compactness, labels, centers = cv2.kmeans(data, 4, None, criteria, 10, flags)
# 图像转换回uint8类型
centers = np.uint8(centers)
res = centers[labels.flatten()]
dst = res.reshape((img.shape))
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

titles = ['原始图像', '聚类量化K=4']
images = [img, dst]
for i in range(2):
	plt.subplot(1, 2, i + 1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()
