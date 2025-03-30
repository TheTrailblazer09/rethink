from recognizer import face_recognizer
import shutil
import os

def organizer(image_path, matched_names):
    directory = "/Users/krishaanggupta/Documents/Rethink assessment/Outputs/"
    class_dict = {"104": 0, "106": 0, "108": 0}
    for name in matched_names:
        num,_ = name.split(".")
        if int(num) > 120 and int(num) < 145:
            class_dict["104"] += 1
        elif int(num) > 167 and int(num) < 189:
            class_dict["106"] += 1
        elif int(num) > 207 and int(num) < 237:
            class_dict["108"] += 1
            
    if (class_dict["104"]/len(matched_names) > 0.3):
        destination_path = directory + "104"
        shutil.copy(image_path, destination_path)

    elif (class_dict["106"]/len(matched_names) > 0.3):
        destination_path = directory + "106"
        shutil.copy(image_path, destination_path)

    elif (class_dict["108"]/len(matched_names) > 0.3):
        destination_path = directory + "108"
        shutil.copy(image_path, destination_path)
    print("GrEaT SuCcEsS")

if __name__ == "__main__":
    image_folder = input("Enter the path for the folder of images")
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            organizer(image_path, face_recognizer(image_path))