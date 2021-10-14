'''

在OpenCV中可以使用calcHist()函数计算直方图，计算完成后采用OpenCV中的绘图函数，如绘制矩形的rectangle()函数，绘制线段的line()函数来完成。
hist=cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
(1)hist表示直方图，返回一个二维数组。
(2)images表示输入的原始图像。
(3)channels表示指定通道，通道编号需要使用中括号，输入图像是灰度图像时，它的值为[0]，彩色图像则为[0],[1],[2],分别表示蓝色、绿色、红色。
(4)mask表示可选择的操作掩码。如果要统计整幅图像的直方图，则该值为None；如果需要统计图像的某一部分直方图，需要掩模来计算。
(5)histSize表示灰度级的个数，需要使用中括号。
(6)ranges表示像素值范围。
(7)accumu表示累计叠加标识，默认为false，如果被设置为true，则直方图在开始分配时不会被清零，该参数允许从多个对象中计算单个直方图，
或者用于实时更新直方图；多个直方图的累积结果用于对一组图像的直方图计算。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# src = cv2.imread('lena.jpg')
# hist = cv2.calcHist([src], [0], None, [256], [0, 255])
# print(hist.size)
# print(hist.shape)
# print(hist)
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# plt.subplot(121)
# plt.imshow(src, 'gray')
# plt.axis('off')
# plt.title('(a)原始图像')
# plt.subplot(122)
# plt.plot(hist, color='r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('(b)直方图曲线')
# plt.show()

'''
三个分量分别进行计算及绘制
'''
src = cv2.imread('lena.jpg')
img_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
histb = cv2.calcHist([src], [0], None, [256], [0, 255])
histg = cv2.calcHist([src], [1], None, [256], [0, 255])
histr = cv2.calcHist([src], [2], None, [256], [0, 255])
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.subplot(121)
plt.imshow(img_rgb, 'gray')
plt.axis('off')
plt.title('(a)原始图像')
plt.subplot(122)
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('(b)直方图曲线')
plt.show()