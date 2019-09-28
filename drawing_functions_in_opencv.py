import cv2
import numpy as np

img = cv2.imread('demo-image.jpg', 1)
img = np.zeros([500, 500, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 10)
img = cv2.arrowedLine(img, (0, 0), (255, 255), (255, 0, 0), 10)

img = cv2.rectangle(img, (0,0), (300, 300), (0,0,255), 5)
img = cv2.circle(img, (200,200), 100, (0,0,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (0, 200), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()