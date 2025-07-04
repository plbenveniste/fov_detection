# Vertebrae Presence Extractor

This project produces and analyzes spinal cord segmentation images (in `.nii.gz` format) generated with the [`totalspineseg`](https://github.com/neuropoly/totalspineseg) tool and automatically detects the presence of vertebrae across different regions of the spine (Cervical, Thoracic, Lumbar). It generates a structured CSV report indicating which vertebrae are present in each image.

## 📌 Features
- Runs the totalspineseg tool on the images
- Load and analyze `.nii.gz` segmentation images
- Detect presence of:
  - **Cervical vertebrae (C1–C7)**
  - **Thoracic vertebrae (T1–T12)**
  - **Lumbar vertebrae (L1–L5)**
- Create a CSV file that:
  - Lists each image path
  - States whether cervical, thoracic, and lumbar vertebrae are present
  - Shows a `True`/`False` column for every individual vertebra (e.g., C1, T2, L5, etc.)

## 🔧 Installation

### 1. Install Conda

We recommend installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for a minimal setup.

---

### 2. Install Spinal Cord Toolbox (SCT)

Clone the SCT repository and run the installer:

```bash
git clone https://github.com/spinalcordtoolbox/spinalcordtoolbox.git
cd spinalcordtoolbox
./install_sct
```

---

### 3. Install Python dependencies

Install the required Python packages such as nibabel:

```bash
pip install nibabel
```

---

### 4. Download the required dataset

Install this particular dataset and make sure to have git installed on your computer:
```bash
git clone https://github.com/spine-generic/data-multi-subject && \
cd data-multi-subject && \
git annex init && \
git annex get
```

## 🧪 Example Output

Example CSV output:

```csv
Image_path,Cervical,Thoracic,Lumbar,C1,C2,C3,...,L5
/path/to/img.nii.gz,TRUE,TRUE,FALSE,TRUE,TRUE,FALSE,...,FALSE
```

## 🧠 Labels Used

The segmentation is based on these label values:
| Label | Name |
|:------|:-----|
| 11 | vertebrae_C1 |
| 12 | vertebrae_C2 |
| 13 | vertebrae_C3 |
| 14 | vertebrae_C4 |
| 15 | vertebrae_C5 |
| 16 | vertebrae_C6 |
| 17 | vertebrae_C7 |
| 21 | vertebrae_T1 |
| 22 | vertebrae_T2 |
| 23 | vertebrae_T3 |
| 24 | vertebrae_T4 |
| 25 | vertebrae_T5 |
| 26 | vertebrae_T6 |
| 27 | vertebrae_T7 |
| 28 | vertebrae_T8 |
| 29 | vertebrae_T9 |
| 30 | vertebrae_T10 |
| 31 | vertebrae_T11 |
| 32 | vertebrae_T12 |
| 41 | vertebrae_L1 |
| 42 | vertebrae_L2 |
| 43 | vertebrae_L3 |
| 44 | vertebrae_L4 |
| 45 | vertebrae_L5 |

## 🚀 Usage

### Command Line

```bash
python run_all_imgs.py -i /path/to/dataset -path_to_csv /path/to/output.csv
```
## 📊 Vertebrae Frequency Analysis

This project includes a visualization to analyze how frequently each vertebra appears across the dataset.

### 🔍 What It Does

- Reads the final CSV file containing per-image vertebrae presence.
- Computes the **percentage presence** of each vertebra label (e.g., C1, T2, L5) across all processed images.
- Displays the results in a **sorted vertical bar chart**, grouped by vertebra region (Cervical, Thoracic, Lumbar).
- Each bar represents how often that specific vertebra appears across the dataset.

### 📈 Output Example

The script produces a clean and informative **barplot** using Seaborn, with the following features:
- Vertically-oriented histogram
- Color-coded bars using a `viridis` palette
- Vertebrae sorted in anatomical order (C1–C7, T1–T12, L1–L5)
- Saved automatically as an image file (e.g., `vertebrae_frequencies.png`)

See [issue #4](https://github.com/plbenveniste/fov_detection/issues/4) for more details.

### 📁 Output File

The figure is saved automatically in high resolution (`300 dpi`) for use in presentations, papers, or reports.

### Command Line

```bash
python stats.py -i /path/to/csv_file -o /path/to/output
```