## importando biblioteca
import cv2

#carregar imagem
img = cv2.imread("./img/frutas.jpg")

##converter a imagem com o de cima para cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#3 Exibir imagem com a de cima cinza
cv2.imshow("Cinza", imgCinza)


## fechar o programa
cv2.waitKey(0)
cv2.destroyAllWindows()

