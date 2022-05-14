import cv2 
import numpy as np


imgOriginal = cv2.imread("anya.jpeg", 0)


tipo = cv2.THRESH_BINARY_INV = cv2.THRESH_OTSU
limiar, imgBinarizada = cv2.threshold(imgOriginal, 0, 255, tipo)


print(limiar)

cv2.imshow("Imagem Original", imgOriginal)
cv2.imshow("imagem tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()