'''

图像处理过程中常常需要用到灰度图像、二值图像、HSV(hue,saturation,value，色调，饱和度，明度)、
HIS(hue,saturation,intensity，色调，饱和度，强度)等。
常用类型有以下三种：
cv2.COLOR_BGR2GRAY
cv2.COLOR_BGR2RGB
cv2.COLOR_GRAY2BGR
dst=cvtColor(src, code, dst=None, dstCn=None)
(1)src表示输入图像，需要进行颜色空间变换的原图像
(2)code表示转换的代码或标识
(3)dst表示输出图像，其大小和深度与src一致
(4)dstCn表示目标图像通道数，其值为0时，由src和code决定。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# src = cv2.imread('lena.jpg')
# result1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# result2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# cv2.imshow('src', src)
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)

img_BGR = cv2.imread('lena.jpg')

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)  # BGR转换为RGB
img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)  # 灰度化处理
img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)  # BGR转HSV
img_YCrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)  # BGR转YCrCb
img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)  # BGR转HLS
img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)  # BGR转XYZ
img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)  # BGR转LAB
img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)  # BGR转YUV

titles = ['BGR', 'RGB', 'GRAY', 'HSV', 'YCrCb', 'HLS', 'XYZ', 'LAB', 'YUV']
images = [img_BGR, img_RGB, img_GRAY, img_HSV, img_YCrCb, img_HLS, img_XYZ, img_LAB, img_YUV]
for i in range(9):
	plt.subplot(3, 3, i + 1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()
