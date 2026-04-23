import cv2
import os

input_folder = "dataset/"
output_folder = "results/preprocessed/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = input_folder + file
    img = cv2.imread(path)

    if img is None:
        continue

    img = cv2.resize(img, (256,256))

    cv2.imwrite(output_folder + file, img)

print("DONE 🔥 Check results folder")
