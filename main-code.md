# Core Analysis & Trend Visualization
> **The Primary Engine of the Undergraduate Thesis**

This module (`main_code.ipynb`) is the heart of the research. It processes the raw metadata collected from GitHub and transforms it into meaningful insights regarding Machine Learning repository trends and community sustainability.

## 📌 Overview
The notebook focuses on Exploratory Data Analysis (EDA) and data preprocessing. It aims to answer the core research questions by identifying patterns in how open-source projects grow, peak, and sustain their development activity.

## 🚀 Key Functionalities
- **Data Preprocessing**: 
  - Loading raw datasets generated from the extraction stage.
  - Handling missing values and cleaning repository attributes.
  - Date-time conversion for longitudinal analysis (tracking projects over time).
- **Exploratory Data Analysis (EDA)**:
  - Analyzing distribution of stars, forks, and open issues.
  - Correlating developer activity (pushes/updates) with community interest.
- **Scientific Visualization**:
  - Generates distribution plots and correlation heatmaps.
  - Time-series charts showing the evolution of ML repositories.
  - Visualizing the sustainability metrics of various project categories.
- **Strategic Insights**:
  - Identifying the "Peak periods" of project engagement.
  - Providing a data-driven view for stakeholders on project reliability.



## 📊 Analyzed Metrics
This notebook specifically deep-dives into:
1. **Popularity Metrics**: Stargazers, Watchers, and Fork counts.
2. **Activity Metrics**: Created at vs. Updated at vs. Pushed at intervals.
3. **Project Health**: Ratio of open issues to total engagement.
4. **Technology Trends**: Language distribution and score-based ranking.

## 🛠️ Requirements
The following libraries are essential to run this analysis:
- `pandas` & `numpy`: For high-performance data manipulation.
- `matplotlib` & `seaborn`: For creating thesis-standard visualizations.
- `requests`: To handle any additional metadata fetching.
- `os` & `csv`: For file system management and data logging.

## ⚙️ How to Use
1. Ensure the dataset (CSV) from the `ambil-data-repo.ipynb` stage is available.
2. Run the cells sequentially to see the step-by-step transformation from raw data to visual charts.
3. The output plots can be exported for inclusion in the "Results and Discussion" (Bab 4) of the thesis.

---
**Status:** Completed - Main Analysis & Visualization Stage
