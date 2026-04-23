import os

original_folder = "dataset/"
compressed_folder = "results/compressed/"

for file in os.listdir(original_folder):
    orig_size = os.path.getsize(original_folder + file)

    comp_file = "jpg_" + file
    if os.path.exists(compressed_folder + comp_file):
        comp_size = os.path.getsize(compressed_folder + comp_file)

        ratio = orig_size / comp_size
        print(f"{file} -> Compression Ratio: {ratio:.2f}")