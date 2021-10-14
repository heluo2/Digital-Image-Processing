'''

图像镜像变换是图像旋转变换的一种特殊情况，通常包括垂直方向和水平方向的镜像。
在Python中主要调用OpenCV的flip()函数实现图像镜像变换
dst=flip(src, flipCode, dst=None)
(1)src表示原始图像。
(2)flipCode表示翻转方向，如果flipCode为0，则以x轴为对称轴翻转，如果flipCode>0，则以Y轴为对称轴翻转，如果flipCode<0，
则在x轴、y轴方向同时翻转。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img1 = cv2.flip(src, 0)  # 参数=0以x轴为对称翻转
img2 = cv2.flip(src, 1)  # 参数>0以y轴为对称翻转
img3 = cv2.flip(src, -1)  # 参数<0以x轴和y轴翻转

titles = ['img', 'img1', 'img2', 'img3']
images = [src, img1, img2, img3]
for i in range(4):
	plt.subplot(2, 2, i + 1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()
