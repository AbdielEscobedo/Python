import cv2

cap = cv2.VideoCapture(0)
#Aqui llamamos al modelo preentrenado
faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
  ret,frame = cap.read()

#Convertimos la imagen en el frame en escala de grises para
#comparar con el modelo preentrenado
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#Comparamos la iamgen con la clasificacion preentrenadoa
  faces = faceClassif.detectMultiScale(gray, 1.3, 5)
#Dibuje el rectangulo desde el centro del reconocimiento
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

  cv2.imshow('frame',frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()