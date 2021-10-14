'''

1. 概述
图像采样(image sampling)处理是一幅连续图像在空间上分割成M×N个网格，每个网格用一个亮度值或灰度值来表示。
图像采样的间隔越大，所得图像像素数越少，空间分辨率越低，图像质量越差，甚至出现马赛克效应。
相反，图像采样的间隔越小，所得图像像素数越多，空间分辨率越高，图像质量越好，但数据量会相应地增大。
数字图像的质量很大程度上取决于量化和采样中所采用的灰度级和样本数。
现实生活中的图像，都需要经过离散化处理转换成数字图像，从而进行后续的计算机处理和图像识别等操作。

2. 操作
核心流程是建立一幅临时图像，设置需要采样的区域，然后循环遍历原始图像中所有像素点，采样区域内的像素点赋值相同，最终实现图像采样处理。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('scenery.jpg')
# height = img.shape[0]
# width = img.shape[1]
# # 采样转换成16×16区域
# numheight = int(height / 16)
# numwidth = int(width / 16)
#
# new_img = np.zeros((height, width, 3), np.uint8)
#
# # 图样循环采样16×16区域
# for i in range(16):
# 	y = i * numheight
# 	for j in range(16):
# 		x = j * numwidth
# 		c = img[y, x]
# 		b = img[y, x][0]
# 		g = img[y, x][1]
# 		r = img[y, x][2]
#
# 		for n in range(numheight):
# 			for m in range(numwidth):
# 				new_img[y + n, x + m][0] = np.uint8(b)
# 				new_img[y + n, x + m][1] = np.uint8(g)
# 				new_img[y + n, x + m][2] = np.uint8(r)
#
# cv2.imshow('src', img)
# cv2.imshow('src1', new_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
以上代码存在一个问题，当图像的长度和宽度不能被采样区域整除时，输出图像的最右边和最下边的区域没有被采样定理。
推荐进行求余运算，将不能整除部分的区域也进行相应的采样处理。
'''

img = cv2.imread('scenery.jpg')
height = img.shape[0]
width = img.shape[1]
print(height)
print(width)
# 采样转换成16×16区域
c = 17
numheight = int(height / c)
numwidth = int(width / c)

new_img = np.zeros((height, width, 3), np.uint8)

# 图样循环采样16×16区域
for i in range(c):
	y = i * numheight
	for j in range(c):
		x = j * numwidth
		b = img[y, x][0]
		g = img[y, x][1]
		r = img[y, x][2]

		if j == c - 1 and i != c - 1:
			for n in range(numheight):
				for m in range(x, width):
					new_img[y + n, m][0] = np.uint8(b)
					new_img[y + n, m][1] = np.uint8(g)
					new_img[y + n, m][2] = np.uint8(r)
		elif i == c - 1 and j != c - 1:
			for n in range(y, height):
				for m in range(numwidth):
					new_img[n, x + m][0] = np.uint8(b)
					new_img[n, x + m][1] = np.uint8(g)
					new_img[n, x + m][2] = np.uint8(r)
		elif j == c - 1 and i == c - 1:
			for n in range(y, height):
				for m in range(x, width):
					new_img[n, m][0] = np.uint8(b)
					new_img[n, m][1] = np.uint8(g)
					new_img[n, m][2] = np.uint8(r)
		else:
			for n in range(numheight):
				for m in range(numwidth):
					new_img[y + n, x + m][0] = np.uint8(b)
					new_img[y + n, x + m][1] = np.uint8(g)
					new_img[y + n, x + m][2] = np.uint8(r)

cv2.imshow('src', img)
cv2.imshow('src1', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
局部马赛克处理
'''

# img = cv2.imread('lena.jpg')
# # 设置单机鼠标开启
# en = False
#
#
# # 鼠标事件
# def draw(event, x, y, flags, param):
# 	global en
# 	# 单机鼠标开启en值
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		en = True
# 	# 单击鼠标并移动
# 	elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_LBUTTONDOWN:
# 		# 调用函数打马赛克
# 		if en:
# 			drawMask(y, x)
# 		# 单机鼠标弹起结束操作
# 		elif event == cv2.EVENT_LBUTTONUP:
# 			en = False
#
#
# # 图像局部采样处理
# def drawMask(x, y, size=20):
# 	# size×size采样处理
# 	m = int(x / size) * size
# 	n = int(y / size) * size
# 	print(m, n)
# 	# 10×10区域设置为同一像素
# 	for i in range(size):
# 		for j in range(size):
# 			img[m + i, n + j] = img[m, n]
#
#
# # 打开对话框
# cv2.namedWindow('image')
#
# # 调用draw函数设置鼠标操作
# cv2.setMouseCallback('image', draw)
#
# # 循环处理
# while (1):
# 	cv2.imshow('image', img)
# 	# 按esc键退出
# 	if cv2.waitKey(10) & 0xFF == 27:
# 		break
# 	# 按s键保存图片
# 	elif cv2.waitKey(10) & 0xFF == 115:
# 		cv2.imwrite('lena1.jpg', img)
#
# # 退出窗口
# cv2.destroyAllWindows()
