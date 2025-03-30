# import dlib
# import cv2
# import numpy as np
# import json

# # Load dlib models
# p = "shape_predictor_68_face_landmarks.dat"
# face_rec_model = "dlib_face_recognition_resnet_model_v1.dat"

# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(p)
# face_recognizer = dlib.face_recognition_model_v1(face_rec_model)

# # Load the image
# image = cv2.imread("238B28BF-66F5-4EDD-857D-2CD816ED875F_1_105_c.jpeg", cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Detect faces
# rects = detector(gray, 1)

# face_encodings = []
# for rect in rects:
#     # Get facial landmarks
#     shape = predictor(gray, rect)
    
#     # Extract 128-d embedding (face encoding)
#     face_descriptor = face_recognizer.compute_face_descriptor(image, shape)
#     encoding = np.array(face_descriptor)
    
#     # Store encoding
#     face_encodings.append(encoding.tolist())  # Convert to list for JSON storage

# # Save encodings to a JSON file
# with open("face_encodings.json", "w") as f:
#     json.dump(face_encodings, f)

# print(f"Saved {len(face_encodings)} face encodings to 'face_encodings.json'")


import os
import dlib
import cv2
import numpy as np
import json
from imutils import face_utils

# Load dlib models
p = "shape_predictor_68_face_landmarks.dat"
face_rec_model = "dlib_face_recognition_resnet_model_v1.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)
face_recognizer = dlib.face_recognition_model_v1(face_rec_model)

# Path to the folder containing images
image_folders = ["/Users/krishaanggupta/Documents/Rethink assessment/Portraits/TEACHER_104", 
                "/Users/krishaanggupta/Documents/Rethink assessment/Portraits/TEACHER_106", 
                "/Users/krishaanggupta/Documents/Rethink assessment/Portraits/TEACHER_108"]

# Initialize a list to hold all the encodings
all_encodings = {}

# Iterate through the images in the folder
for image_folder in image_folders:
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            rects = detector(gray, 1)

            face_encodings = []
            for rect in rects:
                # Get facial landmarks
                shape = predictor(gray, rect)
                
                # Extract 128-d embedding (face encoding)
                face_descriptor = face_recognizer.compute_face_descriptor(image, shape)
                encoding = np.array(face_descriptor)
                
                # Store encoding
                face_encodings.append(encoding.tolist())  # Convert to list for saving

            # Save encodings for the current image if faces are detected
            if face_encodings:
                all_encodings[filename] = face_encodings

# Save all encodings to a JSON file
with open("all_face_encodings.json", "w") as f:
    json.dump(all_encodings, f)

print(f"Saved encodings for {len(all_encodings)} images to 'all_face_encodings.json'")
