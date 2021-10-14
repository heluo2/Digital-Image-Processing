'''

OpenCV是一个轻量级高效的跨平台计算机视觉库，实现了图像处理和计算机视觉方面的多种通用算法。
图像可以理解为一个数组，图像处理就是对数字的处理。

读取图像：
retval = imread(filename, flags=None)
1）filename表示需要载入的图片路径名
2）flags为int类型，表示载入标识,指定一个加载图像的颜色类型，默认值为1。
  cv2.IMREAD_UNCHANGED表示读入完整图像或图像，包括alpha通道；
  cv2.IMREAD_GRAYSCALE表示读入灰度图像；
  cv2.IMREAD_COLOR表示读入彩色图像，默认参数，忽略alpha通道。

显示图像：
imshow(winname,mat)
1)winname表示窗口的名称
2）mat表示要显示的图像

显示图像过程中还要调用两个操作窗口的函数，它们分别是waitKey()和cv2.destroyWindow()
retval = waitKey(delay=None)
键盘绑定函数，共一个参数delay，表示等待的毫秒数，看键盘是否有输入，返回值为ASCII值。如果参数为0，则表示无限期的等待键盘输入；
参数大于0表示等待delay毫秒；参数小于0表示等待键盘单机。
destroyWindow()
该函数可以轻易删除所有建立的窗口。如果你想删除特定的窗口可以使用cv2.destroyWindow()，并在括号内输入要删除的窗口名。

'''

import cv2

# 读取图像
img = cv2.imread('lena.jpg')

# 显示图像
cv2.imshow('demo', img)

# 等待显示
# cv2.waitKey(0)
# cv2.destroyWindow()

# 无限期等待输入
k = cv2.waitKey(0)

# 如果输入Esc按键退出
if k == 27:
	cv2.destroyAllWindows()
