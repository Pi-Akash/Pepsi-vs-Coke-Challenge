import pandas as pd
import streamlit as st

filename = "Participant_Data.csv"

st.header(":floppy_disk: Data")
st.subheader("The page showcases all the participants information who have taken the challenge.")
filename = "Participant_Data.csv"
df = pd.read_csv(filename)
df["Result"] = df["Drink_Identified"] == df["Drink_Original"]

st.write("You can add/remove/edit records directly from your browser.")
df = st.data_editor(
    df, 
    num_rows = "dynamic",
    use_container_width = True
    )

df.to_csv(filename, index = False)

@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")

csv_df = convert_df(df)
st.write("You can download the data to your local by clicking on the button below :point_down:")
st.download_button(
    label = "Download data as CSV", 
    data = csv_df, 
    file_name="Pepsi_vs_Coke.csv",
    mime = "text/csv"
    )