# World Happiness EDA & Model

This repository contains our data analysis pipeline in a Jupyter notebook, along with supporting CSV files managed through Git LFS.

## Dependencies

You can set up the environment using either Conda (recommended) or pip.

### Option 1: Conda Installation (Recommended)
```bash
# Create new conda environment
conda create -n yourenv python=3.8
conda activate yourenv

# Install packages
conda install -c conda-forge pandas numpy matplotlib seaborn scikit-learn jupyter
conda install -c conda-forge geopandas
conda install -c plotly plotly

# Verify installation
python -c "import pandas; import numpy; import matplotlib; import seaborn; import sklearn; import geopandas; import plotly"
```

### Option 2: Pip Installation
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

requirements.txt:
```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
geopandas
plotly
```

## Setup Instructions

1. Install Git LFS
```bash
# Mac (Homebrew)
brew install git-lfs

# Ubuntu
sudo apt-get install git-lfs

# Windows
# Download from https://git-lfs.com
```

2. Clone and Initialize
```bash
# Clone repository
git clone [repository-url]
cd [repository-name]

# Initialize Git LFS
git lfs install

# Pull LFS files
git lfs pull
```

3. Set Up Python Environment (choose either Conda or Pip method above)

4. Launch Jupyter
```bash
jupyter notebook
```

## Project Structure
```
├── data/           # CSV files (managed by Git LFS)
├── analysis.ipynb  # Main analysis notebook
├── .gitattributes  # Git LFS configuration
└── requirements.txt
```

## Notes for Contributors
- All CSV files are managed through Git LFS
- Make sure Git LFS is installed before cloning
- Always pull LFS files after cloning: `git lfs pull`
- Use the same environment setup (Conda or pip) as other team members for consistency

## Note: Storage Limits
- GitHub LFS has a storage limit of 1GB for free accounts
- Monthly bandwidth limit: 1GB
