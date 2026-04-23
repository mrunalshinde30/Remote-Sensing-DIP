import cv2
import os
from skimage.metrics import structural_similarity as ssim
import numpy as np

input_folder = "results/preprocessed/"   # ✅ FIXED
filtered_folder = "results/filtered/"

def calculate_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return 100
    return 20 * np.log10(255.0 / np.sqrt(mse))

for file in os.listdir(input_folder):
    orig = cv2.imread(input_folder + file, 0)

    f1 = cv2.imread(filtered_folder + "g_" + file, 0)
    f2 = cv2.imread(filtered_folder + "m_" + file, 0)
    f3 = cv2.imread(filtered_folder + "b_" + file, 0)

    if orig is None or f1 is None:
        continue

    print("\nImage:", file)

    for name, img in [("Gaussian", f1), ("Median", f2), ("Bilateral", f3)]:
        psnr_val = calculate_psnr(orig, img)
        ssim_val = ssim(orig, img)

        print(f"{name} -> PSNR: {psnr_val:.2f}, SSIM: {ssim_val:.4f}")