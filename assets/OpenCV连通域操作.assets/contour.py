import cv2
import numpy as np

img = cv2.imread("1.png",cv2.IMREAD_GRAYSCALE)
img[img>0] = 255
print(img.shape)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
print(type(contours))
print(len(contours))
print(contours[0].shape)
cv2.drawContours(img,contours,-1,255,-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

area = []
for j in range(len(contours)):
    area.append(cv2.contourArea(contours[j]))
max_idx = np.argmax(area)
area[max_idx] = 0
sub_max_idx = np.argmax(area)

for k in range(len(contours)):
    if k != max_idx and k != sub_max_idx:
        cv2.fillPoly(img, [contours[k]], 0)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()