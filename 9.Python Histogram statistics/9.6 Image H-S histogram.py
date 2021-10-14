'''

为了刻画图像中颜色的直观特性，常常需要分析图象的HSV空间下的直方图特性。HSV空间是由色调、饱和度、明度构成的，因此在进行直方图计算时，
需要先将原RGB图像转化为HSV颜色空间图像，然后将对应的H和S通道进行单元划分，在其二维空间上计算相对应直方图，
再计算直方图空间上的最大值并归一化绘制相应的直方图信息，从而形成色调-饱和度直方图（或H-S直方图）。该直方图通常应用在目标检测、
特征分析以及目标特征跟踪等场景。
由于H和S分量与人感受颜色的方式是紧密相连的，V分量与图像的色彩信息无关，这些特点使得HSV模型非常适合借助人的视觉系统来感知色彩特性的图像处理算法。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist(hsv, [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.figure(figsize=(8, 6))
plt.subplot(121)
plt.imshow(img_rgb, 'gray')
plt.title('(a)')
plt.axis('off')

plt.subplot(122)
plt.imshow(hist, interpolation='nearest')
plt.title('(b)')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
