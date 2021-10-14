'''

10.2.1原理知识
直方图均衡化是图像灰度变化的一个重要处理，广泛应用于图像增强领域。它是指通过某种灰度映射将原始图像的像素点均匀地分布在每一个灰度级上，
其结果将产生一幅灰度级分布概率均衡的图像。直方图均衡化地中心思想是把原始图像的灰度直方图从比较集中的某个灰度区间转变为全范围均匀分布
的灰度区间，通过该处理，增加了像素灰度值的动态范围，从而达到增强图像对整体对比度的效果。直方图均衡化包括三个核心步骤。
(1)统计直方图中每个灰度级出现的次数。
(2)计算累计归一化直方图。
(3)重新计算像素点的像素值。
直方图均衡化算法的详细处理过程如下。
首先，计算原始图像直方图的概率密度，P(rk)=nk/N。其中，rk表示第k个灰度级(k=0,1,2,...L-1)，L最大值为256；
nk表示图像中灰度级rk的像素个数；N表示图像中像素的总个数；P(rk)表示图像中第k个灰度级占总像素数的比例。
其次，通过灰度变换函数T计算新图像灰度级的概率密度。新图像灰度级的概率密度是原始图像灰度级概率密度的累计，sk=T(rk)=ΣP(rj)
其中，k是新图像的灰度级，k=0,1,2,...L-1；rk表示原始图像的第k个灰度级；sk为直方图均衡化处理后的第k个灰度级。
最后，计算新图像的灰度值。由于sk=T(rk)=ΣP(rj)计算所得的sk位于0~1，需要乘以图像的最大灰度级L，转换为最终的灰度值res
res=sk×L
Python调用OpenCV中的cv2.equalizeHist()函数实现直方图均衡化处理，并且为全局直方图均衡化。
dst=cv2.equalizeHist(src, dst=None)
(1)src表示输入图像。
(2)dst表示目标图像，直方图均值化处理的结果。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('test.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# result = cv2.equalizeHist(gray)
# cv2.imshow('input', gray)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread('lena.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# result = cv2.equalizeHist(gray)
# plt.subplot(221)
# plt.imshow(gray, cmap=plt.cm.gray)
# plt.axis('off')
# plt.title('(a)')
# plt.subplot(222)
# plt.imshow(result, cmap=plt.cm.gray)
# plt.axis('off')
# plt.title('(b)')
# plt.subplot(223)
# plt.hist(img.ravel(), 256)
# plt.title('(c)')
# plt.subplot(224)
# plt.hist(result.ravel(), 256)
# plt.title('(d)')
# plt.show()

'''
彩色图像进行全局均衡化处理
'''
img = cv2.imread('yxz.jpg')
b, g, r = cv2.split(img)
bh = cv2.equalizeHist(b)
gh = cv2.equalizeHist(g)
rh = cv2.equalizeHist(r)
result = cv2.merge((bh, gh, rh))
# cv2.imshow('input', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.figure('Hist')
plt.hist(bh.ravel(), bins=256, density=1, color='b', edgecolor='b', stacked=1)
plt.hist(gh.ravel(), bins=256, density=1, color='g', edgecolor='g', stacked=1)
plt.hist(rh.ravel(), bins=256, density=1, color='r', edgecolor='r', stacked=1)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

