import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

image = cv2.imread('image.jpg')
image = image.astype(np.float32) / 255.0

mean = 0
variance = 1
stddev = math.sqrt(variance)

rows, cols, channels = image.shape
noise = np.random.normal(mean, stddev, (rows, cols, channels))

noisy_image = image + noise
noisy_image = np.clip(noisy_image, 0, 1)
x = np.linspace(mean - 3*stddev, mean + 3*stddev, 100)

noisy_image = (noisy_image * 255).astype(np.uint8)

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, stats.norm.pdf(x, mean, stddev))
ax1.set_title("Probability Density Function")
ax2.plot(x, stats.norm.cdf(x, mean, stddev))
ax2.set_title("Cumulative Distribution Function")

cv2.imshow("original", image)
cv2.imshow("noisy", noisy_image)
plt.show()
cv2.waitKey(0)
