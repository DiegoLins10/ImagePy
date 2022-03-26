## importando biblioteca
## separacao de canais espaços de cores
import cv2
import numpy as np

#carregar imagem
img = cv2.imread(".././img/luffy.jpg")


B, G, R = cv2.split(img)

# combinando cores
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imshow("IMG PADRAO", cv2.merge([B, G, R]))

## fechar o programa com qualquer tecla == 0
cv2.waitKey(0)
cv2.destroyAllWindows()