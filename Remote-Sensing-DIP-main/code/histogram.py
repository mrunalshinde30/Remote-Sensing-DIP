import cv2
import os
import matplotlib.pyplot as plt

input_folder = "dataset/"
output_folder = "results/histograms/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    path = input_folder + file
    img = cv2.imread(path, 0)  # grayscale

    if img is None:
        continue

    plt.hist(img.ravel(), bins=256)
    plt.title("Histogram - " + file)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.savefig(output_folder + file + "_hist.png")
    plt.clf()

print("HISTOGRAM DONE 🔥")
