'''

OpenCV中没有CreatetImage函数，如果需要创建图像，则选哟使用Numpy库函数实现。
调用np.zeros()函数创建空图像，创建的信徒想使用Numpy数组的属性来表示图像的尺寸和通道信息，其中，参数img.shape表示原始图像的形状，
参数np.uint8表示类型。
emptyImage=np.zeros(img.shape,np.uint8)

在OpenCV中，输出图像到文件使用的函数为imwrite()。
retval=imwrite(filename, img, params=None)
filename表示要保存的路径及文件名
img表示图像矩阵
params特定格式保存的参数编码，默认值为空。对于JEPG图片，该参数cv2.IMWRITE_JPEG_QUALITY表示图像的质量，用0~100的整数表示，默认值为95.
对于PNG图片，该参数cv2.IMWRITE_PNG_COMPRESSION表示的是压缩级别，从0~9，压缩级别越高，图像尺寸越小，默认级别为3。
对于PPM、PGM、PBM图像，该参数表示一个二进制格式的标志cv2.IMWRITE_PXM_BINARY。注意该类型为Long，必须转换为int。

'''

import cv2
import numpy as np

img = cv2.imread('lena.jpg')

# # 创建空图像
# emptyImage = np.zeros(img.shape, np.uint8)
#
# # 复制图像
# emptyImage2 = img.copy()
#
# # 显示图像
# cv2.imshow('demo1', img)
# cv2.imshow('demo2', emptyImage)
# cv2.imshow('demo3', emptyImage2)

cv2.imshow('demo', img)

cv2.imwrite('dst1.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite('dst2.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite('dst3.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite('dat4.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

cv2.waitKey(0)
cv2.destroyAllWindows()
