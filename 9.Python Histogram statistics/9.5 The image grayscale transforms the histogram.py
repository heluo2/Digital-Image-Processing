'''

结合直方图分别对比图象灰度变换前后的变化
1.灰度上移变换图像直方图对比
图像灰度上移变换使用的表达式为Db=Da+50，该算法将实现图像灰度值的上移，从而提升图像的亮度。
2.灰度减弱图像直方图对比
该算法将减弱图像的对比度，使用的表达式为Db=Da×0.8
3.图像反色变换直方图对比
该算法将图像的颜色反色，对原图像的像素值进行反转，即黑色变为白色，白色变为黑色，使用的表达式为Db=255-Da
4.图像对数变换直方图对比
该算法将增加低灰度区域的对比度，从而增强暗部的细节，使用的表达式为Db=c×log(1+Da)
5.图像阈值化处理直方图对比
该算法原型threshold(grayImage, 127, 255, cv2.THRESH_BINARY),大于阈值的像素点的灰度值设为最大值，小于阈值的像素点灰度值设定为0

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
1.灰度上移变换图像直方图对比
'''
# img = cv2.imread('lena.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = grayImage.shape[0]
# width = grayImage.shape[1]
# result = np.zeros((height, width), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		if int(grayImage[i, j] + 50) > 255:
# 			gray = 255
# 		else:
# 			gray = int(grayImage[i, j] + 50)
# 		result[i, j] = np.uint8(gray)
#
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# hist_res = cv2.calcHist([result], [0], None, [256], [0, 255])
#
# plt.figure(figsize=(8, 6))
# plt.subplot(221)
# plt.imshow(img, 'gray')
# plt.title('(a)')
# plt.axis('off')
#
# plt.subplot(222)
# plt.plot(hist)
# plt.title('(b)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.subplot(223)
# plt.imshow(result, 'gray')
# plt.title('(c)')
# plt.axis('off')
#
# plt.subplot(224)
# plt.plot(hist_res)
# plt.title('(d)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.show()

'''
2.灰度减弱图像直方图对比
'''
# img = cv2.imread('lena.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = grayImage.shape[0]
# width = grayImage.shape[1]
# result = np.zeros((height, width), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = int(grayImage[i, j] * 0.8)
# 		result[i, j] = np.uint8(gray)
#
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# hist_res = cv2.calcHist([result], [0], None, [256], [0, 255])
#
# plt.figure(figsize=(8, 6))
# plt.subplot(221)
# plt.imshow(img, 'gray')
# plt.title('(a)')
# plt.axis('off')
#
# plt.subplot(222)
# plt.plot(hist)
# plt.title('(b)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.subplot(223)
# plt.imshow(result, 'gray')
# plt.title('(c)')
# plt.axis('off')
#
# plt.subplot(224)
# plt.plot(hist_res)
# plt.title('(d)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.show()

'''
3.图像反色变换直方图对比
'''
# img = cv2.imread('lena.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = grayImage.shape[0]
# width = grayImage.shape[1]
# result = np.zeros((height, width), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = 255 - grayImage[i, j]
# 		result[i, j] = np.uint8(gray)
#
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# hist_res = cv2.calcHist([result], [0], None, [256], [0, 255])
#
# plt.figure(figsize=(8, 6))
# plt.subplot(221)
# plt.imshow(img, 'gray')
# plt.title('(a)')
# plt.axis('off')
#
# plt.subplot(222)
# plt.plot(hist)
# plt.title('(b)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.subplot(223)
# plt.imshow(result, 'gray')
# plt.title('(c)')
# plt.axis('off')
#
# plt.subplot(224)
# plt.plot(hist_res)
# plt.title('(d)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.show()

'''
4.图像对数变换直方图对比
'''
# img = cv2.imread('lena.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = grayImage.shape[0]
# width = grayImage.shape[1]
# result = np.zeros((height, width), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = 42 * np.log(1.0 + grayImage[i, j])
# 		result[i, j] = np.uint8(gray)
#
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# hist_res = cv2.calcHist([result], [0], None, [256], [0, 255])
#
# plt.figure(figsize=(8, 6))
# plt.subplot(221)
# plt.imshow(img, 'gray')
# plt.title('(a)')
# plt.axis('off')
#
# plt.subplot(222)
# plt.plot(hist)
# plt.title('(b)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.subplot(223)
# plt.imshow(result, 'gray')
# plt.title('(c)')
# plt.axis('off')
#
# plt.subplot(224)
# plt.plot(hist_res)
# plt.title('(d)')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.show()

'''
5.图像阈值化处理直方图对比
'''
img = cv2.imread('lena.jpg')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
r, result = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_res = cv2.calcHist([result], [0], None, [256], [0, 255])

plt.figure(figsize=(8, 6))
plt.subplot(221)
plt.imshow(img, 'gray')
plt.title('(a)')
plt.axis('off')

plt.subplot(222)
plt.plot(hist)
plt.title('(b)')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(223)
plt.imshow(result, 'gray')
plt.title('(c)')
plt.axis('off')

plt.subplot(224)
plt.plot(hist_res)
plt.title('(d)')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
