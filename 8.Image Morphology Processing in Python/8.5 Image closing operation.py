'''

图像闭运算是图像依次经过膨胀、腐蚀处理的过程，先膨胀后腐蚀有助于过滤前景物体内部的小孔或物体上的小黑点。
A被B闭运算就是A被B膨胀后的结果再被B腐蚀。
图像闭运算在OpenCv中主要使用函数morphologyEx()，它是形态学扩展的一组函数
dst=morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None
(1)src表示原始图像
(2)op表示形态学运算的类型，MORPH_CLOSE – 闭运算（Closing operation）
(3)kernel表示卷积核
(4)iterations表示迭代次数

'''

import cv2
import numpy as np

src = cv2.imread('test03.png', cv2.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
kernel = np.ones((10, 10), np.uint8)
result = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)

cv2.imshow('src', src)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
