import cv2 as cv
import numpy as np

img_gray = cv.imread("girl1.jpg", cv.IMREAD_GRAYSCALE)
image = cv.imread("girl1.jpg")
cv.imshow("Girl Color", image)

# create a pic by numpy
pic = np.zeros((500, 500, 3), dtype='uint8')
# draw rectangle at 0,0 with width = 300, height = 300, and with color (255,255,255)
cv.rectangle(pic, (0, 0), (300, 300), (255, 255, 255), 3, lineType=8, shift=0)
cv.line(pic, (0, 0), (300, 300), (123, 123, 123))
color = (255, 0, 255)
cv.circle(pic, (150, 150), 100, color)
cv.line(pic, (300, 0), (0, 300), color)

content = "Le Quoc Tuan"
font = cv.FONT_HERSHEY_DUPLEX
cv.putText(pic, content, (0, 150), font, 2, color, 4, cv.LINE_8)

cv.imshow("dark", pic)

cv.waitKey(0)
cv.destroyAllWindows()
