import cv2
import pickle
import numpy as np
import os

video = cv2.VideoCapture(0)
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize dictionary to store face data
faces_data_dict = {}

name = input("Enter Name for the person: ")

# Trim any extra characters and ensure the name is a valid filename
name = name.strip().replace(" ", "_")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    myFaces = faceDetection.detectMultiScale(gray, 1.3, 5)

    if name not in faces_data_dict:
        faces_data_dict[name] = []

    for (x, y, w, h) in myFaces:
        croppedImage = frame[y:y + h, x:x + w, :]
        resizedImage = cv2.resize(croppedImage, (50, 50))

        if len(faces_data_dict[name]) < 100:  # Limiting to 100 samples per person
            faces_data_dict[name].append(resizedImage)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
        cv2.putText(frame, f"{name}: {len(faces_data_dict[name])}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 255, 255), 1)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data_dict[name]) >= 100:
        break
video.release()
cv2.destroyAllWindows()

faces_data_dict[name] = np.asarray(faces_data_dict[name])
faces_data_dict[name] = faces_data_dict[name].reshape(100, -1)


# Save face data
if not os.path.exists('data'):
    os.makedirs('data')

with open(f"data/{name}_faces_data.pkl", 'wb') as f:
    pickle.dump(faces_data_dict[name], f)

if 'names.pkl' not in os.listdir('data/'):
    names = [name]
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names+[name]
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)


