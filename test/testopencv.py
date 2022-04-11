import cv2 as cv

img_gray = cv.imread("girl1.jpg", 0)
cv.imshow("Girl", img_gray)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("girl_gray.jpg", img_gray)
