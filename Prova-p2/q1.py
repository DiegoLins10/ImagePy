import cv2
import numpy as np




img  = cv2.imread("botao1.jpg",0)
imgTipo = cv2.THRESH_BINARY
ret ,binarizada = cv2.threshold(img,127,255,imgTipo)



modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE
contornar,hierarquia= cv2.findContours(
    binarizada,modo,metodo
)




f=len(contornar) -2
print(f)


cv2.waitKey(0)
cv2.destroyAllWindows()