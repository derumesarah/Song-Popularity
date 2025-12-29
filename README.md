# 🎵 Song-Popularity
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
│   └── (EDA & feature importance plots)   # All visualizations 
├── notebook/
│   └── Song_popularity.ipynb      # Model development in notebook
└── README.md

# 🚀 Project Objectives
- Predict the number of Spotify streams for a song using structured song metadata
- Analyze which features drive song popularity
- Provide actionable insights for data, marketing, and product teams
- Deploy the final model using an interactive Streamlit web app

# 📊 Tech Stack
Languages: Python
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, joblib, streamlit
Deployment: Streamlit web app 
Modeling:
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
Source: Top Spotify Songs 2023 (Kaggle)

# 
