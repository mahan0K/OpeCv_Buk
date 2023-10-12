import cv2

img = cv2.imread("test.jpg")
#print(img.shape)
img = cv2.resize(img,(5800,800))
##print(img.shape)
# OpenCv    работает с BGR синии , зелённый,красный.
cv2.imshow("Result", img)

cv2.waitKey(0)


