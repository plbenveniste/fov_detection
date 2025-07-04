
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Plot vertebrae region statistics from CSV.")
    parser.add_argument("-i", type=str, required=True, help="Path to CSV file containing vertebrae statistics.")
    parser.add_argument("-o", type=str, required=True, help="Output path for the plot image.")
    return parser.parse_args()


def plot_vertebrae_statistics(input_path, output_path):
    """
    Reads vertebrae presence data from a CSV and plots the percentage
    of images containing cervical, thoracic, and lumbar vertebrae.
    """
    # Load the CSV file
    df = pd.read_csv(input_path)

    # Extract vertebrae columns
    vertebra_cols = [col for col in df.columns if col.startswith("vertebrae_")]

    # Count the number of vertebrae detected per image
    df["vertebrae_count"] = df[vertebra_cols].sum(axis=1)

    # Calculate presence frequencies as %
    frequencies = df[vertebra_cols].mean() * 100  # Mean over booleans

    # Create a DataFrame with vertebra names and their frequencies
    freq_df = frequencies.reset_index()
    freq_df.columns = ["Vertebra", "Presence (%)"]

    # Custom sorting function: Cx → Tx → Lx
    def vertebra_sort_key(name):
        if "C" in name:
            return (0, int(name.split("C")[-1]))
        elif "T" in name:
            return (1, int(name.split("T")[-1]))
        elif "L" in name:
            return (2, int(name.split("L")[-1]))
        return (3, 0)

    # Appliquer le tri
    freq_df["SortKey"] = freq_df["Vertebra"].apply(vertebra_sort_key)
    freq_df = freq_df.sort_values("SortKey").drop("SortKey", axis=1)

    # Affichage
    plt.figure(figsize=(12, 6))
    sns.barplot(data=freq_df, x="Vertebra", y="Presence (%)", hue="Vertebra", palette="viridis", legend=False)
    plt.title("Vertebrae Presence Frequencies")
    plt.xticks(rotation=45)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')


def plot_vertebrae_region(input_path, output_path):
    """
    Reads vertebrae presence data from a CSV and plots the percentage
    of images containing cervical, thoracic, and lumbar vertebrae.
    """
    df = pd.read_csv(input_path)
    region_columns = df.columns[1:4]  # Assumes columns 1, 2, 3 are C, T, L
    region_percentages = df[region_columns].mean() * 100

    # Plot setup
    plt.figure(figsize=(8, 6))
    bars = plt.bar(region_columns, region_percentages, color=["#2578FE", "#FF2525", "#15FF25"], width=0.6)

    # Add value labels above bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom', fontsize=12)

    # Labeling
    plt.title("Presence of Vertebrae Regions in Images", fontsize=16)
    plt.xlabel("Vertebrae Region", fontsize=14)
    plt.ylabel("Percentage of Images (%)", fontsize=14)
    plt.ylim(0, 110)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    output_path = output_path.split('.')
    output_path = "".join(output_path[0]) + "_1" + "." + output_path[1]
    plt.savefig(output_path, dpi=300, bbox_inches='tight')


def plot_average_presence(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)

    # Get vertebrae columns (starting from 5th column)
    vertebrae_data = df.iloc[:, 4:]

    # Count present vertebrae per image (sum of TRUEs)
    vertebrae_counts = vertebrae_data.sum(axis=1)

    # Create label: Image_1, Image_2, ...
    image_labels = [f"Image_{i+1}" for i in range(len(df))]

    # Prepare DataFrame for plotting
    count_df = pd.DataFrame({
        "Image": image_labels,
        "Vertebrae Count": vertebrae_counts
    })

    # Compute statistics
    mean_val = vertebrae_counts.mean()
    median_val = vertebrae_counts.median()
    std_val = vertebrae_counts.std()

    # Plot
    plt.figure(figsize=(14, 6))
    sns.barplot(data=count_df, x="Image", y="Vertebrae Count", color="#2D7DFF")

    # Add horizontal lines for mean, median, and std
    plt.axhline(mean_val, color='red', linestyle='--', label=f"Mean: {mean_val:.1f}")
    plt.axhline(median_val, color='green', linestyle='-.', label=f"Median: {median_val:.1f}")
    plt.axhline(mean_val + std_val, color='orange', linestyle=':', label=f"Mean + Std: {mean_val + std_val:.1f}")
    plt.axhline(mean_val - std_val, color='orange', linestyle=':', label=f"Mean - Std: {mean_val - std_val:.1f}")

    # Labels and title
    plt.xticks(rotation=90, fontsize=9)
    plt.xlabel("Image", fontsize=12)
    plt.ylabel("Number of Vertebrae Present", fontsize=12)
    plt.title("Vertebrae Presence per Image", fontsize=14)
    plt.legend()
    plt.tight_layout()
    output_path = output_path.split('.')
    output_path = "".join(output_path[0]) + "_2" + "." + output_path[1]
    plt.savefig(output_path, dpi=300)


def main():
    args = parse_args()
    input_path = args.i
    output_path = args.o    
    # Plot vertebrae statistics and region presence
    print("Plotting vertebrae statistics...")
    plot_vertebrae_statistics(input_path, output_path)
    print("Plotting vertebrae region presence...")
    plot_vertebrae_region(input_path, output_path)
    print("Plotting average presence...")
    plot_average_presence(input_path, output_path)

if __name__ == "__main__":
    main()


