from sklearn.neighbors import KNeighborsClassifier

import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
#from win32com.client import Dispatch

#def speak(str1):
 #   speak = Dispatch(("SAPI.SpVoice"))
  #  speak.Speak(str1)


video = cv2.VideoCapture(1) #storing webcam stuff in video
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

COL_NAMES = ['NAME', 'TIME']


while True:
   ret,frame = video.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #haarcascade works better on grayscale
   myFaces = faceDetection.detectMultiScale(gray, 1.3, 5)
   for(x, y, w, h) in myFaces:
       croppedImage = frame[y:y+h, x:x+w, :]
       resizedImage = cv2.resize(croppedImage, (50,50)).flatten().reshape(1,-1)

       output = knn.predict(resizedImage)
       ts = time.time()
       date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
       timestamp=datetime.fromtimestamp(ts).strftime("%H-%M-%S")
       os.path.isfile("attendance/attendance_" +date+".csv")
       cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),1)
       cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1) #adds a square around the face
       attendancedb = [str(output[0]), str(timestamp)]
   cv2.imshow("frame", frame)
   k = cv2.waitKey(1)
   if k==ord('x'):
       if os.path.exists("attendance/attendance_" +date+".csv"):
           #speak("Attendance taken")
           #time.sleep(5)
           with open("attendance/attendance_" + date + ".csv", "+a") as csvfile:
               writer = csv.writer(csvfile)
               writer.writerow(attendancedb)
           csvfile.close()
       else:
           with open("attendance/attendance_"+date+".csv", "+a") as csvfile:
               writer = csv.writer(csvfile)
               writer.writerow(COL_NAMES)
               writer.writerow(attendancedb)
           csvfile.close()
   if k == ord('q'):
       break
video.release()
cv2.destroyAllWindows()

