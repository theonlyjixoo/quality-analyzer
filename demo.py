import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def calculate_project_quality(analysis_df, repo_df, weight_smell=0.5, weight_sustain=0.3, weight_stability=0.2):
    """Menghitung persentase kualitas proyek berdasarkan code smell, popularitas, dan stabilitas."""
    results = []
    
    for _, row in analysis_df.iterrows():
        total_lines = row['total_line_count']
        bad_smells = row['total_bad_smells']
        project_name = row['Folder']
        total_files = row['num_files']
        
        # Cari informasi tambahan dari fixed_df
        repo_info = repo_df[repo_df['full_name'].str.contains(project_name, na=False, case=False)]
        repo_url = repo_info['html_url'].values[0] if not repo_info.empty else "Unknown"
        default_branch = repo_info['default_branch'].values[0] if not repo_info.empty else "Unknown"
        
        stargazers = repo_info['stargazers_count'].values[0] if not repo_info.empty else 0
        watchers = repo_info['watchers_count'].values[0] if not repo_info.empty else 0
        open_issues = repo_info['open_issues_count'].values[0] if not repo_info.empty else 0
        forks = repo_info['forks_count'].values[0] if not repo_info.empty else 0
        
        if total_lines == 0:
            maintainability_score = 100  # Jika tidak ada kode, dianggap sempurna
        else:
            smell_ratio = (bad_smells / total_lines) * 100
            maintainability_score = max(0, 100 - smell_ratio)  # Skor minimum 0%

        created_at = repo_info['created_at'].values[0] if not repo_info.empty else 0
        pushed_at = repo_info['pushed_at'].values[0] if not repo_info.empty else 0

        created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        pushed_date = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ")

        days_since_creation = (pushed_date - created_date).days
        alpha = 0.1
        beta = 0.9

        sustainability_score = (alpha * (stargazers / max(100,days_since_creation)) + beta * (watchers / max(100,days_since_creation)))* 100  # Normalisasi skor
        stability_score = max(0, 100 - (open_issues / (open_issues + 1) * 100))  # Semakin sedikit open issues, semakin tinggi skornya
        
        # Hitung total kualitas proyek berdasarkan bobot
        quality_score = (
            (maintainability_score * weight_smell) + 
            (sustainability_score * weight_sustain) + 
            (stability_score * weight_stability)
        )
        
        results.append({
            'Project': project_name,
            'days since create': days_since_creation,
            'Total Lines': total_lines,
            'Bad Smells': bad_smells,
            'Stargazers': stargazers,
            'Watchers': watchers,
            'Open Issues': open_issues,
            'Maintainability Score (%)': round(maintainability_score, 2),
            'Sustainability Score (%)': round(sustainability_score, 2),
            'Stability Score (%)': round(stability_score, 2),
            'Overall Quality Score (%)': round(quality_score, 2)
        })
    
    return pd.DataFrame(results)

# Load dataset
grouped_analysis_results_path = "D:/S2/Tesis/code/grouped_analysis_results.csv"
fixed_df_path = "D:/S2/Tesis/code/fixed_df.csv"

grouped_analysis_results = pd.read_csv(grouped_analysis_results_path)
fixed_df = pd.read_csv(fixed_df_path)
fixed_df['full_name'] = fixed_df['full_name'].str.replace('/', '_')

# Hitung kualitas proyek
quality_df = calculate_project_quality(grouped_analysis_results, fixed_df)

pd.set_option("display.max_columns", None)  # Menampilkan semua kolom
pd.set_option("display.width", 100)  # Menyesuaikan lebar tampilan
pd.set_option("display.max_rows", None)  # Menampilkan semua baris jika diperlukan

# Tampilkan hasil
print(quality_df.head())

# Tampilkan 5 proyek dengan kualitas terbaik & terburuk
print("\nTop 5 Proyek dengan Kualitas Terbaik:")
print(quality_df.sort_values(by="Overall Quality Score (%)", ascending=False).head(5))

print("\nTop 5 Proyek dengan Kualitas Terburuk:")
print(quality_df.sort_values(by="Overall Quality Score (%)", ascending=True).head(5))

# Simpan hasil validasi ke file CSV
output_csv_path = "D:/S2/Tesis/code/validated_results.csv"
quality_df.to_csv(output_csv_path, index=False)
print(f"\n✅ Hasil validasi telah disimpan dalam {output_csv_path}")