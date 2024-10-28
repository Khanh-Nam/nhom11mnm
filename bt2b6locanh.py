# su dung bo loc lam rox anh chup x quang

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh chụp X-quang
img = cv2.imread(r'D:\Ki 7\Ma nguon mo\b6\xuong.jpg')  # Đọc ở dạng ảnh xám (grayscale)

# 1. Tạo kernel làm nét ảnh
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

# 2. Áp dụng bộ lọc làm rõ (sharpen)
output = cv2.filter2D(img, -1, kernel_sharpening)

# 3. Kết hợp hai ảnh vào một khung
combined = np.hstack((img, output))  # Nối hai ảnh theo chiều ngang

# Hiển thị kết quả bằng matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Ảnh gốc')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Ảnh sau khi làm rõ')
plt.imshow(output, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
