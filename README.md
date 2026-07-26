# ⚽ FIFA Player Analytics

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.x-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Supported-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A comprehensive **Sports Analytics** project built entirely with **Jupyter Notebooks**. This repository explores FIFA player data through data cleaning, feature engineering, exploratory analysis, interactive visualizations, machine learning, clustering, explainable AI, and similarity search.

---

# Table of Contents

* Overview
* Features
* Repository Structure
* Technologies
* Dataset
* Installation
* Quick Start
* Notebook Guide
* Machine Learning Pipeline
* Visualizations
* Results
* Future Improvements
* Contributing
* License

---

# Overview

Modern football clubs rely heavily on analytics for:

* Talent scouting
* Wage optimization
* Transfer valuation
* Squad building
* Youth development
* Contract decisions

This project demonstrates how data science techniques can be applied to player data to generate actionable insights and predictive models.

---

# Features

* Comprehensive data cleaning workflow
* Feature engineering
* Statistical analysis
* Exploratory data analysis
* Interactive Plotly visualizations
* Market value prediction
* Wage prediction
* Player clustering
* Explainable AI using SHAP
* Player similarity recommendation engine
* Publication-ready figures
* Reproducible notebook workflow

---

# Repository Structure

```text
fifa-player-analytics/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── Makefile
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_dataset_overview.ipynb
│   ├── 02_data_cleaning_preprocessing_updated.ipynb
│   ├── 03_feature_engineering_updated.ipynb
│   ├── 04_exploratory_data_analysis.ipynb
│   ├── 05_interactive_visualizations.ipynb
│   ├── 06_market_value_prediction.ipynb
│   ├── 07_player_clustering.ipynb
│   ├── 08_model_explainability.ipynb
│   ├── 09_player_similarity_engine.ipynb
│   └── 10_final_report.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   ├── modeling.py
│   ├── clustering.py
│   ├── similarity.py
│   ├── explainability.py
│   └── utils.py
│
├── models/
├── reports/
    ├──figures/
    ├──tables/
```

---

# Technologies

## Programming

* Python
* Jupyter Notebook

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Plotly

## Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM

## Explainable AI

* SHAP

## Statistics

* SciPy
* Statsmodels

---

# Dataset

The project is designed for publicly available FIFA player datasets.

Typical columns include:

* Name
* Age
* Nationality
* Club
* Overall Rating
* Potential
* Preferred Foot
* Height
* Weight
* Position
* Wage
* Market Value
* Crossing
* Finishing
* Heading Accuracy
* Short Passing
* Long Passing
* Dribbling
* Ball Control
* Vision
* Sprint Speed
* Stamina
* Strength
* Aggression
* Reactions
* Composure

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Subiswas36218/fifa-player-analytics.git
cd fifa-player-analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter:

```bash
jupyter lab
```

---

# Notebook Guide

## Notebook 01

Dataset Overview

Topics

* Data loading
* Dataset shape
* Column inspection
* Missing values
* Memory usage
* Descriptive statistics

---

## Notebook 02

Data Cleaning

* Duplicate removal
* Missing values
* Unit conversion
* Data normalization
* Data validation

---

## Notebook 03

Feature Engineering

Creates engineered features such as:

* Technical Score
* Physical Score
* Mental Score
* Offensive Score
* Defensive Score
* Passing Score
* Wage-to-Value Ratio
* Growth Potential
* Age Group

---

## Notebook 04

Exploratory Data Analysis

Answers questions including:

* Which countries produce the highest-rated players?
* Which clubs own the most valuable squads?
* Which positions earn the highest wages?
* How does age affect market value?
* Which attributes correlate most strongly with player ratings?

---

## Notebook 05

Interactive Dashboard

Includes:

* Scatter plots
* Bubble charts
* Treemaps
* Sunburst charts
* Radar charts
* Correlation heatmaps
* Geographic visualizations

---

## Notebook 06

Market Value Prediction

Algorithms:

* Linear Regression
* Random Forest
* Gradient Boosting
* XGBoost
* LightGBM

Evaluation Metrics:

* MAE
* RMSE
* R²

---

## Notebook 07

Player Clustering

Techniques:

* PCA
* UMAP
* K-Means
* DBSCAN
* HDBSCAN (optional)

Goal:

Identify player archetypes based on technical and physical attributes.

---

## Notebook 08

Explainable AI

Interpret model predictions using:

* SHAP Summary Plots
* Feature Importance
* Permutation Importance
* Partial Dependence Plots

---

## Notebook 09

Player Similarity Engine

Find players with similar profiles using feature embeddings and distance metrics.

Supports:

* Cosine Similarity
* Euclidean Distance
* PCA projection

---

## Notebook 10

Final Report

Contains:

* Executive Summary
* Key Findings
* Business Insights
* Recruitment Recommendations
* Youth Development Analysis
* Future Work

---

# Machine Learning Pipeline

```text
Raw Data
    │
    ▼
Data Cleaning
    │
    ▼
Feature Engineering
    │
    ▼
EDA
    │
    ▼
Visualization
    │
    ▼
Model Training
    │
    ▼
Evaluation
    │
    ▼
Explainability
    │
    ▼
Similarity Engine
```

---

# Example Questions Answered

* Which attributes most influence market value?
* Which players are underpaid relative to performance?
* Which clubs have the strongest squads?
* Which nations produce elite talent?
* Which young players have the highest potential?
* Which players are statistically similar?

---

# Expected Outputs

* Publication-quality figures
* Interactive dashboards
* Trained regression models
* Cluster visualizations
* SHAP explanations
* Similarity recommendations
* Analytical report

---

# Skills Demonstrated

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Data Visualization
* Statistical Analysis
* Regression
* Clustering
* Explainable AI
* Recommendation Systems
* Sports Analytics
* Reproducible Research
* Notebook Storytelling

---

# Future Improvements

* Deep learning models
* Time-series analysis across FIFA editions
* Transfer value forecasting
* Salary optimization
* Interactive Streamlit dashboard
* Player career trajectory prediction
* Team chemistry analysis
* Tactical role classification

---

# Contributing

Contributions are welcome.

Suggested workflow:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request with a clear description.

---

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# Acknowledgements

Thanks to the football analytics and open data communities for making player datasets publicly available for research and educational purposes.