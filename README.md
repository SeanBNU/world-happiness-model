# World Happiness EDA & Model

This repository contains our data analysis pipeline in a Jupyter notebook, along with supporting CSV files managed through Git LFS.

## Dependencies

- Python 3.8+
- Git LFS
- Jupyter Notebook

### Python Packages
```
pip install -r requirements.txt
```

Required packages:
- pandas
- numpy
- jupyter
[Add any other specific packages your notebook uses]

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

3. Create Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

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
- Update requirements.txt if you add new dependencies

## Storage Limits
- GitHub LFS has a storage limit of 1GB for free accounts
- Monthly bandwidth limit: 1GB
