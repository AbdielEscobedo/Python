import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#Creamos una ventana llamada frame donde generamos las dos trackbar para ajustar el blur
cv2.namedWindow('frame')
cv2.createTrackbar('Blur','frame',0,15,nothing)
cv2.createTrackbar('Gray','frame',0,1,nothing)

while True:    
    ret,frame = cap.read()    
    #Asiganamos los valores al blur y el valor de gray o no
    val = cv2.getTrackbarPos('Blur','frame')
    grayVal = cv2.getTrackbarPos('Gray','frame')
    #Si gray esta en uno convertimos todo el frame a escala de grises
    if grayVal == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassif.detectMultiScale(frame, 1.3, 5)

    for (x,y,w,h) in faces:
        if val > 0: 
            #Aqui ajustamos el frame a la cantidad de blur que queremos
            frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(val,val))
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()