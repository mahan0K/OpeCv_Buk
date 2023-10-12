import cv2

img = cv2.imread("test.jpg")
print(img.shape)
img = cv2.resize(img,(500,800))
print(img.shape)
# OpenCv    работает с BGR синии , зелённый,красный.





