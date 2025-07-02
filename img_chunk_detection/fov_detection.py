import nibabel as nib # type: ignore
import argparse
import csv


def Parse_Args():
    parser = argparse.ArgumentParser(description="Identify vertebrae in a NIfTI image")
    parser.add_argument('-i', type=str, required=True, help='Path to the output of totalspineseg')
    parser.add_argument('-path_to_csv', type=str, required=True, help='Path to save the csv file containing the vertebrae information for each image')
    return parser.parse_args()


def from_output_to_bool(img_path):
    img = nib.load(img_path)
    data = img.get_fdata()
    print(f"Dimensions : {data.shape}")
    # ici on print les valeurs uniques
    unique_values = set(data.flatten())
    print(f"Unique values in the image: {unique_values}")
    # on détermine quels types de vertèbres sont présents
    C,T,L = False,False,False
    # Cervical vertebrae: 11-17
    # Thoracic vertebrae: 21-32
    # Lumbar vertebrae: 41-45
    # On vérifie si les valeurs uniques contiennent des vertèbres cervicales, thoraciques ou lombaires
    for x in unique_values:
        if 11<= x <= 17:
            C = True
        if 21<= x <= 32:
            T = True
        if 41<= x <= 45:
            L = True
    print(f"Cervical vertebrae present: {C}"), print(f"Thoracic vertebrae present: {T}"), print(f"Lumbar vertebrae present: {L}")
    return C, T, L


def from_output_to_csv(img_path, path_to_csv, C, T, L):
    # This function is a placeholder for future implementation
    # It should convert the output to a CSV file containing vertebrae information
    # Vérifie si le fichier existe déjà
    try:
        with open(path_to_csv, 'r', encoding='utf-8') as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    # Ouvre le fichier en mode ajout (ou crée-le)
    with open(path_to_csv, 'a', encoding='utf-8') as f:
        if not file_exists:
            f.write("Image_path,Cervical,Thoracic,Lumbar\n")
        f.write(f"{img_path},{C},{T},{L}\n")


def main():
    args = Parse_Args()
    img_path = args.i
    path_to_csv = args.path_to_csv
    C, T, L = from_output_to_bool(img_path)
    from_output_to_csv(img_path, path_to_csv, C, T, L)

if __name__ == "__main__":
    main()