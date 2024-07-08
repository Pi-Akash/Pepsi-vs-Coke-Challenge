import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics import confusion_matrix
import plotly.express as px

st.header(":chart: Insights")

df = pd.read_csv("Participant_Data.csv")

st.subheader("Overall Summary:")
st.write("- Total Number of Observations : ", df.shape[0])
st.write("- Total unique challengers : ", len(df["Participant_Name"].unique()))
st.write("- Total Correct identifications : ", df[df["Result"] == True].shape[0])

st.subheader("Plots")
drinks = ["Pepsi", "Coke", "Diet Coke", "Dr. Pepper"]

st.write(":round_pushpin: Confusion Matrix : ")
# overall results
data = confusion_matrix(df["Drink_Identified"], df["Drink_Original"])
fig = px.imshow(data,
                labels = dict(x = "Identified", y = "Original"),
                x = drinks, y = drinks,
                text_auto = True, aspect = "auto")
st.plotly_chart(fig)

st.write(":round_pushpin: Most Mis-identified drinks:")
temp_df = df[df["Result"] == False]["Drink_Original"].value_counts().reset_index()
fig = px.bar(temp_df, x = "Drink_Original", y = "count", title = "Most mis-identified drinks.")
st.plotly_chart(fig)

st.write(":round_pushpin: Most Identified drinks:")
temp_df = df[df["Result"] == True]["Drink_Identified"].value_counts().reset_index()
fig = px.bar(temp_df, x = "Drink_Identified", y = "count", title = "Most identified drinks.")
st.plotly_chart(fig)