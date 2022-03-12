import cv2


imagem = cv2.imread("C:/Users/diego.lins/Desktop/python/cachorro.jpg")

cv2.imshow("imagem", imagem)

cv2.waitKey(0)

cv2.destroyAllWindows()