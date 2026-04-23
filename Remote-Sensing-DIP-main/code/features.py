import cv2
import os

input_folder = "results/preprocessed/"
output_folder = "results/features/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = input_folder + file
    img = cv2.imread(path)

    if img is None:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)

    # CLAHE (contrast enhancement)
    clahe = cv2.createCLAHE(2.0, (8,8))
    enhanced = clahe.apply(gray)

    cv2.imwrite(output_folder + "edge_" + file, edges)
    cv2.imwrite(output_folder + "clahe_" + file, enhanced)

print("FEATURE EXTRACTION DONE 🔥")