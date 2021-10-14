'''

图像顶帽运算(top-hat transformation)又称为图像礼帽运算，它是原始图像减去图像开运算后的结果，常用于解决由于光照不均匀图像分割出错的问题。
图像顶帽运算使用一个结构元通过开运算从一幅图像中删除物体，顶帽运算用于暗背景上的亮物体，它的一个重要用途是矫正不均匀光照的影响。

图像顶帽运算在OpenCv中主要使用函数morphologyEx()，它是形态学扩展的一组函数
dst=morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None
(1)src表示原始图像。
(2)op表示形态学运算的类型，MORPH_TOPHAT - 形态学顶帽运算。
(3)kernel表示卷积核。
(4)iterations表示迭代次数。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# src = cv2.imread('test06.png', cv2.IMREAD_UNCHANGED)
#
# kernel = np.ones((10, 10), np.uint8)
# result = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)
#
# cv2.imshow('src', src)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制灰度三维图
'''
img = cv2.imread('test06.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((10, 10), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# imgd = np.array(img)
imgd = np.array(result)

sp = img.shape
h = int(sp[0])
w = int(sp[1])

fig = plt.figure(figsize=(16, 12))
ax = fig.gca(projection="3d")

x = np.arange(0, w, 1)
y = np.arange(0, h, 1)
x, y = np.meshgrid(x, y)
z = imgd
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)

# 自定义z轴
ax.set_zlim(-10, 255)
ax.zaxis.set_major_locator(LinearLocator(10))  # 设置z轴网格线的疏密
# 将z的value字符串转为float并保留两位小数
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# 设置坐标轴的label和标题
ax.set_xlabel('x', size=15)
ax.set_ylabel('y', size=15)
ax.set_zlabel('z', size=15)
ax.set_title('surface plot', weight='bold', size=20)

# 添加右侧的色卡条
fig.colorbar(surf, shrink=0.6, aspect=8)
plt.show()
