import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('image.jpg')

blue_channel, green_channel, _ = cv2.split(image)

joint_hist, x_edges, y_edges = np.histogram2d(
    blue_channel.flatten(),
    green_channel.flatten(),
    bins=(256, 256),
    range=[[0, 255], [0, 255]],
    density=True
)

plt.figure()
plt.imshow(joint_hist.T, origin='lower', extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]])
plt.xlabel('Blue Intensity')
plt.ylabel('Green Intensity')
plt.title('Joint Histogram of Blue and Green Channels')
plt.colorbar()
plt.show()


