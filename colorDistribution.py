import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('image.jpg')

colorChannels = cv2.split(image)

histograms = []
cdfs = []
for channel in colorChannels:
    currentHistogram = np.bincount(channel.flatten(), minlength=256)
    currentHistogram = currentHistogram / channel.size
    histograms.append(currentHistogram)
    cdfs.append(np.cumsum(currentHistogram))

colors = ['blue', 'green', 'red']

fig, (ax1, ax2) = plt.subplots(2)
for i,histogram in enumerate(histograms):
    ax1.plot(histogram, color=colors[i], label=colors[i].capitalize())
    ax2.plot(cdfs[i], color=colors[i], label=colors[i].capitalize())

cv2.imshow("Image", image)

ax1.set_xlabel('Pixel Intensity')
ax1.set_ylabel('Normalized Frequency')
ax1.set_title('Normalized Color Image Histogram - Probability Mass Function')
ax1.legend()

ax2.set_xlabel('Pixel Intensity')
ax2.set_ylabel('CDF')
ax2.set_title('Cumulative Distribution Function')

plt.show()