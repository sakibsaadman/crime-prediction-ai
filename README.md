# Crime Prediction using Artificial Intelligence

## Overview

This project was developed as part of the **Discipline-Specific AI Project** module. The aim of the project is to build an **AI-based crime prediction system for West Yorkshire** using historical police crime data. The system analyses crime records, applies machine learning techniques, compares multiple models, and predicts crime type based on selected features.

The project uses a complete machine learning workflow including data preprocessing, feature engineering, model training, evaluation, visualisation, and advanced optimisation techniques.

---

## Project Aim

To develop an artificial intelligence based crime prediction system for West Yorkshire using historical police data, in order to identify crime patterns and support proactive decision making.

---

## Objectives

- Collect and combine 12 months of West Yorkshire police crime data
- Clean, preprocess, and prepare the dataset for machine learning
- Engineer useful temporal and spatial features
- Split the dataset into training, validation, and testing sets
- Build a baseline **Decision Tree** model
- Develop and compare **Random Forest**, **Support Vector Machine**, and **CNN** models
- Evaluate models using **Accuracy**, **F1 Score**, **Confusion Matrix**, **ROC**, and **AUC**
- Apply **feature selection**, **hyperparameter tuning**, and **cross validation**
- Build an additional advanced model such as **Neural Network** or **XGBoost**
- Select the final best-performing model
- Create visualisations and a prediction pipeline for the final prototype

---

## Team Roles

### Sakib Saadman  
**Project Lead / Scrum Master**  
- Coordinated tasks and monitored project progress  
- Managed sprints and workflow using Jira  
- Maintained GitHub repository and project organisation  
- Oversaw integration of all project components  

### Muhammad Shaukat  
**Data Analyst and Research Lead**  
- Collected and prepared the dataset  
- Performed preprocessing and feature engineering  
- Supported exploratory analysis and visual analytics  

### Hira Naib  
**Model Developer and Documentation Lead**  
- Developed and evaluated machine learning models  
- Supported technical documentation and reporting  
- Contributed to ethics and compliance considerations  

### Client / Stakeholder  
**Kieran Townsend, FALL**  
- Provided project feedback  
- Reviewed milestones and prototype outcomes  

---

## Dataset

The dataset used in this project is based on **West Yorkshire police crime data for 2025**.  
It contains information such as:

- Crime type  
- Location  
- Latitude and longitude  
- Month  
- Outcome information  

The dataset was combined from multiple monthly CSV files into a single dataset for processing and analysis.

---

## Methodology

The project follows an **Agile methodology** with iterative development through sprints. Work was divided into manageable stages, and progress was monitored regularly using Jira and GitHub.

### Main workflow
1. Data collection and combination  
2. Data cleaning and preprocessing  
3. Feature engineering  
4. Train / validation / test split  
5. Model development  
6. Model evaluation  
7. Advanced optimisation  
8. Final model selection  
9. Prediction pipeline and prototype output  

---

## Models Used

The following models were developed and compared:

- **Decision Tree**  
- **Random Forest**  
- **Support Vector Machine (SVM)**  
- **Convolutional Neural Network (CNN)**  

### Advanced section
- **Feature Selection**
- **SMOTE for class balancing**
- **Hyperparameter tuning**
- **Neural Network**
- **XGBoost**
- **Cross validation**

---

## Evaluation Metrics

The models were evaluated using:

- Accuracy  
- F1 Score  
- Classification Report  
- Confusion Matrix  
- ROC Curve  
- AUC Score  

These metrics were used to compare the models and identify the best-performing approach for the final system.

---

## Features of the Final Notebook

The final notebook includes:

- Single upload point for combined CSV dataset  
- Data inspection and preparation  
- Monthly crime trend visualisation  
- Crime type heatmap  
- Baseline and advanced machine learning models  
- Model comparison table  
- Accuracy and F1 comparison charts  
- Pie chart showing success percentages  
- ROC curves and confusion matrices  
- Feature selection and SMOTE  
- Hyperparameter tuning and XGBoost  
- Prediction pipeline for new input values  

---

## Repository Structure

```text
Crime-Prediction-AI/
│
├── data/
│   └── Combined CSV dataset or source files
│
├── notebooks/
│   └── Crime Prediction.ipynb
│
├── images/
│   └── charts, screenshots, diagrams
│
├── docs/
│   └── reports, presentation files, supporting documents
│
├── README.md
└── requirements.txt
