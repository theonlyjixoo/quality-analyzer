# Analysis of Machine Learning Repository Trends on GitHub
> **Undergraduate Thesis Project**

This repository contains the full implementation of my thesis, organized into three main stages: Data Extraction, Core Analysis, and Model Validation.

## 📌 Project Workflow
To understand the repository trends, the project is divided into three functional modules:

1.  **Data Extraction** (`ambil-data-repo.ipynb`)
    - Interfaces with the GitHub REST API.
    - Collects raw metadata from Machine Learning repositories (stars, forks, languages, etc.).
    - Exports the collected data into CSV format for processing.

2.  **Core Analysis** (`Tesis_verse_1.1.ipynb`)
    - The primary analysis engine of this thesis.
    - Performs data cleaning, exploratory data analysis (EDA), and trend visualization.
    - Investigates the relationship between project activity and community engagement.

3.  **Model Validation** (`validasi.ipynb`)
    - Conducts statistical validation and performance testing (e.g., MSE calculation).
    - Uses Grid Search for hyperparameter tuning (Alpha & Beta weights).
    - Ensures the reliability of the analysis results and predictive models.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: 
  - `Requests`: API integration.
  - `Pandas & Numpy`: Data manipulation and numerical computation.
  - `Scikit-Learn`: Model validation and Grid Search.
  - `Matplotlib & Seaborn`: Scientific data visualization.

## 📂 Repository Structure
```text
├── ambil-data-repo.ipynb   # Stage 1: Data Gathering
├── Tesis_verse_1.1.ipynb   # Stage 2: Main Analysis
├── validasi.ipynb          # Stage 3: Validation & Testing
├── data/                   # Directory for CSV datasets
└── README.md               # Project documentation
