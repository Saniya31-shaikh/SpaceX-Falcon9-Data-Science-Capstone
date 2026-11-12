# SpaceX Falcon 9 Data Science Capstone

This project was completed as part of the **IBM Data Science Professional Certificate Capstone** on Coursera.

The objective is to analyze historical SpaceX Falcon 9 launches and use machine learning to predict the first-stage landing classification. The project covers data collection, preprocessing, exploratory data analysis, SQL, interactive visualizations, geospatial analysis, and machine learning.

## Project Objectives

- Collect and prepare SpaceX launch data.
- Analyze launch sites, payload mass, orbit types, and booster characteristics.
- Explore patterns associated with landing classifications.
- Visualize launch locations using Folium.
- Develop an interactive dashboard using Plotly Dash.
- Train and evaluate machine learning classification models.

## Technologies Used

**Programming:** Python, SQL

**Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Folium, Scikit-learn

**Tools:** Google Colab, Jupyter Notebook, SQLite, VS Code, GitHub

**Dashboard:** Plotly Dash

## Dataset

The machine learning analysis uses the historical SpaceX Falcon 9 dataset provided through the IBM course.

| Dataset Information | Value |
|---|---|
| Historical records | 90 |
| Original features | 17 |
| Target column | Class |
| Class 0 records | 11 |
| Class 1 records | 79 |
| Historical period | 2010–2020 |
| Unique launch sites | 3 |

The target variable `Class` follows the IBM course's landing-outcome classification convention. Class 0 represents specified unsuccessful landing outcomes, while Class 1 represents the remaining outcomes under that convention. Class 1 should not be interpreted as independently verified successful landings in every case.

A separate dataset containing 165 launches from 2025 was collected through Wikipedia web scraping. This dataset was analyzed separately and was not used for machine learning training.

## Project Implementation

### Notebook 01 — SpaceX Data Collection and Preparation

- Worked with the historical SpaceX launch dataset.
- Examined the dataset structure and missing values.
- Converted date information into the appropriate format.
- Created the binary target variable `Class`.
- Saved the processed dataset as `spacex_launches_processed.csv`.

### Notebook 02 — Web Scraping

- Extracted SpaceX launch records from Wikipedia using Python.
- Cleaned launch dates, payload information, and landing outcomes.
- Processed 165 launch records from 2025.
- Saved the results as `spacex_web_scraped_cleaned.csv`.

### Notebook 03 — SQL Exploratory Data Analysis

Used SQLite and SQL queries to investigate:

- Launch frequency by site.
- Payload mass distribution.
- Landing classifications by launch site.
- Orbit characteristics.
- Booster reuse and flight history.

### Notebook 04 — Exploratory Data Analysis and Visualization

Used Pandas, Matplotlib, and Seaborn to analyze relationships between landing classifications and:

- Payload mass.
- Flight number.
- Launch site.
- Orbit type.
- Booster reuse.
- Booster block version.

Generated statistical visualizations and correlation analysis.

### Notebook 05 — Folium Geospatial Analysis

Created interactive maps to visualize Falcon 9 launch locations.

The project includes:

- Launch site location map.
- Landing classification map.
- Launch marker clustering.
- Florida launch site distance map.

The calculated distance between Kennedy Space Center LC-39A and Cape Canaveral SLC-40 was approximately **5.76 km**, based on the dataset coordinates.

The generated HTML maps are available in the `maps/` folder.

### Notebook 06 — Plotly Dash Dashboard

Developed a Python dashboard application for exploring Falcon 9 launch classifications.

Dashboard components include:

- Launch site selection dropdown.
- Classification distribution pie chart.
- Payload mass range slider.
- Interactive scatter plot.

The dashboard source code is available in `dashboard/spacex_dashboard.py`.

To run the dashboard locally, install the required dependencies and execute:

```bash
python dashboard/spacex_dashboard.py
```

The application is configured to run locally at `http://127.0.0.1:8050/`.

### Notebook 07 — Machine Learning Prediction

The final notebook focuses on building and evaluating classification models.

**Data preparation**

- Selected nine predictor variables.
- Excluded outcome-related and identifier fields to reduce potential data leakage.
- Used an 80% training and 20% testing split.
- Applied stratified sampling to preserve class proportions.
- Used preprocessing pipelines for numerical and categorical features.

**Machine learning algorithms**

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Decision Tree
4. K-Nearest Neighbors (KNN)

Hyperparameter tuning was performed using GridSearchCV with five-fold stratified cross-validation. Balanced accuracy was used for model selection because the dataset is imbalanced.

## Machine Learning Results

### Cross-Validation Results

| Model | CV Balanced Accuracy |
|---|---:|
| Decision Tree | 0.837 |
| Support Vector Machine | 0.679 |
| Logistic Regression | 0.656 |
| K-Nearest Neighbors | 0.618 |

The **Decision Tree** achieved the highest cross-validation balanced accuracy and was selected by the training-stage model selection procedure.

### Held-Out Test Results

| Model | Accuracy | Balanced Accuracy | ROC-AUC |
|---|---:|---:|---:|
| Logistic Regression | 0.833 | 0.906 | 0.906 |
| K-Nearest Neighbors | 0.833 | 0.688 | 0.656 |
| Support Vector Machine | 0.722 | 0.625 | 0.875 |
| Decision Tree | 0.667 | 0.594 | 0.766 |

Although Decision Tree performed best during cross-validation, **Logistic Regression achieved the highest balanced accuracy on the held-out test set**.

### Selected Decision Tree Evaluation

| Evaluation Metric | Result |
|---|---:|
| Training CV Balanced Accuracy | 0.837 |
| Test Accuracy | 0.667 |
| Test Balanced Accuracy | 0.594 |
| Test ROC-AUC | 0.766 |
| Test Average Precision (Class 1) | 0.958 |

The Decision Tree confusion matrix was:

| Actual / Predicted | Class 0 | Class 1 |
|---|---:|---:|
| Class 0 | 1 | 1 |
| Class 1 | 5 | 11 |

The evaluation included a confusion matrix, ROC curve, precision-recall curve, and model comparison chart.

## Key Findings

- The historical dataset contains substantially more Class 1 observations than Class 0 observations.
- Launch site, payload mass, and booster characteristics were explored as potential predictors.
- Decision Tree achieved the strongest balanced accuracy during training cross-validation.
- Logistic Regression performed better on the held-out test set.
- The differences between cross-validation and test results demonstrate the importance of evaluating models on unseen data.
- Results should be interpreted cautiously because the dataset contains only 90 records, including 11 Class 0 observations.

## Repository Structure

```text
SpaceX-Falcon9-Data-Science-Capstone/
|
|-- dashboard/
|   |-- README.md
|   |-- spacex_dashboard.py
|
|-- data/
|   |-- spacex_launches_processed.csv
|   |-- spacex_web_scraped_cleaned.csv
|
|-- maps/
|   |-- README.md
|   |-- spacex_classification_map.html
|   |-- spacex_florida_distance.html
|   |-- spacex_landing_clusters.html
|   |-- spacex_launch_sites.html
|
|-- notebooks/
|   |-- 01_SpaceX_Data_Collection.ipynb
|   |-- 02_SpaceX_Web_Scraping.ipynb
|   |-- 03_SpaceX_SQL_EDA.ipynb
|   |-- 04_SpaceX_EDA_Visualization.ipynb
|   |-- 05_SpaceX_Folium_Geospatial_Analysis.ipynb
|   |-- 06_SpaceX_Plotly_Dash_Dashboard.ipynb
|   |-- 07_SpaceX_Machine_Learning.ipynb
|
|-- .gitignore
|-- README.md
```

*Notebook filenames above represent the intended organization; actual uploaded filenames may differ.*

## Conclusion

This capstone project provided practical experience with the complete data science workflow, from data preparation and analysis to visualization and machine learning.

The machine learning experiments demonstrated that model selection results can differ from performance on unseen data, particularly when working with a small, imbalanced dataset.

The project helped strengthen my understanding of Python, SQL, exploratory data analysis, data visualization, machine learning pipelines, cross-validation, and classification evaluation.

## Author

**Saniya Shaikh**

MCA Student | Data Science and Machine Learning

**Course:** IBM Data Science Professional Certificate — Applied Data Science Capstone

**Platform:** Coursera
