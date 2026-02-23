# Model Validation & Parameter Optimization
> **Part of Undergraduate Thesis Project**

This module is dedicated to the validation phase of the thesis. It ensures that the analysis model is statistically sound and optimized for the research dataset.

## 📌 Overview
`validasi.ipynb` is a crucial component of the research that handles the fine-tuning of the scoring model. It uses mathematical approaches to find the most accurate weights for evaluating GitHub repository trends.

## 🚀 Key Functionalities
- **Weight Optimization (Grid Search)**: Systematically tests combinations of weights ($\alpha$ and $\beta$) to find the most effective parameters for the research model.
- **Error Measurement**: Calculates **Mean Squared Error (MSE)** to quantify the difference between the model's predictions and the actual data.
- **Data Integrity Check**: Processes the `fixed_df.csv` dataset to ensure consistency before final conclusions are drawn.
- **Linear Regression Analysis**: Utilizes `Scikit-Learn` to perform regression tasks that support the trend analysis findings.

## 🧪 Scientific Results (Example Output)
Based on the implementation, the notebook identifies:
- **Optimal Alpha ($\alpha$):** 0.1
- **Optimal Beta ($\beta$):** 0.9
- **Minimum MSE:** ~211.27

## 🛠️ Requirements
This notebook requires the following scientific Python stack:
- `pandas` & `numpy`: Data manipulation and numerical operations.
- `scikit-learn`: Implementation of `GridSearchCV`, `LinearRegression`, and `mean_squared_error`.
- `datetime`: Handling temporal data for validation.

## ⚙️ Configuration Note
> [!IMPORTANT]
> **File Paths:** This notebook currently references a local path (`D:/S2/Tesis/code/fixed_df.csv`). 
> To run this notebook in a new environment, update the `fixed_df_path` variable to point to your local `fixed_df.csv` file.

---
**Status:** Completed - Validation & Optimization Stage
