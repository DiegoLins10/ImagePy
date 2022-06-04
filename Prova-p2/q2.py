import numpy as np
import cv2

cascadeFace = cv2.CascadeClassifier("frontalface.xml")

imagemOriginal = cv2.imread("pessoas.jpg")
imagem = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2GRAY)

# faces = cascadeFace.detectMultiScale(imagem, 1.3, 5)

faces = cascadeFace.detectMultiScale(
        imagem,
        scaleFactor=1.1,
        minNeighbors=1,
) 

#desenha um retangulo nas faces detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(imagemOriginal, (x,y), (x+w, y+h), (000,255,0), 2)
    
    
#exibe o total de faces detectadas
print(len(faces))

cv2.imshow("Resultado", imagemOriginal)
cv2.waitKey(0)
cv2.destroyAllWindows();    