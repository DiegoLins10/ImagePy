## importando biblioteca
## separacao de canais espaços de cores
import cv2

#carregar imagem
img = cv2.imread(".././img/luffy.jpg")

## CONVERTER RGB EM HSV
imagemHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mascara verde (36,0,0) ~ (70, 255,255)
mask1 = cv2.inRange(imagemHsv, (36, 0, 0), (70, 255,255))

## mascara amarela (15,0,0) ~ (36, 255, 255)
mask2 = cv2.inRange(imagemHsv, (15,0,0), (36, 255, 255))

## junta as mascaras
mask = cv2.bitwise_or(mask1, mask2)
target = cv2.bitwise_and(img,img, mask=mask)

cv2.imwrite("saida.png", target)

file = cv2.imread("saida.png")

cv2.imshow("IMAGEM COMBINADA", file)

## fechar o programa com qualquer tecla == 0
cv2.waitKey(0)
cv2.destroyAllWindows()