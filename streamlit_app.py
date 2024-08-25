import streamlit as st

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
    }

    /* Header styling */
    .header {
        background-color: #2E7D7D;  /* Muted teal for a calm appearance */
        color: white;
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
        color: white;
        padding: 8px 15px;
        text-decoration: none;
        font-size: 18px;
    }
    .navbar a:hover {
        background-color: #FFA726;  /* Orange hover effect */
        color: white;
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

# Main content
st.markdown("## Overview")
st.markdown("Welcome to the Mpox Dashboard. Use the tools below to explore and analyze Mpox-related tweets.")

# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Mpox Tweets", "100,000")
col2.metric("Total Cases in Austin", "50")

# Content Boxes
st.markdown("### List of Keywords")
st.markdown("<div class='stMarkdown'>- **Monkey**: 3000 last month, 10,000 total</div>", unsafe_allow_html=True)
st.markdown("<div class='stMarkdown'>- **Pox**: 3000 last month, 10,000 total</div>", unsafe_allow_html=True)
st.markdown("<div class='stMarkdown'>- **Quarantine**: 3000 last month, 10,000 total</div>", unsafe_allow_html=True)
st.markdown("<div class='stMarkdown'>- **Crazy**: 3000 last month, 10,000 total</div>", unsafe_allow_html=True)

# Map and Graphs placeholders
col3, col4 = st.columns([2, 1])
with col3:
    st.markdown("<div class='stMarkdown'>Geographic location of the tweets in Austin (Placeholder for Map)</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='stMarkdown'>Frequency of tweets over time by topic (Placeholder for Graph)</div>", unsafe_allow_html=True)

# Footer Links
st.markdown("### Learn more:")
st.markdown("[Link to our paper](#)", unsafe_allow_html=True)
