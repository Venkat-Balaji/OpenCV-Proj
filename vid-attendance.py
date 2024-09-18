import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
from data import known_face_encodings, known_face_names

video_path = "C:/Users/HAI/Desktop/attendance/video.mp4"
video_capture = cv2.VideoCapture(video_path)

students = known_face_names.copy()
face_locations = []
face_encodings = []
face_names = []
s = True

current_date = datetime.now().strftime("%d-%m-%Y")
f = open(current_date + '-Attendance.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

            if name in known_face_names:
                if name in students:
                    students.remove(name)
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
