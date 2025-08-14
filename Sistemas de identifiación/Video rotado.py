import cv2
import numpy as np

i=0

captura = cv2.VideoCapture(0)
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    i=i+1
    ancho = imagen.shape[1] #columnas
    alto = imagen.shape[0] # filas
    M = cv2.getRotationMatrix2D((ancho//2,alto//2),i,1)
    imageOut = cv2.warpAffine(imagen,M,(ancho,alto))
    cv2.imshow('video', imageOut)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
  else: break
captura.release()
cv2.destroyAllWindows()