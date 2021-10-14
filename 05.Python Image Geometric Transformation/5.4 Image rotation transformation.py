'''

图像旋转是指图像以某一点为中心旋转一定的角度，形成一幅新的图像的过程。
图像旋转变换会有一个旋转中心，这个旋转中心一般为图像的中心，旋转之后图像的大小一般会发生改变。
图像旋转变换主要调用getRotationMatrix2D()函数和warpAffine()函数实现
M=getRotationMatrix2D(center, angle, scale)
(1)center表示旋转中心点，通常设置为(cols/2,rows/2)
(2)angle表示旋转角度，正值表示逆时针旋转，坐标原点被定为左上角
(3)scale表示比例因子
rotated=cv2.warpAffine(src,M,(cols, rows))
(1)src表示原始图像
(2)M表示旋转参数，即getRotationMatrix2D()函数定义的结果
(3)(cols, rows)表示原始图像的宽度和高度

'''

import cv2
import numpy as np

src = cv2.imread('lena.jpg')
# 原始图像的高、宽以及通道数
rows, cols, channel = src.shape
# 绕图像的中心旋转
# 函数参数：旋转中心 旋转度数 scale
# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -90, 1)
# 函数参数：原始图像 旋转参数 元素图像宽高
rotated = cv2.warpAffine(src, M, (cols, rows))

cv2.imshow('src', src)
cv2.imshow('rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
