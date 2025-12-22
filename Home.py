import streamlit as st

st.set_page_config(
    page_title="Song Popularity App",
    layout="wide"
)

st.title("🎵 Song Popularity Prediction App")
st.caption("Predict estimated stream counts based on song data + audio features.")

st.markdown("---")

st.subheader("👋 Welcome!")
st.write(
    "This project was build to help you estimate the expected number of streams for a song" 
)

st.info("👉 Use the **sidebar** (left) to switch between pages anytime.")

st.markdown("### 🧾 What you can do here")
st.markdown("""
- **Predict**: Enter song attributes and get an estimated stream count.
- **Insights**: Learn which patterns and features drive a song’s popularity on streaming platforms
""") 
