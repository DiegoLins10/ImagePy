import cv2
import numpy as np


total = 0
video = cv2.VideoCapture("contagem-de-objetos-480.mov")


while True:
    ret,frame = video.read()
    frameCinza = cv2.cvtColor(frame,cv2.COLOR_RGBA2GRAY)
    t = cv2.THRESH_BINARY_INV
    # procura a cor
    ret, frameBinarizado = cv2.threshold(frameCinza,200,255,t)
    cont, hierarquia = cv2.findContours(frameBinarizado, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#    soma o totalcontornos
    totalAtual = len(cont)
    if totalAtual != total:
         total = totalAtual
         print(totalAtual)

       

    cv2.imshow("Video botao", frame)
    if cv2.waitKey(1) & 0xFF  == ord("q"):
        break
  
video.release()
cv2.destroyAllWindows() 