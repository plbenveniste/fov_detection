import pathlib
from run_totalspineseg import totalspineseg
from fov_detection import from_output_to_bool, from_output_to_csv
import pathlib as Path
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Identify vertebrae in a NIfTI image")
    parser.add_argument('-i', type=str, required=True, help='Path to the folder containing NIfTI images serving as input for totalspineseg')
    parser.add_argument('-o', type=str, required=True, help='Path to save the segmented image returned by totalspineseg')
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
    """
    Run totalspineseg on the input image and then process the output to generate a CSV file.
    """
    # Run totalspineseg
    totalspineseg(input_path, output_path)

    # Process the output to get vertebrae information
    output_path = output_path.split(".nii.gz")
    output_path = "".join(output_path) + "_step2_output.nii.gz"
    C, T, L = from_output_to_bool(output_path)
    # Save the vertebrae information to a CSV file
    from_output_to_csv(output_path, path_to_csv, C, T, L)


if __name__ == "__main__":
    args = parse_args()
    input_path = args.i
    output_path = args.o
    path_to_csv = args.path_to_csv
    # imgs = get_all_imgs(input_path)
    run_all_imgs(input_path, output_path, path_to_csv)
    # print(imgs[0:10])
    # print(len(imgs))  # Print the total number of images found
