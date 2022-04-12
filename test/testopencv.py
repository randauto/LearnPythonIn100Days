import cv2 as cv
import numpy as np

img_gray = cv.imread("girl1.jpg", cv.IMREAD_GRAYSCALE)
image = cv.imread("girl1.jpg")
cv.imshow("Girl Color", image)
cv.imshow("Girl Gray", img_gray)

b, g, r = image[100, 100]
print(b, g, r)
print(img_gray.shape)

cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("girl_gray.jpg", img_gray)
