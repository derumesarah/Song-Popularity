import streamlit as st
from PIL import Image 
import os

st.set_page_config(page_title="Insights", layout="wide")

st.title("📊 Insights")
st.caption("Key findings from exploratory data analysis (EDA) and model interpretation")

st.markdown("""
This page summarizes the **most important patterns and relationships** found during the exploratory data analysis  
of the dataset. The goal is to translate data insights into **clear, actionable understanding**.
""")

st.marksown(---)

# 1. Distribution of streams
st.subheader("🎧 Overall Distribution of Streams")

st.image("images/Distribution streams.png", use_container_width=True)

st.write("""
The distribution of Spotify streams is **strongly right-skewed**:
- Most songs achieve relatively low stream counts
- A small number of songs reach extremely high values

**Implication:**  
This large variance justifies the **log-transformation** of streams used during model training,
as it stabilizes the learning process and prevents overemphasis on extreme outliers.
""")

st.markdown("---")
