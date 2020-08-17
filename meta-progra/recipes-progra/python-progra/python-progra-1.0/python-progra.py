#CERROJO CON RECONOCIMIENTO FACIAL

import cv2
import os
import RPi.GPIO as GPIO
import time
import numpy

LED_encendido = 7
LED_acceso = 11
LED_desconocido = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_encendido,GPIO.OUT)
GPIO.setup(LED_acceso,GPIO.OUT)
GPIO.setup(LED_desconocido,GPIO.OUT)

dataPath = 'C:/home/edgardo/poky/meta-progra/recipes-progra/python-progra/python-progra-1.0'
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

face_recognizer = cv2.face.EigenFaceRecognizer_create()

face_recognizer.read('modeloEigenFace_Sofia.xml')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    GPIO.output(LED_encendido,GPIO.HIGH)
    ret,frame = cap.read()
    if ret == False:break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        #EigenFaces
        if result[1] <5000:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            GPIO.output(LED_acceso,GPIO.HIGH)
            GPIO.output(LED_desconocido,GPIO.LOW)
            time.sleep(0.5)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            GPIO.output(LED_acceso,GPIO.LOW)
            GPIO.output(LED_desconocido,GPIO.HIGH)
            time.sleep(0.5)
        
    cv2.imshow('frame',frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()
