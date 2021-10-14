'''

图像的腐蚀(erosion)和膨胀(dilation)是两种基本的形态学运算，主要用来寻找图像中的极小区域和极大区域。
图像腐蚀类似于”领域被蚕食“，它将图像中的高亮区域或白色部分进行缩减细化，其运行结果比原图的高亮区更小。
设A，B为集合，S被B的腐蚀，记为A-B
图像A用卷积模板B来进行腐蚀处理，通过模板B与图像A进行卷积计算，得出B覆盖区域的像素最小值，并用这个最小值来替代参考点的像素值。
图像腐蚀主要包括二值图像和卷积核两个输入对象 ，卷积核是腐蚀中的关键数组，采用Numpy库可以生成。卷积核的中心点逐个像素扫描原始图像，
被扫描到的原始图像中的像素点，只有当卷积核对应的元素值为1时，其值才为1，否则将其像素值修改为0.
在Python中，主要调用OpenCV的erode()函数实现图像腐蚀
dst=erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
(1)src表示原始图像
(2)kernel表示卷积核
(3)iterations表示迭代次数，默认值为1，表示进行一次腐蚀操作。
可以采用函数numpy.ones()创建卷积核

'''

import cv2
import numpy as np

src = cv2.imread('test01.jpg', cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
# # 图像腐蚀处理
# erosion = cv2.erode(src, kernel)
# 多次腐蚀处理
erosion = cv2.erode(src, kernel, iterations=9)

cv2.imshow('src', src)
cv2.imshow('result', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
