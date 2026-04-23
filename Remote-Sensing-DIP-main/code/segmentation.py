import cv2
import numpy as np
import os

input_folder = "results/preprocessed/"
output_folder = "results/segmented/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = input_folder + file
    img = cv2.imread(path)

    if img is None:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- Method 1: Otsu Thresholding ---
    _, otsu = cv2.threshold(gray, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # --- Method 2: K-Means Clustering ---
    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    K = 3
    _, label, center = cv2.kmeans(
        Z, K, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        10, cv2.KMEANS_RANDOM_CENTERS
    )

    center = np.uint8(center)
    res = center[label.flatten()]
    segmented = res.reshape(img.shape)

    cv2.imwrite(output_folder + "otsu_" + file, otsu)
    cv2.imwrite(output_folder + "kmeans_" + file, segmented)

print("SEGMENTATION DONE 🔥")