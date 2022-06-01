import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, ls='-.')
plt.show()

"""
The line style can be written in a shorter syntax:
linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --
supported value:  '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
"""

# Line Color

plt.plot(ypoints, color='r')
plt.show()

# You can also use Hexadecimal color values:
plt.plot(ypoints, c='#4CAF50')
plt.show()

# Or any of the 140 supported color names.
# link: https://www.w3schools.com/colors/colors_names.asp
plt.plot(ypoints, c='hotpink')
plt.show()

# Line Width

plt.plot(ypoints, linewidth='20.5', ls='dashed', c='r')
plt.show()

# Draw two lines by specifiyng the x- and y-point values for both lines:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
