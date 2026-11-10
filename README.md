# Unemployment Analysis with Python

## CodeAlpha Data Science Internship – Task 2

## Project Overview

Unemployment is an important economic indicator that reflects the employment situation of a country. This project focuses on analyzing unemployment trends in India using Python and data analysis techniques.

The analysis explores unemployment patterns across different Indian states and rural and urban areas. It also investigates changes in unemployment rates during the COVID-19 period to understand how the pandemic affected employment trends.

## Objectives

- Analyze unemployment trends across different Indian states.
- Explore unemployment rates in rural and urban areas.
- Identify patterns and changes in unemployment over time.
- Investigate unemployment trends during the COVID-19 period.
- Visualize important findings using Python libraries.
- Generate meaningful insights from the datasets.

## Technologies Used

- **Programming Language:** Python
- **IDE:** Jupyter Notebook
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Data Analysis:** Exploratory Data Analysis (EDA)
- **Data Visualization:** Matplotlib and Seaborn

## Project Structure

```text
CodeAlpha_Unemployment_Analysis/
│
├── Dataset/
│   ├── Unemployment in India.csv
│   ├── Unemployment_Rate_upto_11_2020.csv
│   ├── unemployment_india_cleaned.csv
│   └── unemployment_rate_upto_nov2020_cleaned.csv
│
├── Notebooks/
│   └── CodeAlpha_Task2_Unemployment_Analysis.ipynb
│
├── src/
│   ├── 01_data_preprocessing.py
│   └── 02_unemployment_analysis.py
│
├── Reports/
│   └── CodeAlpha_Task2_Unemployment_Analysis_Report.pdf
│
├── Visualizations/
│   ├── monthly_trend.png
│   ├── rural_urban.png
│   └── state_average.png
│
└── README.md
```

## Dataset Description

The project uses two unemployment datasets containing information about India's employment situation.

**Dataset 1: Unemployment in India**
- Region
- Date
- Frequency
- Estimated Unemployment Rate (%)
- Estimated Employed
- Estimated Labour Participation Rate (%)
- Area (Rural/Urban)

**Dataset 2: Unemployment Rate up to November 2020**
- Region
- Date
- Frequency
- Estimated Unemployment Rate (%)
- Estimated Employed
- Estimated Labour Participation Rate (%)
- Region classification
- Longitude and Latitude

## Project Workflow

1. **Data Collection:** Load the unemployment datasets using Pandas.
2. **Data Preprocessing:** Inspect missing values, remove duplicate records, clean column names, and prepare the datasets for analysis.
3. **Exploratory Data Analysis:** Examine unemployment trends across regions and time periods.
4. **COVID-19 Analysis:** Compare unemployment rates before and during the COVID-19 period.
5. **Data Visualization:** Create charts to understand monthly trends, state-wise unemployment, and rural/urban differences.
6. **Insights:** Interpret the observed patterns and summarize the findings.

## Key Findings

- The datasets reveal variations in unemployment rates across Indian states.
- Rural and urban unemployment patterns show noticeable differences.
- The second dataset shows an increase in average unemployment rates during the selected COVID-19 period compared with January–February 2020.
- The analysis highlights the importance of understanding employment trends across different regions and time periods.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd CodeAlpha_Unemployment_Analysis
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Open Jupyter Notebook

```bash
jupyter notebook
```

### 5. Run the Notebook

Open the `CodeAlpha_Task2_Unemployment_Analysis.ipynb` file and execute the cells sequentially.

Ensure the datasets are placed in the expected directories before running the notebook.

## Project Deliverables

- Data preprocessing Python script.
- Unemployment analysis Python script.
- Jupyter Notebook containing the analysis.
- Original and cleaned datasets.
- Data visualization outputs.
- Project documentation in PDF format.

## Internship Information

**Organization:** CodeAlpha  
**Domain:** Data Science  
**Task:** Task 2 – Unemployment Analysis with Python

## Author

Developed as part of the CodeAlpha Data Science Internship program.

## Acknowledgement

I sincerely thank CodeAlpha for providing this opportunity to work on a real-world data analysis project and improve my practical skills in Python, data preprocessing, exploratory data analysis, and visualization.

---

**If you find this project useful, feel free to explore the repository!**
