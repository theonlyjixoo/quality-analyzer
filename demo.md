# Project Quality Calculator (Integrator)
> **Part of Undergraduate Thesis Project**

This Python script (`demo.py`) serves as the integration layer of the research. It calculates the final quality scores for each Machine Learning repository by combining code analysis results with community engagement metrics.

## 📌 Overview
`demo.py` is designed to process multiple data sources and output a comprehensive "Quality Profile" for each project. It evaluates projects based on three main pillars: **Code Health (Smells)**, **Sustainability (Popularity)**, and **Stability**.

## 🚀 Key Functionalities
- **Multi-Source Data Merging**: Combines data from `grouped_analysis_results.csv` (analysis output) and `fixed_df.csv` (metadata output).
- **Project Quality Scoring**: Implements a weighted scoring formula:
  - **Code Smell Weight (50%)**: Evaluating the technical debt.
  - **Sustainability Weight (30%)**: Based on stargazers and community interest.
  - **Stability Weight (20%)**: Based on issue management and project age.
- **Automated Ranking**: Automatically identifies the Top 5 best-performing and bottom 5 worst-performing projects based on the final quality percentage.
- **Data Sanitization**: Handles string formatting for repository names to ensure accurate mapping between datasets.

## 📊 Scoring Metrics
The script produces the following metrics for each repository:
1. **Sustainability Score (%)**: Reflects the popularity and community backing.
2. **Stability Score (%)**: Reflects how well the project is maintained.
3. **Overall Quality Score (%)**: The final weighted average used for the thesis conclusion.



## 🛠️ Requirements
- `pandas`: For data frame manipulation and CSV processing.
- `numpy`: For numerical calculations.
- `scikit-learn`: For underlying regression models and validation metrics (MSE).

## ⚙️ Configuration
> [!IMPORTANT]
> **Data Dependency:** This script requires two CSV files to be present in the specified directory:
> - `grouped_analysis_results.csv`
> - `fixed_df.csv`
>
> **Path Settings:** Please update the variables `grouped_analysis_results_path` and `fixed_df_path` inside the script to match your local file system before execution.

## 🖥️ How to Run
Run the script via terminal or command prompt:
```bash
python demo.py
