'''

如果要统计图像的某一部分直方图，就需要使用掩模（蒙板）来进行计算。假设将要统计的部分设置为白色，其余部分设置为黑色，
然后使用该掩模进行直方图绘制。

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

img = cv2.imread('yxz.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 设置掩模
mask = np.zeros(img.shape[:2], np.uint8)
mask[50:150, 50:150] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)

# 图像直方图计算
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
# 图像直方图计算（含掩模）
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

plt.figure(figsize=(8, 6))

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.subplot(221)
plt.imshow(img_rgb, 'gray')
plt.axis('off')
plt.title('(a)原始图像')

plt.subplot(222)
plt.imshow(mask, 'gray')
plt.axis('off')
plt.title('(b)掩模')

plt.subplot(223)
plt.imshow(masked_img, 'gray')
plt.axis('off')
plt.title('(c)图像掩模处理')

plt.subplot(224)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.title('(d)直方图曲线')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
