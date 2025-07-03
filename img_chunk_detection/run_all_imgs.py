"""
This script runs the totalspineseg segmentation on a dataset containing NIfTI images to identify vertebrae and saves the results in a CSV file.

Input: 
    -i: path to the folder containing NIfTI images serving as input for totalspineseg
    -path_to_csv: path to save the CSV file containing vertebrae information

Output:
    -path_to_csv: the updated CSV file containing the vertebrae information

Author: Nathan Benveniste
"""
import pathlib
from run_totalspineseg import totalspineseg
from fov_detection import from_output_to_bool, from_output_to_csv
import pathlib as Path
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Identify vertebrae in a NIfTI image")
    parser.add_argument('-i', type=str, required=True, help='Path to the folder containing NIfTI images serving as input for totalspineseg')
    parser.add_argument('-path_to_csv', type=str, required=True, help='Path to save the CSV file containing the vertebrae information for each image')
    return parser.parse_args()


def get_all_imgs(input_path):
    imgs_list = list(pathlib.Path(input_path).rglob("*.nii.gz"))
    # conversion to string
    imgs_list = [str(img) for img in imgs_list] 
    # Remove derivatives
    imgs_list = [img for img in imgs_list if "derivatives" not in img]
    imgs_list = [img for img in imgs_list if "sourcedata" not in img]
    imgs_list = [img for img in imgs_list if  "/dwi/" not in img]  # Exclude DWI images
    return imgs_list


def run_all_imgs(input_path, output_path, path_to_csv):
    # Run totalspineseg
    totalspineseg(input_path, output_path)
    # Process the output to get vertebrae information
    output_path = output_path.split(".nii.gz")
    output_path = "".join(output_path) + "_step2_output.nii.gz"
    C, T, L, unique_val = from_output_to_bool(output_path)
    # Save the vertebrae information to a CSV file
    from_output_to_csv(input_path, path_to_csv, C, T, L, unique_val)


if __name__ == "__main__":
    args = parse_args()
    input_path = args.i
    assert os.system("mkdir ~/Desktop/temp")==0
    output_path = "~/Desktop/temp/seg_img.nii.gz"
    path_to_csv = args.path_to_csv
    imgs = get_all_imgs(input_path)
    print(imgs)
    # Loop through all images and process them
    for img in imgs:
        print(f"Processing image: {img}")
        # Process the output to generate CSV
        run_all_imgs(img, output_path, path_to_csv)
    assert os.system("rm -r ~/Desktop/temp")==0
