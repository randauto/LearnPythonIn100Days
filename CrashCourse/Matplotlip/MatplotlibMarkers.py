import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='*')  # marker

plt.show()
# Marker Reference
# https://www.w3schools.com/python/matplotlib_markers.asp

# Format Strings fmt

plt.plot(ypoints, 'o:r', ms=20)  # Mark each point with a circle red color with marker size 20 px
plt.show()

plt.plot(ypoints, 'o--b')  # Mark each point with a circle red color:
plt.show()

plt.plot(ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')
plt.show()
