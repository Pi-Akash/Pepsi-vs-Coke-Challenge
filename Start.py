import pandas as pd
import numpy as np
import streamlit as st

home_page = st.Page("1_🏠_Home.py", title = "Home")
data_page = st.Page("2_💾_Data.py", title = "Data")
visual_page = st.Page("3_💹_Insights.py", title = "Insights")
start = st.navigation([home_page, data_page, visual_page])


if __name__ == "__main__":
    start.run()