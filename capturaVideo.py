import cv2

captura = cv2.VideoCapture("C:/Users/diego.lins/Desktop/python/video.mp4")

while True:
    ret, frame = captura.read()
    cv2.imshow("imagem", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

## Zera variaveis
captura.release()

## Fecha janelas
cv2.destroyAllWindows()