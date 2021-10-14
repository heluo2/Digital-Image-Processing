'''

  绘制直线
在OpenCV中，绘制直线需要获取直线的起点和终点坐标，调用cv2.line()函数实现该功能
line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
(1)img表示需要绘制直线的图像
(2)pt1表示线段第一个点的坐标
(3)pt2表示线段第二个点的坐标
(4)color表示线条颜色，需要传入一个RGB元组
(5)thickness表示线条粗细
(6)lineType表示线条的类型
(7)shift表示点坐标中的小数位数

绘制矩形
在OpenCV中，绘制矩形通过cv2.rectangle()函数实现
rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
(1)img表示需要绘制矩形的图像
(2)pt1表示矩形左上角位置坐标
(3)pt2表示矩形右下角位置坐标
(4)color表示矩形颜色
(5)thickness表示线条粗细
(6)lineType表示线条的类型
(7)shift表示点坐标中的小数位数

绘制圆形
在OpenCV中，绘制矩形通过cv2.circle()函数实现
circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
(1)img表示需要绘制圆的图像
(2)center表示圆心坐标
(3)radius表示圆的半径
(4)color表示圆的颜色
(5)thickness如果为正值，表示圆轮廓的厚度，如果为负值表示绘制一个填充圆
(6)lineType表示圆的边界的类型
(7)shift表示中心坐标和半径值中的小数位数

绘制椭圆
在OpenCV中，绘制矩形通过cv2.ellipse()函数实现
ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
(1)img表示需要绘制椭圆的图像
(2)center表示椭圆圆心坐标
(3)axes表示轴的长度（短半径和长半径）
(4)angle表示偏转的角度（逆时针旋转）
(5)startAngle表示圆弧起始角的角度（逆时针旋转）
(6)endAngle表示圆弧终结角的角度（逆时针旋转）
(7)color表示线条的颜色
(8)thickness如果为正值，表示椭圆轮廓的厚度，如果为负值表示绘制一个填充椭圆
(9)lineType表示椭圆的边界的类型
(10)shift表示中心坐标和轴值中的小数位数

绘制多边形
在OpenCV中，绘制矩形通过cv2.polylines()函数实现
polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)
(1)img表示需要绘制圆的图像
(2)pts表示多边形曲线阵列
(3)isClosed表示绘制的多边形是否闭合，False表示不闭合
(4)color表示线条的颜色
(5)thickness表示线条厚度
(6)lineType表示边界的类型
(7)shift表示顶点坐标中的小数位数

绘制文字
在OpenCV中，绘制矩形通过cv2.putText()函数实现
putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
(1)img表示需要绘制圆的图像
(2)text表示要绘制的文字
(3)org表示绘制的位置，即图像中文本字符串的左下角
(4)fontFace表示字体类型
(5)fontScale表示字体大小，计算比例因子乘以字体特定的基本大小
(6)color表示字体颜色
(7)thickness表示字体粗细
(8)lineType表示边界的类型
(9)bottomLeftOrigin如果为真，则图像数据原点位于左下角，否则在它左上角

'''

import cv2
import numpy as np

'''
绘制直线
'''
# # 创建黑色图像
# img = np.zeros((256, 256, 3), np.uint8)
#
# # 绘制直线
# # cv2.line(img, (0, 0), (255, 255), (55, 255, 155), 5)
# i = 0
# while i < 255:
# 	cv2.line(img, (0, i), (255, 255 - i), (55, 255, 155), 5)
# 	i += 1
#
# # 显示图像
# cv2.imshow('line', img)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制矩形
'''
# # 创建黑色图像
# img = np.zeros((256, 256, 3), np.uint8)
#
# # 绘制矩形
# cv2.rectangle(img, (20, 20), (150, 150), (55, 255, 155), 5)
#
# # 显示图像
# cv2.imshow('rectangle', img)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制圆
'''
# 创建黑色图像
# img = np.zeros((256, 256, 3), np.uint8)
#
# # 绘制圆
# cv2.circle(img, (100, 100), 50, (55, 255, 155), 5)	#空心
# cv2.circle(img, (100, 100), 50, (55, 255, 155), -1)	#实心
#
# # 显示图像
# cv2.imshow('circle', img)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制椭圆
'''
# # 创建黑色图像
# img = np.zeros((256, 256, 3), np.uint8)
#
# # 绘制椭圆
# # 椭圆中心(120,100)，长轴和短轴为(100,50)
# # 偏转角度为20°
# # 圆弧起始角的角度0°，圆弧终结角的角度360°
# # 颜色(255,0,255)，线条厚度2
# # cv2.ellipse(img, (120, 100), (100, 50), 20, 0, 360, (255, 0, 255), 2)	#空心
# cv2.ellipse(img, (120, 100), (100, 50), 20, 0, 360, (255, 0, 255), -1)	#实心
#
# # 显示图像
# cv2.imshow('ellipse', img)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制多边形
'''
# # 创建黑色图像
# img = np.zeros((512, 512, 3), np.uint8)
#
# # 绘制多边形
# # pts = np.array([[10, 80], [120, 80], [120, 200], [30, 250]])	#四边形
# pts = np.array([[50, 190], [380, 420], [255, 50], [120, 420],[450,190]])	#五角星
# cv2.polylines(img, [pts], True, (255, 255, 255), 5)
#
# # 显示图像
# cv2.imshow('pts', img)
#
# # 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
绘制多边形
'''
# 创建黑色图像
img = np.zeros((256, 256, 3), np.uint8)

# 绘制文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'I LOVE PYTHON!', (10, 100), font, 0.6, (255, 255, 0), 2)

# 显示图像
cv2.imshow('wenzi', img)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
