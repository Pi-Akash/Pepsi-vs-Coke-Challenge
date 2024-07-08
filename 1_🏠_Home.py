import pandas as pd
import streamlit as st
import os

st.header("Pepsi :beers: Coke")
st.subheader("Hello! Welcome to Pepsi vs Coke Challenge")
st.write("Please insert the information in the below form to record observations.")

filename = "Participant_Data.csv"
if os.path.exists(filename):
    df = pd.read_csv(filename)
else:
    df = pd.DataFrame({
            "Participant_Name" : "Dummy",
            "Round" : "Dummy",
            "Drink_Identified" : "Dummy",
            "Drink_Original" : "Dummy",
            "Confidence" : 0.0
        })
    df.to_csv(filename, index = [0])

with st.form("PVC_Form"):
    # participants name
    participant_name = st.text_input("Enter Participants Name:", value = None)
    
    # round number
    round_number = st.radio(
        label = "Please select Round : ", 
        options = ["Round 1", "Round 2", "Round 3"]
        )

    # Drink Identified
    drink_identified = st.radio(
        label = "Please select Drink which Participant identified: :beer:",
        options = ["Pepsi", "Coke", "Diet Coke", "Dr. Pepper"]
    )

    # Drink Original
    drink_original = st.radio(
        label = "Please select Drink which was given to Participant: :beer:",
        options = ["Pepsi", "Coke", "Diet Coke", "Dr. Pepper"]
    )

    # Confidence
    confidence_level = st.number_input(
        label = "How confident the participant is?"
    )

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        new_row = {
            "Participant_Name" : participant_name,
            "Round" : round_number,
            "Drink_Identified" : drink_identified,
            "Drink_Original" : drink_original,
            "Confidence" : confidence_level
        }
        df = pd.concat([df, pd.DataFrame(new_row, index = [0])], ignore_index = True)
        df.to_csv(filename, index = False)
        st.balloons()
        st.success("Data inserted successfully.")