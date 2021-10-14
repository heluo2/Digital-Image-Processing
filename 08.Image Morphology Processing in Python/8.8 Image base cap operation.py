'''

图像底帽运算(botton-hat transformation)又称为图像黑帽运算，它是用图像闭运算操作减去原始图像后的结果，
从而获取图像内部的小孔或前景色中黑点，也常用于光照不均匀图像分割出错的问题。
图像底帽运算是用一个结构元通过闭运算从一幅图像中删除物体，常用于矫正不均匀光照的影响。
图像底帽运算在OpenCv中主要使用函数morphologyEx()，它是形态学扩展的一组函数
dst=morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None
(1)src表示原始图像。
(2)op表示形态学运算的类型，MORPH_BLACKHAT - 形态学底帽运算。
(3)kernel表示卷积核。
(4)iterations表示迭代次数。

'''

import cv2
import numpy as np

src = cv2.imread('test06.png', cv2.IMREAD_UNCHANGED)

kernel = np.ones((10, 10), np.uint8)
result = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('src', src)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()