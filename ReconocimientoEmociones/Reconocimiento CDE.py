import cv2
import os
import imutils

personName = 'CDE'
dataPath = 'C:/Users/raula/OneDrive/Escritorio/Python/reconocimientoderostros/Data'#Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 768)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1366)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 768)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1366)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    
    ret, frame = cap.read()
    if ret == False:
        break
    frame =  imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        #cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
        #count = count + 1

        name = "CIUDADANO"
        color = (125, 220, 0)
        cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, -1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)

    resized = cv2.resize(frame, (768, 1240), interpolation=cv2.INTER_AREA)

    cv2.imshow('frame',resized)

    k =  cv2.waitKey(1)
    if k == 27 or count >= 300:
        break

cap.release()
cv2.destroyAllWindows()
