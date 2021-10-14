'''

图像灰度化是将一幅彩色图像转换为灰度化图像的过程。彩色图像通常包括R、G、B三个分量，分别显示出红绿蓝等各种颜色，灰度化就是使彩色图像
的R、G、B三个分量相等的过程。灰度图像中每个像素仅具有一种样本颜色，其灰度是位于黑色与白色之间的多级色彩深度，灰度值大的像素点比较亮，
反之比较暗，像素值最大为255（表示白色），像素值最小为0（表示黑色）。
假设某点的颜色由RGB组成，常见的灰度处理算法如下：
最大值灰度处理：Gray=max(R,G,B)
浮点灰度处理：Gray=R×0.3+G×0.59+B×0.11
整数灰度处理：Gray=(R×30+G×59+B×11)/100
移位灰度处理：Gray=(R×28+G×151+B×77)>>8
平均灰度处理：Gray=(R+G+B)/3
加权平均灰度处理：Gray=R×0.299+G×0.587+B×0.144

1.基于OpenCV的图像灰度化处理
我们看到大多数彩色图像都是RGB类型，但是在图像处理过程中，常常需要用到灰度图像、二值图像、HSV、HSI等，OpenCV提供了cvtColor()函数
dst=cvtColor(src, code, dst=None, dstCn=None)
(1)src表示输入图像，需要进行颜色空间变换的原图像
(2)code表示转换的代码或标识
(3)dst表示输出图像，其大小和深度与src一致
(4)dstCn表示目标图像通道数，其值为0时，由src和code决定。
该函数的作用是将一个图像从一个颜色空间转换到另一个颜色空间，其中，RGB是指Red、Green和Blue，一幅图像由这三个通道构成；
Gray表示只有一个灰度值一个通道；
HSV包含色调、饱和度和明度三个通道。

2.基于像素操作的图像灰度化处理
(1)最大值灰度处理方法
该方法的灰度值等于彩色图像R、G、B三个分量中的最大值，公式为
gray(i,j)=max(R(i,j),G(i,j),B(i,j))

(2)平均灰度化处理方法
该方法的灰度值等于彩色图像R、G、B三个分量灰度值的求和平均值，公式为
gray(i,j)=(R(i,j)+G(i,j)+B(i,j))/3

(3)加权平均灰度处理方法
该方法根据色彩重要性，将三个分量以不同的权值进行加权平均。由于人眼对绿色的敏感度最高，对蓝色的敏感度最低，因此，对RGB三分量进行加权平均
得到较为合理的灰度图像。
gray(i,j)=0.30×R(i,j)+0.59×G(i,j)+0.11×B(i,j)

7.2.1图像的灰度线性变换
图像的灰度线性变换是通过建立灰度，从而改善图像的质量，凸显图像的细节，提高图像的对比度。灰度线性变换的计算公式为
Db=f(Da)=αDa+b
式中，Db为灰度线性变换后的灰度值，Da为变换前输入图像的灰度值，α和b为线性变换方程f(D)的参数，分别表示斜率和截距。
(1)当α=1，b=0时，保持原始图像。
(2)当α=1，b！=0时，图像所有的灰度值上移或下移。
(3)当α=-1，b=255时，原始图像的灰度值反转。
(4)当α>1时，输出图像的对比度增强。
(5)当0<α<1时，输出图像的对比度减小。
(6)当α<0时，原始图像暗区域变亮，亮区域变暗，图像求补。

1.图像灰度上移变换：Db=Da+50
2.图像对比度增强变换：Db=Da×1.5
3.图像对比度减弱变换：Db=Da×0.8
4.图像灰度反色变换：Db=255-Da

7.2.2图像的灰度非线性变换
1.图像灰度非线性变换
原始图像的灰度值按照Db=Da×Da/255的公式进行非线性变换
2.图像灰度对数变换
图像灰度的对数变换一般表示为Db=c×log(1+Da)
式中，c为尺度比较常数，Da为原始图像灰度值，Db为变换后的目标灰度值。
由于对数曲线在像素较低的区域斜率大，在像素较高的区域斜率小，所以图像经过对数变换后，较暗区域的对比度将有所提升。
这种变换可用于增强图像的暗部细节，从而用来扩展被压缩的高值图像中的较暗像素。
对数变换实现了扩展低灰度值而压缩高灰度值的效果，广泛地应用于频谱图象的显示中。一个典型的应用是傅里叶频谱，其动态范围宽达0~10^6.
直接显示频谱时，图像显示设备的动态范围往往不能满足要求，从而丢失大量的暗部细节；
而使用对数变换后，图像的动态范围被合理地非线性压缩，从而可以清晰显示。
3.图像灰度伽马变换
伽马变换又称为指数变换或幂次变换，是另一种常用的灰度非线性变换。图像灰度伽马变换一般表示为：
Db=c×Da^γ
(1)当γ>1时，会拉伸图像中灰度级较高的区域，压缩灰度级较低的部分。
(2)当γ<1时，会拉伸图像中灰度级较低的区域，压缩灰度级较高的部分。
(3)当γ=1时，该灰度变换是线性的，此时通过线性方式改变原图像。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
1.基于OpenCV的图像灰度化处理
'''
# src = cv2.imread('miao.jpg')
# # result = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# result = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#
# cv2.imshow('src', src)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img_BGR = cv2.imread('miao.jpg')
#
# img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)  # BGR转换为RGB
# img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)  # 灰度化处理
# img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)  # BGR转HSV
# img_YCrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)  # BGR转YCrCb
# img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)  # BGR转HLS
# img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)  # BGR转XYZ
# img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)  # BGR转LAB
# img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)  # BGR转YUV
#
# titles = ['BGR', 'RGB', 'GRAY', 'HSV', 'YCrCb', 'HLS', 'XYZ', 'LAB', 'YUV']
# images = [img_BGR, img_RGB, img_GRAY, img_HSV, img_YCrCb, img_HLS, img_XYZ, img_LAB, img_YUV]
# for i in range(9):
# 	plt.subplot(3, 3, i + 1)
# 	plt.imshow(images[i], 'gray')
# 	plt.title(titles[i])
# 	plt.xticks([])
# 	plt.yticks([])
# plt.show()

'''
最大值灰度图像处理方法
'''
# img = cv2.imread('miao.jpg')
# height = img.shape[0]
# width = img.shape[1]
# result = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = max(img[i, j][0], img[i, j][1], img[i, j][2])
# 		result[i, j] = np.uint8(gray)
#
# cv2.imshow('src', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
平均灰度化处理方法
'''
# img = cv2.imread('miao.jpg')
# height = img.shape[0]
# width = img.shape[1]
# result = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = (int(img[i, j][0]) + int(img[i, j][1]) + int(img[i, j][2])) / 3
# 		result[i, j] = np.uint8(gray)
#
# cv2.imshow('src', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
加权平均灰度处理方法
'''
# img = cv2.imread('miao.jpg')
# height = img.shape[0]
# width = img.shape[1]
# result = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = 0.30 * img[i, j][0] + 0.59 * img[i, j][1] + 0.11 * img[i, j][2]
# 		result[i, j] = np.uint8(gray)
#
# cv2.imshow('src', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
1.图像灰度上移变换：Db=Da+50
'''
# img = cv2.imread('miao.jpg')
# result1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = result1.shape[0]
# width = result1.shape[1]
# result2 = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		if int(result1[i, j] + 50) > 255:
# 			gray = 255
# 		else:
# 			gray = int(result1[i, j] + 50)
# 		result2[i, j] = np.uint8(gray)
#
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
2.图像对比度增强变换：Db=Da×1.5
'''
# img = cv2.imread('miao.jpg')
# result1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = result1.shape[0]
# width = result1.shape[1]
# result2 = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		if int(result1[i, j] * 1.5) > 255:
# 			gray = 255
# 		else:
# 			gray = int(result1[i, j] * 1.5)
# 		result2[i, j] = np.uint8(gray)
#
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
3.图像对比度减弱变换：Db=Da×0.8
'''
# img = cv2.imread('miao.jpg')
# result1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = result1.shape[0]
# width = result1.shape[1]
# result2 = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		if int(result1[i, j] * 0.8) > 255:
# 			gray = 255
# 		else:
# 			gray = int(result1[i, j] * 0.8)
# 		result2[i, j] = np.uint8(gray)
#
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
4.图像灰度反色变换：Db=255-Da
'''
# img = cv2.imread('1.jpg')
# result1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = result1.shape[0]
# width = result1.shape[1]
# result2 = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = 255 - result1[i, j]
# 		result2[i, j] = np.uint8(gray)
#
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
1.图像灰度非线性变换
'''
# img = cv2.imread('miao.jpg')
# result1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height = result1.shape[0]
# width = result1.shape[1]
# result2 = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
# 	for j in range(width):
# 		gray = int(int(result1[i, j]) * int(result1[i, j]) / 255)
# 		result2[i, j] = np.uint8(gray)
#
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
2.图像灰度对数变换
'''

# def log_plot(c):
# 	x = np.arange(0, 256, 0.01)
# 	y = c * np.log(1 + x)
# 	plt.plot(x, y, 'r', linewidth=1)
# 	plt.rcParams['font.sans-serif'] = ['SimHei']
# 	plt.title('对数变换函数')
# 	plt.xlabel('x')
# 	plt.ylabel('y')
# 	plt.xlim(0, 255)
# 	plt.ylim(0, 255)
# 	plt.show()
#
#
# def log(c, img5):
# 	output1 = c * np.log(1.0 + img5)
# 	output1 = np.uint8(output1 + 0.5)
# 	return output1
#
#
# img = cv2.imread('2.jpg')
# log_plot(42)
# output = log(42, img)
#
# cv2.imshow('result1', img)
# cv2.imshow('result2', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
3.图像灰度伽马变换
'''


def gamma_plot(c, v):
	x = np.arange(0, 256, 0.01)
	y = c * x ** v
	plt.plot(x, y, 'r', linewidth=1)
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.title('伽马变换函数')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.xlim(0, 255)
	plt.ylim(0, 255)
	plt.show()


def gamma(img, c, v):
	lut = np.zeros(256, dtype=np.float32)
	for i in range(256):
		lut[i] = c * i ** v
	output_img = cv2.LUT(img, lut)  # 像素灰度值的映射
	output_img = np.uint8(output_img + 0.5)
	return output_img


img = cv2.imread('miao.jpg')
gamma_plot(0.00000005, 4.0)
output = gamma(img, 0.00000005, 4.0)
cv2.imshow('imput', img)
cv2.imshow('output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
