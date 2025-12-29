# 🎵 Song Popularity Prediction Project
This project builds a data-driven machine learning application to predict the popularity of songs based on their audio features and streaming platform presence.

In addition to prediction, the project provides interpretable insights into which factors most strongly influence streaming success.

The project is deployed as a multi-page Streamlit app: [https://song-popularity-app.streamlit.app/]

## 🛠️ Project Structure

```text
song-popularity/
├── Home.py                  # Landing page for the Streamlit app
├── pages/
│   ├── 1_Predict.py
│   ├── 2_Insights.py
│   └── 3_About.py
├── app/
│   └── random_forest_log_model.pkl   # Final saved model
├── images/
│   └── (EDA & feature importance plots)    
├── notebook/
│   └── Song_popularity.ipynb      # Model development in notebook
└── README.md
```

# 🚀 Project Objectives
- Predict the number of Spotify streams for a song using structured song metadata
- Analyze which features drive song popularity
- Provide actionable insights for data, marketing, and product teams
- Deploy the final model using an interactive Streamlit web app

# 📊 Tech Stack
```
Languages: Python
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, joblib, streamlit
Deployment: Streamlit web app 
Modeling:
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
Source: Top Spotify Songs 2023 (Kaggle)
```
# 🧹 Data Cleaning & Preprocessing
Key preprocessing steps include:
- Converting string-based numeric columns (e.g. playlist counts) to integers
- Handling missing values (e.g. filling missing musical keys)

Encoding categorical features:
- Musical key encoded using LabelEncoder
- Mode converted to binary (Major = 1, Minor = 0)
- Removing outliers and invalid rows
- Dropping text columns (track & artist names)

# 🔍 Exploratory Data Analysis (EDA)
The EDA focuses on answering key questions such as:
- How are streams distributed?
- Do audio features influence popularity?
- Does release timing matter?
- How strong is the effect of platform exposure?

# 📈 Modeling
Models are evaluated using:
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- R² Score
- Cross-validation

Random Forest and XGBoost perform best after log transformation.

# 🧠 Feature Importance 
Most important features from both Random Forest and XGBoost:
- Spotify playlist presence (dominant factor)
- Deezer playlists
- Release year
- Chart appearances

Key insight:

Platform visibility has a far greater impact on popularity than individual audio characteristics.

# 🖥️ Streamlit Application
The project is deployed as a multi-page Streamlit app, including:
- Predict Page
Input song features and receive estimated stream counts
- Insights Page
Visual explanations of EDA results and feature importance
- About Page
Project overview and methodology

The app uses a trained log-based Random Forest model for stream prediction.
