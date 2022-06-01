import matplotlib.pyplot as plt
import numpy as np

# Draw a line in a diagram from position (0,6) to position (6,250):
xAxits = np.array([0, 6])
yAxits = np.array([6, 250])

plt.plot(xAxits, yAxits)
plt.plot(xAxits, yAxits, 'o')  # draw without line

# Multiple Points
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 20])

plt.plot(xpoints, ypoints)

plt.show()
