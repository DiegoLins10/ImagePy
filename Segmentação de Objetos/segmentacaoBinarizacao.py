import cv2
import numpy as np

imgOriginal = cv2.imread("img/anya.jpeg", 0)

metodo = cv2.THRESH_BINARY_INV  
#cv2..THRESH_BINARY -- parte principal em preto
#cv2.THRESH_BINARY_INV  -- parte principal em branco

ret, imgBinarizada = cv2.threshold(imgOriginal, 135, 255, metodo)

#cv2.imshow("Imagem Original", imgOriginal)
#cv2.imshow("Imagem tratada", imgBinarizada)



cv2.imwrite("anya2.jpeg", imgBinarizada) ## salva a imagem para usar no morfologia


cv2.imshow("original", imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
