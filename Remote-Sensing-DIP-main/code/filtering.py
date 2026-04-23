import cv2
import os

input_folder = "results/preprocessed/"
output_folder = "results/filtered/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = input_folder + file
    img = cv2.imread(path)

    if img is None:
        continue

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(img, (5,5), 0)

    # Median Blur
    median = cv2.medianBlur(img, 5)

    # Bilateral Filter
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    cv2.imwrite(output_folder + "g_" + file, gaussian)
    cv2.imwrite(output_folder + "m_" + file, median)
    cv2.imwrite(output_folder + "b_" + file, bilateral)

print("FILTERING DONE 🔥")