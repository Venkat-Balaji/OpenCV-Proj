import face_recognition

Venkat_image = face_recognition.load_image_file("C:/Users/HAI/Desktop/attendance/Venkat.jpg")
Venkat_encoding = face_recognition.face_encodings(Venkat_image)[0]

Shiyam_image = face_recognition.load_image_file("C:/Users/HAI/Desktop/attendance/Shiyam.jpg")
Shiyam_encoding = face_recognition.face_encodings(Shiyam_image)[0]

Hari_image = face_recognition.load_image_file("C:/Users/HAI/Desktop/attendance/Hari.jpg")
Hari_encoding = face_recognition.face_encodings(Hari_image)[0]

# Hamsi_image = face_recognition.load_image_file("C:/Users/HAI/Desktop/attend/Hamsi.jpg")
# Hamsi_encoding = face_recognition.face_encodings(Hamsi_image)[0]

# Madhu_image = face_recognition.load_image_file("C:/Users/HAI/Desktop/attend/Madhu.jpg")
# Madhu_encoding = face_recognition.face_encodings(Madhu_image)[0]

# Shakthi_image = face_recognition.load_image_file("C:/Users/HAI/Desktop/attend/Shakthi.jpg")
# Shakthi_encoding = face_recognition.face_encodings(Shakthi_image)[0]

known_face_encodings = [Venkat_encoding, Shiyam_encoding, Hari_encoding]
known_face_names = ["Venkat Balaji", "Shiyam", "Hari"]
known_face_reg=["713321TS054","713321TS047","713321TS019"]
