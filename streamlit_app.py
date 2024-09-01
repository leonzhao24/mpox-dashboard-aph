import streamlit as st
import pandas as pd
# Set page configuration
st.set_page_config(page_title="Mpox Dashboard", layout="wide")
# Custom CSS for a natural theme and new font
st.markdown(
    """
    <style>
    /* General body styling */
    body {
        background-color: #F5F5F5;  /* Light beige background for a natural feel */
        font-family: 'Arial', sans-serif;  /* Clean, modern font */
        color: black;  /* Change text color to black */
    }
    /* Header styling */
    .header {
        background-color: #2E7D7D;  /* Muted teal for a calm appearance */
        color: black;  /* Change header text color to black */
        padding: 10px;
        text-align: center;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    /* Navigation bar styling */
    .navbar {
        background-color: #2E7D7D;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .navbar a {
        color: black;  /* Change navigation link color to black */
        padding: 8px 15px;
        text-decoration: none;
        font-size: 18px;
    }
    .navbar a:hover {
        background-color: #FFA726;  /* Orange hover effect */
        color: black;  /* Keep hover text color black */
        border-radius: 5px;
    }
    /* Box and Panel styling */
    .stMarkdown {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: black;  /* Ensure content box text is black */
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #F5F5F5;
    }
    /* Button styling */
    .stButton button {
        background-color: #2E7D7D;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #FFA726;  /* Orange hover effect */
    }
    /* Metric box styling */
    .stMetric {
        background-color: #E3F2FD;  /* Light blue background for metrics */
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 20px;
        text-align: center;
        color: black;  /* Ensure metric text is black */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Sidebar for Advanced Search
st.sidebar.markdown("## Advanced Search for Tweets")
with st.sidebar.form(key='advanced_search_form'):
    st.text_input("Key Terms", "")
    st.selectbox("Time period", options=["2020", "2021", "2022"], index=0)
    st.text_input("Topic Labels", "")
    st.slider("Engagement", 0, 100, 50)
    submit_button = st.form_submit_button(label="Submit advanced Search")
if submit_button:
    st.sidebar.write("Advanced search submitted.")
# Header
st.markdown("<div class='header'><h1>Mpox Dashboard</h1></div>", unsafe_allow_html=True)
# Navigation Bar with links to external pages
st.markdown("""
    <div class="navbar">
        <a href="https://example.com/our-methodology" target="_blank">Our Methodology</a>
        <a href="https://example.com/our-mission" target="_blank">Our Mission</a>
    </div>
    """, unsafe_allow_html=True)
# Load and process the data
file_path = "Copy of Copy of Book1.csv"
data = pd.read_excel(file_path)
# Metrics
total_tweets = len(data)
total_cases_in_austin = data['Location'].str.contains("Austin", case=False, na=False).sum()
col1, col2 = st.columns(2)
col1.metric("Total Mpox Tweets", total_tweets)
col2.metric("Total Cases in Austin", total_cases_in_austin)
# Analyze keywords
keywords = ["Monkey", "Pox", "Quarantine", "Crazy"]
keyword_counts = {kw: data['CleanedText'].str.contains(kw, case=False, na=False).sum() for kw in keywords}
# Content Boxes
st.markdown("### List of Keywords")
for keyword, count in keyword_counts.items():
    st.markdown(f"<div class='stMarkdown'>- **{keyword}**: {count} occurrences</div>", unsafe_allow_html=True)
# Display tweet counts per location
st.markdown("### Tweet Counts per Location")
location_counts = data['Location'].value_counts()
st.bar_chart(location_counts)
# Alternatively, show a table
st.dataframe(location_counts.reset_index().rename(columns={'index': 'Location', 'Location': 'Tweet Count'}))
# Load and display the data
st.markdown("### Data Table")
st.dataframe(data)
# Footer Links
st.markdown("### Learn more:")
st.markdown("[Link to our paper](#)", unsafe_allow_html=True)