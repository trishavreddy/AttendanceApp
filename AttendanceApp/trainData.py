import cv2
import pickle
import numpy as np
import os
import csv
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime

video = cv2.VideoCapture(0)
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load names
names = []
with open('data/names.pkl', 'rb') as f:
    while True:
        try:
            name = pickle.load(f)
            names = name
        except EOFError:
            break

# Load face data for each person
faces_data_dict = {}
for name in names:
    try:
        with open(f'data/{name}_faces_data.pkl', 'rb') as face_file:
            faces_data_dict[name] = pickle.load(face_file)
    except FileNotFoundError:
        print(f"No face data found for {name}.")

# Train the model
FACES = []
LABELS = []
for name, face_data in faces_data_dict.items():
    for face in face_data:
        FACES.append(face.flatten())
        LABELS.append(name)
FACES = np.array(FACES)
LABELS = np.array(LABELS)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

#COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    myFaces = faceDetection.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in myFaces:
        croppedImage = frame[y:y + h, x:x + w, :]  # Grayscale
        resizedImage = cv2.resize(croppedImage, (50,50)).flatten().reshape(1,-1) #changed this line

        # Check if resized image is empty
        if resizedImage.size == 0:
            continue

        # Flatten and reshape the image
        #resizedImage = resizedImage.flatten().reshape(1, -1)

        output = knn.predict(resizedImage)
        ts = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

        # Logging attendance when 'x' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('x'):
            with open(f"attendance/attendance_{output[0]}.csv", 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([output[0], ts])
                cv2.putText(frame, "Attendance Taken", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

