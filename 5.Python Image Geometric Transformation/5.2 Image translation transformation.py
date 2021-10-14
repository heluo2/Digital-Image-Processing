'''

图像平移是将图像中的所有像素点按照给定的平移量进行水平或垂直方向上的移动。
shifted=warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None)
(1)src表示原始图像
(2)M表示平移矩阵
M=np.float32([[1,0,x],[0,1,y])
x表示水平平移量，y表示垂直平移量
(3)dsize表示变换后的输出图像的尺寸大小
(4)dst表示输出图像，其大小为dsize，类型与src相同
(5)flags表示插值方法的组合和可选值。
(6)borderMode表示像素外推法，当borderMode=BORDER_TRANSPARENT时，表示目标图像中的像素不会修改原图像中的“异常值”
(7)borderValue用于边界不变的情况，默认情况下为0

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# src = cv2.imread('lena.jpg')
#
# M = np.float32([[1, 0, 100], [0, 1, 50]])
#
# rows, cols = src.shape[:2]
# result = cv2.warpAffine(src, M, (cols, rows))
#
# cv2.imshow('original', src)
# cv2.imshow('result', result)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread('lena.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

M = np.float32([[1, 0, 0], [0, 1, 100]])
img1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
M = np.float32([[1, 0, 0], [0, 1, -100]])
img2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
M = np.float32([[1, 0, 100], [0, 1, 0]])
img3 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
M = np.float32([[1, 0, -100], [0, 1, 0]])
img4 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

titles = ['Image1', 'Image2', 'Image3', 'Image4']
images = [img1, img2, img3, img4]
for i in range(4):
	plt.subplot(2, 2, i + 1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()
