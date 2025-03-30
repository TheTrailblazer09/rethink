import os
import dlib
import cv2
import numpy as np
import json
from imutils import face_utils
from scipy.spatial.distance import cosine

def face_recognizer(image_path):
# Load dlib models
    p = "shape_predictor_68_face_landmarks.dat"
    face_rec_model = "dlib_face_recognition_resnet_model_v1.dat"

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)
    face_recognizer = dlib.face_recognition_model_v1(face_rec_model)

    # Load the stored encodings
    with open("all_face_encodings.json", "r") as f:
        stored_encodings = json.load(f)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    rects = detector(gray, 1)
    matched_names = []
    # Iterate over the faces in the image
    for rect in rects:
        # Get facial landmarks
        shape = predictor(gray, rect)
        
        # Extract 128-d embedding (face encoding)
        face_descriptor = face_recognizer.compute_face_descriptor(image, shape)
        encoding = np.array(face_descriptor)
        
        # Compare the encoding with the stored encodings
        min_distance = float('inf')
        matched_name = None

        for filename, encodings in stored_encodings.items():
            for stored_encoding in encodings:
                # Calculate the cosine distance between the encodings
                distance = cosine(encoding, np.array(stored_encoding))
                if distance < min_distance:
                    min_distance = distance
                    matched_name = filename        
        matched_names.append(matched_name)
    print(matched_names)
    return matched_names


#    Draw a bounding box around the face and display the matched name
#         x, y, w, h = face_utils.rect_to_bb(rect)
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
#         # Display the matched name (filename)
#         cv2.putText(image, matched_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Display the output image with the matched names
#     cv2.imshow("Matched Faces", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
