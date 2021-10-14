'''

Matplotlib是Python强大的数据可视化工具，主要用于绘制各种2D图形。本节Python绘制直方图主要调用matplotlib.pyplot库中hist()函数实现，
它会根据数据源和像素级绘制直方图。
n,bins,patches=plt.hist(arr,bins=50,density=1,color='green',alpha=0.75)
(1)arr表示需要计算直方图的一维数组。
(2)bins表示直方图显示的柱数，可选项，默认值为10。
(3)density表示是否将得到的直方图进行向量归一化处理，默认值为0。
(4)color表示直方图颜色。
(5)alpha表示透明度。
(6)n为返回值，表示直方图向量。
(7)bins为返回值，表示各个bin的区间范围。
(8)patches为返回值，表示返回每个bin里面包含的数据，是一个列表。
注意，读取picture.bmp图像的像素为二维数组，而hist()函数的数据源必须是一维数组，通常需要通过函数ravel()拉直图像。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# src = cv2.imread('lena.jpg')
#
# # plt.hist(src.ravel(), 256)
# plt.hist(src.ravel(), bins=256, density=1, facecolor='g', alpha=0.75)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
#
# cv2.imshow('src', src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
分别画出三个通道的直方图
'''
# src = cv2.imread('lena.jpg')
# b, g, r = cv2.split(src)
#
# plt.figure('lena')
# plt.hist(b.ravel(), bins=256, density=1, color='b', edgecolor='b', stacked=1)
# plt.hist(g.ravel(), bins=256, density=1, color='g', edgecolor='g', stacked=1)
# plt.hist(r.ravel(), bins=256, density=1, color='r', edgecolor='r', stacked=1)
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

src = cv2.imread('lena.jpg')
img_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

b, g, r = cv2.split(src)
plt.figure(figsize=(8, 6))

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

plt.subplot(221)
plt.imshow(img_rgb)
plt.axis('off')
plt.title('(a)原图像')
plt.subplot(222)
plt.hist(b.ravel(), bins=256, density=1, color='b', edgecolor='b', stacked=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)蓝色分量直方图')
plt.subplot(223)
plt.hist(g.ravel(), bins=256, density=1, color='g', edgecolor='g', stacked=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)绿色分量直方图')
plt.subplot(224)
plt.hist(r.ravel(), bins=256, density=1, color='r', edgecolor='r', stacked=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)红色分量直方图')
plt.show()
