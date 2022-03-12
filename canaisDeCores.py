## importando biblioteca
import cv2

#carregar imagem
img = cv2.imread("./img/frutas.jpg")

## CONVERTER RGB EM HSV
imagemHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


matiz, saturacao, valor = cv2.split(imagemHsv)

cv2.imshow("CANAL H", matiz)
cv2.imshow("CANAL S", saturacao)
cv2.imshow("CANAL V", valor)
cv2.imshow("IMG PADRAO", imagemHsv)

## fechar o programa com qualquer tecla == 0
cv2.waitKey(0)
cv2.destroyAllWindows()


