import cv2 
import numpy as np


imgRGB = cv2.imread("zoro.jpg")
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

##print(imgHSV)

#verdeClaro = cv2.cvtColor([(172,238,65,255)], cv2.COLOR_BGR2HSV)
verdeClaro = np.uint8([[173,237,67,255]])
verdeClaro2 = cv2.cvtColor(verdeClaro, cv2.COLOR_BGR2HSV)
print(verdeClaro)

#tomClaro = np.array([40, 40, 40]) ## VERDE
tomClaro = np.array(verdeClaro2) ## VERDE
tomEscuro = np.array([70, 255, 255])

imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)

cv2.imshow("Original", imgRGB)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()


