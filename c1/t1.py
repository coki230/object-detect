import cv2
import numpy as np

# img = cv2.imread("beautiful-girl-with-autumn-leaves-photo.jpg")
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img.shape)
# new_img = np.zeros((img.shape[0] * 2, img.shape[1], img.shape[2]),dtype=np.uint8)
# print(new_img.shape)
# new_img[:400,:,:] = img[:,:,:]
# new_img[400:,:,:] = img[::-1,:,:]
# cv2.imshow("img", new_img)
# cv2.waitKey(0)


img = cv2.imread("../c3/beautiful-girl-with-autumn-leaves-photo.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
contours, hir = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
w_img = np.ones((img.shape[0], img.shape[1]))

d_img = cv2.drawContours(w_img, contours, -1, (0, 255, 0))
cv2.imshow("img", d_img)
cv2.waitKey(0)