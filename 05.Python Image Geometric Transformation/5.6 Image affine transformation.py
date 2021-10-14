'''

图像仿射变换又称为图像仿射映射，是指在几何中，一个向量空间进行一次线性变换并接上一个平移，变换为另一个向量空间。
通常图像的旋转加拉伸就是图像仿射变换，仿射变换需要一个M矩阵实现，但是由于仿射变换比较复杂，很难找到这个M矩阵，
OpenCV提供了根据变换前后三个点的对应关系来自动求解M的函数cv2.getAffineTransform(src, dst)，输出结果为仿射矩阵M，
然后使用函数cv2.warpAffine()函数实现图像仿射变换。
M = cv2.getAffineTransform(pos1, pos2)
(1)pos1表示变换前的位置。
(2)pos2表示变换后的位置。
cv2.warpAffine(src,M,(cols, rows))
(1)src表示原始图像。
(2)M表示仿射变换矩阵。
(3)(cols, rows)表示比那桓侯的图像大小。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('lena.jpg')
rows, cols = src.shape[:2]
pos1 = np.float32([[50, 50], [200, 50], [50, 200]])
pos2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pos1, pos2)

result = cv2.warpAffine(src, M, (cols, rows))

cv2.imshow('original', src)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
