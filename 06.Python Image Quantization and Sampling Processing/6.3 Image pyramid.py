'''

图像金字塔是指由一组图像且不同分辨率的子图集合，它是图像多尺度表达的一种，以多分辨率来解释图像的结构，主要用于图像的分割或压缩。
一幅图像的金字塔是一系列以金字塔型状排列的分辨率逐步降低，且来源于同一幅原始图像的图像集合。
生成图像金字塔主要包括两种方式：向下取样、向上取样。
图像分辨率不断降低的过程称为向下取样，图像分辨率不断增大的过程称为向上取样。

1. 图像向下取样
在图像向下取样中，使用最多的是高斯金字塔。它将对图像进行高斯核卷积，并删除原图中所有的偶数行和列，最终缩小图像。
其中，高斯核卷积运算就是对整幅图像进行加权平均的过程，每一个像素的值，都由其本身和邻域内的其他像素值（权重不同）经过加权平均后得到。
高斯核卷积让临近中心的像素点具有更高的重要度，对周围像素计算加权平均值。
原始图像Gi具有M×N像素，进行向下取样之后，所得到的图像Gi+1具有M/2×N/2像素，只有原图的四分之一。通过对输入的原始图像不停迭代，
就会得到整个金字塔。注意，由于每次向下采样会删除偶数行和列，所以它会不停地丢失图像的信息。
在OpenCV中，向下取样使用的函数为pyrDown()，其原型如下所示。
dst=pyrDown(src, dst=None, dstsize=None, borderType=None)
(1)src表示输入图像
(2)dst表示输出图像，与输入图像具有一样的尺寸和类型
(3)dstsize表示输出图像的大小，默认值为Size()
(4)boderType表示像素外推法

2. 图像向上取样
图像向上取样是由小图像不断放大图像的过程。它将图像在每个方向上扩大为原图像的两倍，新增的行和列均用0来填充，并使用与向下取样相同的卷积核
乘以4，再与放大后的图像进行卷积运算，以获得新增像素的新值。
注意，向上取样放大后的图像比原始图像要模糊。同时，向上取样和向下取样不是互逆的操作，经过两种操作后，是无法恢复原始图像的。
在OpenCV中，向下取样使用的函数为pyrUp()，其原型如下所示。
dst=pyrUp(src, dst=None, dstsize=None, borderType=None)
(1)src表示输入图像
(2)dst表示输出图像，与输入图像具有一样的尺寸和类型
(3)dstsize表示输出图像的大小，默认值为Size()
(4)boderType表示像素外推法

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('lena.jpg')
# r1 = cv2.pyrDown(img)
# r2 = cv2.pyrDown(r1)
# r3 = cv2.pyrDown(r2)
#
# cv2.imshow('original', img)
# cv2.imshow('PyrDown1', r1)
# cv2.imshow('PyrDown2', r2)
# cv2.imshow('PyrDown3', r3)
# cv2.waitKey(0)
# cv2.destroyWindow()

img = cv2.imread('lena.jpg')

r1 = cv2.pyrUp(img)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)

cv2.imshow('original', img)
cv2.imshow('pyrup1', r1)
cv2.imshow('pyrup2', r2)
cv2.imshow('pyrup3', r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
