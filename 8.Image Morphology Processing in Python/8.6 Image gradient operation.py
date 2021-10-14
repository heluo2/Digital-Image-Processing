'''

图像梯度运算是图像膨胀处理减去图像腐蚀处理后的结果，从而得到图像的轮廓。
图像梯度运算在OpenCv中主要使用函数morphologyEx()，它是形态学扩展的一组函数
dst=morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None
(1)src表示原始图像。
(2)op表示形态学运算的类型，MORPH_GRADIENT - 形态学梯度（Morphological gradient）。
(3)kernel表示卷积核。
(4)iterations表示迭代次数。

'''

import cv2
import numpy as np

src = cv2.imread('test04.png', cv2.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
kernel = np.ones((10, 10), np.uint8)
result = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('src', src)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

