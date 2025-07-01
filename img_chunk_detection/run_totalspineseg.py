import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Identify vertebrae in a NIfTI image")
    parser.add_argument('-i', type=str, required=True, help='Path to the NIfTI image serving as input for totalspineseg')
    parser.add_argument('-o', type=str, required=True, help='Path to save the segmented image returned by totalspineseg')
    return parser.parse_args()


def totalspineseg(input_path, output_path):
    # Placeholder function for totalspineseg.
    # Here you would implement the logic to process the input NIfTI image
    # and save the output to the specified path.
    assert os.system(f"sct_deepseg totalspineseg -i {input_path} -o {output_path}")==0
    


def main():
    args = parse_args()
    input_path = args.i
    output_path = args.o
    totalspineseg(input_path, output_path)
    
    
    # Here you would call the totalspineseg function with input_path and output_path
    # For example:
    # totalspineseg(input_path, output_path)
if __name__ == "__main__":
    main()


     