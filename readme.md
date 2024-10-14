# Air Quality Analysis Project: All Station - With RFM Analysis & Clustering

## Live Dashboard

https://maliki-airquality.streamlit.app/

## Live Dashboard

d:/Data Analyst/Submission_Dicoding_AirQuality/
├─ Dashboard/
│ ├─ pages/
│ │ ├─ 1_main_pages.py
│ │ ├─ 2_cluster_pages.py
│ │ └─ 3_rfm_pages.py
│ ├─ clustering.csv
│ ├─ hello.py
│ ├─ main.csv
│ └─ rfm.csv
├─ Data/
│ ├─ PRSA_Data_Aotizhongxin_20130301-20170228.csv
│ ├─ PRSA_Data_Changping_20130301-20170228.csv
│ ├─ PRSA_Data_Dingling_20130301-20170228.csv
│ ├─ PRSA_Data_Dongsi_20130301-20170228.csv
│ ├─ PRSA_Data_Guanyuan_20130301-20170228.csv
│ ├─ PRSA_Data_Gucheng_20130301-20170228.csv
│ ├─ PRSA_Data_Huairou_20130301-20170228.csv
│ ├─ PRSA_Data_Nongzhanguan_20130301-20170228.csv
│ ├─ PRSA_Data_Shunyi_20130301-20170228.csv
│ ├─ PRSA_Data_Tiantan_20130301-20170228.csv
│ ├─ PRSA_Data_Wanliu_20130301-20170228.csv
│ └─ PRSA_Data_Wanshouxigong_20130301-20170228.csv
├─ img/
│ ├─ dicoding.gif
│ ├─ email.gif
│ ├─ linkedin.gif
│ └─ share.gif
├─ notebook.ipynb
├─ readme.md
└─ requirements.txt

## Project Overview

This project, submitted for the "Learn Data Analysis with Python" course from Dicoding, focuses on analyzing air quality data, particularly PM2.5 levels, from the Wanshouxigong station. The objective is to uncover trends, seasonal variations, and the impact of different weather conditions on air quality.

## Course Submission

This analysis serves as a course submission for "Learn Data Analysis with Python" offered by Dicoding. It demonstrates the application of data analysis techniques and visualization skills learned in the course.

## Table of Contents

- [Introduction](#introduction)
- [Data Source](#data-source)
- [Libraries Used](#libraries-used)
- [Key Insights](#key-insights)
- [How to Run the Dashboard](#how-to-run-the-dashboard)
- [About Me](#about-me)

## Introduction

The goal of this project is to analyze air quality data, and understand their relationship with various environmental factors. The analysis includes identifying trends, seasonal patterns, and correlations with weather conditions.

## Data Source

The dataset used in this project are made by Dicoding.

## Libraries Used

- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy
- Streamlit
- Altair

## Key Insights

This analysis will answer 4 Question such as:

- Apakah ketika cuaca hujan mengurangi jumlah polutan kotor dan meningkatkan jumlah polutan bersih?
- Bagaimana Peningkatan Frequency Rata-rata PM2.5 di sekitar Sebulan Terakhir, 6 bulan terakhir, 1 tahun terakhir, 5 tahun terakhir
  - Bagaimana Peningkatan Frequency Rata-rata PM10 di sekitar Sebulan Terakhir, 6 bulan terakhir, 1 tahun terakhir, 5 tahun terakhir
- Bulan apa yang memiliki jumlah polutan (SO2,NO2,CO,O3) tertinggi

and do advance analysis for RFM ANalysis and Clustering

## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:

   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name airQualityAdvance python=3.9
     conda activate airQualityAdvance
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv airQualityAdvance
     source airQualityAdvance/bin/activate  # On Windows use `airQualityAdvance\Scripts\activate`
     ```

2. **Install Required Packages**:

   - The following packages are necessary for running the analysis and the dashboard:

     ```
     pip install pandas numpy matplotlib seaborn streamlit
     ```

     or you can do

     ```
     pip install -r requirements.txt
     ```

### Run the Streamlit App

1. **Navigate to the Project Directory** where `hello.py` is located.

2. **Run the Streamlit App**:
   ```
   streamlit run dashboard/hello.py
   ```

### Additional Files

- The dataset used for this analysis is included in the project repository.
- A detailed Python notebook (`notebook.ipynb`) containing the data analysis and visualizations is also provided.

---

### P.S.

Since Dicoding recommended creating the good and tidy folder structures, as `hello.py` in `dashboard` folder, then the deployment for Streamlit App affected.

That was why I put the `requirements.txt` in the `dashboard` folder as well.

---

## About Me

- **Name**: Muhammad Tito Jaya Kusuma
- **Email Address**: mhmmdtjaya@gmail.com
- **Dicoding ID**: [titojayaaaa](https://www.dicoding.com/users/titojayaaaa/)

---

### Want to try your own analysis?📄

- [Get Dataset](https://www.kaggle.com/datasets/jhayyy/polutan-condition-in-chinese-station)
