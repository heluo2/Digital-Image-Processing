'''

图像透视变换(perspective transformation)的本质是将图像投影到一个新的视平面，
同理OpenCV通过函数cv2.getAffineTransform(pos1, pos2)构造矩阵M。
得到M后再通过函数cv2.warpAffine(src,M,(cols, rows))进行透视变换。
M = cv2.getAffineTransform(pos1, pos2)
(1)pos1表示变换前的位置
(2)pos2表示变换后的位置
cv2.warpAffine(src,M,(cols, rows))
(1)src表示原始图像
(2)M表示仿射变换矩阵
(3)(cols, rows)表示比那桓侯的图像大小

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('lena1.jpg')
rows, cols = src.shape[:2]

pos1 = np.float32([[114, 82], [287, 156], [8, 332], [216, 333]])
pos2 = np.float32([[0, 0], [512, 0], [0, 512], [512, 512]])
M = cv2.getPerspectiveTransform(pos1, pos2)

result = cv2.warpPerspective(src, M, (cols, rows))

cv2.imshow('original', src)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
