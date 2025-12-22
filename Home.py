import streamlit as st

st.set_page_config(
    page_title="Song Popularity App",
    layout="wide"
)

st.title("🎵 Song Popularity Prediction App")

st.markdown("""
Welcome! 
This project was build to predict the popularity of a song based on its audio features and platform presence.
Use the sidebar to navigate between pages:
- **Predict** – predict streams
- **Insights** – project insights
---
""")
