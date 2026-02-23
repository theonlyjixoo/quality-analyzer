# Data Acquisition Module: GitHub Repository Scraper
> **Part of Undergraduate Thesis Project**

This specific module is responsible for the initial data collection phase of the thesis. It automates the process of fetching metadata from GitHub repositories to build the research dataset.

## 📌 Overview
`ambil-data-repo.ipynb` is a Python-based notebook designed to interface with the **GitHub REST API**. It searches for repositories based on specific criteria (topics, languages, and popularity) and structured the raw JSON responses into a clean tabular format.

## 🚀 Key Functionalities
- **Automated Search**: Uses GitHub API's search endpoint to find projects labeled with "Machine Learning".
- **Attribute Extraction**: Collects critical metrics for analysis, including:
  - Repository Name & URL
  - Star & Fork Counts
  - Programming Language (Python)
  - Timestamps (Created, Updated, and Pushed dates)
  - Open Issues & License Information
- **Data Export**: Automatically converts the API response into a `.csv` file for use in the next stages of the research.

## 🛠️ Requirements
To run this notebook, you will need the following Python libraries:
- `requests`: To send HTTP requests to the GitHub API.
- `pandas`: To structure the collected data into DataFrames.
- `csv`: To handle file exporting.

## ⚙️ Configuration
Before running, ensure you have:
1. An active internet connection.
2. (Optional but Recommended) A **GitHub Personal Access Token** to increase the API rate limit and avoid being blocked during large data fetches.

## 📂 Output
The primary output of this file is a raw dataset (e.g., `github_repositories.csv`) which serves as the input for the main analysis notebook (`main_code.ipynb`).

---
**Status:** Completed - Data Gathering Stage
