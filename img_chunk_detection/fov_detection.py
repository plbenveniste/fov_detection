"""
This script processes a NIfTI image to identify the presence of cervical, thoracic, and lumbar vertebrae.

Input: 
    -i: path to the NIfTI image output from totalspineseg
    -path_to_csv: path to save the CSV file containing vertebrae information

Output:
    -path_to_csv: the updated CSV file containing the vertebrae information

Author: Nathan Benveniste
"""
import nibabel as nib # type: ignore
import argparse
import csv


def Parse_Args():
    parser = argparse.ArgumentParser(description="Identify vertebrae in a NIfTI image")
    parser.add_argument('-i', type=str, required=True, help='Path to the output of totalspineseg')
    parser.add_argument('-path_to_csv', type=str, required=True, help='Path to save the csv file containing the vertebrae information for each image')
    return parser.parse_args()


def from_output_to_bool(img_path):
    # This function processes the NIfTI image to determine the presence of cervical, thoracic, and lumbar vertebrae.
    img = nib.load(img_path)
    data = img.get_fdata()
    print(f"Dimensions : {data.shape}")
    # Print unique values
    unique_values = set(data.flatten())
    print(f"Unique values in the image: {unique_values}")
    # Determine which types of vertebrae are present
    # Cervical vertebrae: 11-17
    # Thoracic vertebrae: 21-32
    # Lumbar vertebrae: 41-45
    # Verify if the unique values contain cervical, thoracic, or lumbar vertebrae
    C = any(11 <= x <= 17 for x in unique_values)
    T = any(21 <= x <= 32 for x in unique_values)
    L = any(41 <= x <= 45 for x in unique_values)
    print(f"Cervical vertebrae present: {C}"), print(f"Thoracic vertebrae present: {T}"), print(f"Lumbar vertebrae present: {L}")
    return C, T, L, unique_values


def from_output_to_csv(img_path, path_to_csv, C, T, L, unique_values):
    # This function is a placeholder for future implementation
    # It should convert the output to a CSV file containing vertebrae information
    # Dictionaries to link vertebrae labels to their names
    VERTEBRAE_LABELS = {
        11: "vertebrae_C1", 12: "vertebrae_C2", 13: "vertebrae_C3", 14: "vertebrae_C4",
        15: "vertebrae_C5", 16: "vertebrae_C6", 17: "vertebrae_C7",
        21: "vertebrae_T1", 22: "vertebrae_T2", 23: "vertebrae_T3", 24: "vertebrae_T4",
        25: "vertebrae_T5", 26: "vertebrae_T6", 27: "vertebrae_T7", 28: "vertebrae_T8",
        29: "vertebrae_T9", 30: "vertebrae_T10", 31: "vertebrae_T11", 32: "vertebrae_T12",
        41: "vertebrae_L1", 42: "vertebrae_L2", 43: "vertebrae_L3", 44: "vertebrae_L4",
        45: "vertebrae_L5"
    }
    # Verify if the file already exists
    # Construction of the data by vertebra presence
    vertebrae_presence = {label: "True" if label in unique_values else "False" for label in VERTEBRAE_LABELS}
    try:
        with open(path_to_csv, 'r', encoding='utf-8') as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    # Open the file (or create it if it doesn't exist)
    with open(path_to_csv, 'a') as f:
        if not file_exists:
            header = ["Image_path", "Cervical", "Thoracic", "Lumbar"] + list(VERTEBRAE_LABELS.values())
            f.write(",".join(header) + "\n")
        row = [img_path, str(C), str(T), str(L)] + [str(vertebrae_presence[label]) for label in VERTEBRAE_LABELS]
        f.write(",".join(row) + "\n")


def main():
    args = Parse_Args()
    img_path = args.i
    path_to_csv = args.path_to_csv
    C, T, L, unique_val = from_output_to_bool(img_path)
    from_output_to_csv(img_path, path_to_csv, C, T, L, unique_val)

if __name__ == "__main__":
    main()