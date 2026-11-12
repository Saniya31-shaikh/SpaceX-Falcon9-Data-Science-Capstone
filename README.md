# SpaceX Falcon 9 Landing Prediction — Data Science Capstone

**IBM Data Science Professional Certificate | Coursera**

## Project Overview

This project was completed as part of the IBM Data Science Capstone course on Coursera. The objective is to analyze historical SpaceX Falcon 9 launch data and develop machine learning models to predict booster landing classifications.

The project covers data collection, preprocessing, SQL analysis, exploratory data analysis, geospatial visualization, interactive dashboard development, and machine learning.

## Dataset

I worked with two datasets:

**1. Historical SpaceX Launch Dataset (2010–2020)**

- 90 Falcon 9 launch records
- 18 columns after adding the target variable
- Includes launch site, payload mass, orbit, booster information, and landing outcome
- Used for SQL analysis, EDA, geospatial visualization, dashboard development, and machine learning

**2. Wikipedia Web-Scraped Dataset (2025)**

- 165 launch records
- Extracted from a Wikipedia Falcon 9 launch table
- Cleaned and organized using Python and Pandas
- Used to demonstrate web scraping and data preparation

The historical dataset was obtained from IBM's course-hosted data after the direct SpaceX API request encountered a connection error.

The binary target variable, `Class`, follows the labeling convention used in the course dataset. Class 1 includes some records without confirmed landing outcomes and should not be interpreted as a count of verified successful landings.

## Tools and Technologies

- **Programming:** Python
- **Data Processing:** Pandas, NumPy
- **Database Analysis:** SQLite, SQL
- **Visualization:** Matplotlib, Seaborn, Plotly Express
- **Geospatial Analysis:** Folium
- **Dashboard Development:** Plotly Dash
- **Machine Learning:** Scikit-learn
- **Development Environments:** Google Colab, Jupyter Notebook, VS Code
- **Version Control:** GitHub

## Project Workflow

### 1. Data Collection

Explored the SpaceX API and prepared the historical Falcon 9 launch dataset for analysis.

### 2. Web Scraping

Extracted launch information from Wikipedia and cleaned the resulting records into a structured dataset.

### 3. SQL Analysis

Used SQL queries to investigate launch-site distributions, payload characteristics, booster reuse, and landing classifications.

### 4. Exploratory Data Analysis

Created visualizations to examine relationships between payload mass, launch site, orbit, flight number, booster characteristics, and landing classification.

### 5. Geospatial Analysis

Developed interactive Folium maps showing launch-site locations, geographical clusters, classification distributions, and the distance between Florida launch sites.

### 6. Interactive Dashboard

Built a Plotly Dash application with:

- Launch-site dropdown filter
- Landing-classification pie chart
- Payload-range slider
- Interactive scatter plot

### 7. Machine Learning

Implemented a machine learning workflow for predicting the binary landing classification, including feature preprocessing, model training, evaluation, and comparison.

## Exploratory Findings

The historical dataset contains 90 launch records from three launch sites.

| Launch Site | Total Launches | Class 1 Records |
|---|---:|---:|
| CCAFS SLC 40 | 55 | 47 |
| KSC LC 39A | 22 | 21 |
| VAFB SLC 4E | 13 | 11 |

Overall, 79 records belong to Class 1 and 11 records belong to Class 0.

KSC LC 39A had the highest proportion of Class 1 records in this dataset, approximately 95.45%.

These results describe the historical course dataset and should not be generalized to all SpaceX launches.

## Repository Structure

```text
SpaceX-Falcon9-Data-Science-Capstone/
│
├── notebooks/
│   ├── SpaceX_01_API_Data_Collection.ipynb
│   ├── 02_SpaceX_Web_Scraping.ipynb
│   ├── 03_SpaceX_SQL_Analysis.ipynb
│   ├── 04_SpaceX_EDA_Visualization.ipynb
│   ├── 05_SpaceX_Folium_Geospatial_Analysis (1).ipynb
│   ├── 06_SpaceX_Plotly_Dash_Dashboard.ipynb
│   └── 07_SpaceX_Machine_Learning.ipynb
│
├── data/
│   ├── spacex_launches_processed.csv
│   └── spacex_web_scraped_cleaned.csv
│
├── dashboard/
│   ├── spacex_dashboard.py
│   └── README.md
│
├── maps/
│   ├── spacex_launch_sites.html
│   ├── spacex_landing_clusters.html
│   ├── spacex_classification_map.html
│   ├── spacex_florida_distance.html
│   └── README.md
│
├── README.md
└── .gitignore
```

## Running the Project

### Jupyter Notebooks

The analysis notebooks can be opened using Google Colab or Jupyter Notebook.

Some notebooks require uploading the corresponding CSV files from the `data/` directory.

### Dash Application

Install the required packages:

```bash
pip install pandas plotly dash
```

Run the dashboard from the repository root:

```bash
python dashboard/spacex_dashboard.py
```

Open the following address in your browser:

`http://127.0.0.1:8050/`

## Limitations

- The historical analysis is based on a relatively small dataset of 90 records.
- The target classification follows IBM's course convention and does not always indicate a confirmed landing.
- The 2025 web-scraped dataset was analyzed separately and was not used for model training.
- Machine learning performance should be interpreted with consideration of class imbalance and dataset size.

## Acknowledgment

This project was
