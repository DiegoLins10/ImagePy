## importando biblioteca
## separacao de canais espaços de cores
import cv2

#carregar imagem
img = cv2.imread(".././img/luffy.jpg")


b, g, r = cv2.split(img)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
cv2.imshow("IMG PADRAO", img)

## fechar o programa com qualquer tecla == 0
cv2.waitKey(0)
cv2.destroyAllWindows()


