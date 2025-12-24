import streamlit as st


st.set_page_config(page_title="Insights", layout="wide")

st.title("📊 Insights")
st.caption("Key findings from exploratory data analysis (EDA) and model interpretation")

st.markdown("""
This page summarizes the **most important patterns and relationships** found during the exploratory data analysis  
of the dataset. The goal is to translate data insights into **clear, actionable understanding**.
""")

st.markdown("---")


# 1. Feature Importance 

st.subheader("🎧 Feature Importance")

st.image("images/Top 10 features Random Forest.png", width=1000)
st.image("images/Top 10 features XGBRegressor.png", use_container_width=True)

st.write("""
Both models agree on the main drivers:

**Most important feature by far**
- `in_spotify_playlists`

**Secondary contributors**
- `in_deezer_playlists`
- `released_year`
- Platform chart presence

**Key Insight:**  
While musical features add nuance, **platform visibility is the dominant factor**
in predicting streaming success.
""")

st.markdown("---")


# 2. Platform presence 

st.subheader("📲 Platform Exposure & Playlist Presence")

st.image("images/Scatterplot platform popularity.png", use_container_width=True)

st.write("""
Looking at different platforms:
- Songs included in more **Spotify playlists** tend to have much higher streams
- Apple Music and Deezer playlists show similar, though weaker, effects

**Key Insight:**  
Again, visibility on streaming platforms is a **major driver of popularity**, especially on Spotify.
""")

st.markdown("---")


# 3. Audio feautures

st.subheader("🎚️ Audio Features and Popularity")

st.image("images/Scatterplot song features.png", use_container_width=True)

st.write("""
Audio features such as **danceability, valence, and energy** show:
- No strong linear relationship with streams
- High-stream songs tend to fall into **mid-to-high ranges**

**Key Insight:**  
Audio features alone do not determine popularity, but they **contribute in combination**
with platform-related variables.
""")

st.markdown("---")


# 4. Correlation Matrix

st.subheader("🔗 Feature Correlations")

st.image("images/Correlation matrix.png", use_container_width=True)

st.write("""
Key correlation findings:
- Streams correlate strongly with:
  - `in_spotify_playlists`
  - `in_spotify_charts`
  - `in_apple_playlists`
- Audio features such as **acousticness** and **instrumentalness** show
  weak or negative relationships with popularity

This supports the idea that **platform exposure outweighs pure musical attributes**.
""")

st.markdown("---")


# 5. Seasonal effects

st.subheader("📅 Seasonal Effects: Release Month")

st.image("images/Average streams by month.png", use_container_width=True)

st.write("""
Average streams vary noticeably across release months:
- **January and September** show the highest average streams
- **February and December** show significantly lower averages

This may reflect:
- Industry release cycles
- Marketing strategies of major artists
- Seasonal listening behavior

**Key Insight:**  
Higher streams may be associated with certain months, but the release month 
itself does not directly cause a song’s popularity.
""")

st.markdown("---")

# 8. Final Takeaways

st.subheader("✅ Key Takeaways")

st.success("""
• **Platform exposure**, especially Spotify playlists, dominates all other factors  
• Audio features matter, but mostly **in combination**, not isolation  
• Release timing can influence average performance, but should not be over-interpreted  
""")

st.caption("These insights directly inform the model used on the Predict page.")
