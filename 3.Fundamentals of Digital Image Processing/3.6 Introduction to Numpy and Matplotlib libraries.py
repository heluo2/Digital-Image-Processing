'''

Numpy(Numeric Python)是Python提供的数值计算扩展包，拥有高效的处理函数和数值编程工具。
Array是Numpy库中最基础的数据结构，表示数组。
np.zeros()生成的数组均为0。

Matplotlib是Python强大的数据可视化工具和2D绘图库，常用于创建海量类型的2D图表和一些基本的D图表。
Matplotlib提供了一整套和Matlab相似的命令API，十分适合交互式地进行制图，可以将它作为绘图控件，嵌入GUI应用程序中。
Matplotlib作图库常用的函数如下：
1）Plot()：用于绘制二维图、折线图，其格式为plt.plot(X,Y,S)。其中X为横轴，Y为纵轴，参数S为指定绘图的类型、样式和颜色。
2）Pie()：用于绘制饼状图(Pie Plot)
3）Bar()：用于绘制条状图(Bar Plot)
4）Hist()：用于绘制二位条形直方图
5）Scatter()：用于绘制散点图

'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

'''
一维数组
'''
# # 定义一维数组
# a = np.array([2, 0, 1, 5, 8, 3])
# print('原始数据：', a)
#
# # 输出最大、最小值及形状
# print('最大值：', a.max())
# print('最小值：', a.min())
# print('形状：', a.shape)

'''
绘制图形
'''
# # 创建黑色图像
# img = np.zeros((256, 256,3), np.uint8)
#
# # 显示图像
# cv2.imshow('image', a)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制散点图
'''
# # 生成随机数表示点坐标
# x = np.random.rand(200)
# y = np.random.rand(200)
#
# # 生成随机点的大小及颜色
# size = 50 * np.random.rand(200)
# colors = np.random.rand(200)
#
# # 用来正常显示中文标签
# plt.rc('font', family='SimHei', size=13)
#
# # 用来正常显示负号
# plt.rcParams['axes.unicode_minus'] = False
#
# # 绘制散点图
# plt.scatter(x, y, s=size, c=colors)
#
# # 设置x、y轴名称
# plt.xlabel('x坐标')
# plt.ylabel('y坐标')
#
# # 绘制标题
# plt.title('Matplotlib绘制散点图')
#
# # 显示图像
# plt.show()

'''
显示多幅图形
'''
# 读取图像
img1 = cv2.imread('lena.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('people.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3 = cv2.imread('flower.jpg')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img4 = cv2.imread('scenery.jpg')
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

# 显示四幅图像
titles = ['lena', 'people', 'flower', 'scenery']
images = [img1, img2, img3, img4]
for i in range(4):
	plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
plt.show()
