import cv2
import numpy as np

imagemOriginal = cv2.imread("anya2.jpeg", 0)


elementosEstruturante = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE, (5, 5)
)

imagemProcessada = cv2.morphologyEx(
    imagemOriginal, cv2.MORPH_CLOSE, elementosEstruturante
)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()

