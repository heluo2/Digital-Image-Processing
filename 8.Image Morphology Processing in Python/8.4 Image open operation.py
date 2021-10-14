'''

开运算一般能平滑图像的轮廓，削弱狭窄部分，去掉较细的突出。闭运算也能平滑图像的轮廓，与开运算相反，它一般融合窄的缺口和细长的弯口，
去掉小洞，填补轮廓上缝隙。
图像开运算是图像依次经过腐蚀、膨胀处理的过程，图象被腐蚀后将去除噪声，但同时也压缩了图像，然后对腐蚀过的图像进行膨胀处理，
可以在保留原有图像的基础上去除噪声。
A被B开运算就是A被B腐蚀后的结果再被B膨胀。
图像开运算在OpenCv中主要使用函数morphologyEx()，它是形态学扩展的一组函数
dst=morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None
(1)src表示原始图像。
(2)op表示形态学运算的类型，MORPH_OPEN – 开运算（Opening operation）。
(3)kernel表示卷积核。
(4)iterations表示迭代次数。

'''

import cv2
import numpy as np

src = cv2.imread('test01.png', cv2.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
kernel = np.ones((10, 10), np.uint8)
result = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)

cv2.imshow('src', src)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
