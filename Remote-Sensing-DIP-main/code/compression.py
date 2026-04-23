import cv2
import os

input_folder = "results/preprocessed/"
output_folder = "results/compressed/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = input_folder + file
    img = cv2.imread(path)

    if img is None:
        continue

    # JPEG compression (lossy)
    cv2.imwrite(output_folder + "jpg_" + file,
                img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

    # PNG compression (lossless)
    cv2.imwrite(output_folder + "png_" + file, img)

print("COMPRESSION DONE 🔥")