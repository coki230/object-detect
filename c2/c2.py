import numpy as np
import cv2

# hc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img = cv2.imread("2.jpeg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# dets = hc.detectMultiScale(img_gray, 1.2, 2)
# for det in dets:
#     x, y, w, h = det
#     img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow("img", img)
# cv2.waitKey(0)

img = cv2.imread("2.jpeg")
mask = np.zeros((img.shape[0], img.shape[1])).astype("uint8")
rect = cv2.selectROI(img)
bgdModel = np.zeros((1, 65))
fgdModel = np.zeros((1, 65))


ct = cv2.grabCut(img=img, mask=mask, rect=rect, bgdModel=bgdModel, fgdModel=fgdModel, iterCount=5, mode=cv2.GC_INIT_WITH_RECT)

print(np.unique(mask, return_counts=True))

mask = np.where(mask > 2, 1, 0).astype("uint8")

cv2.imshow("img", img * mask[:, :, np.newaxis])
cv2.waitKey(0)