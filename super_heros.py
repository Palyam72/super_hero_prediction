import pandas as pd
import streamlit as st
import numpy as np

# Set page config
st.set_page_config(
    page_title="Super Hero Finder",
    page_icon="🦸‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add title and description
st.title("Super Hero Finder")
st.write("Find your favorite super hero based on their abilities!")
column1,column2=st.columns([1,1])
with column1:
    st.image("logo.png", width=100)
with column2:
    st.header("Enter the values for the super hero abilities:")
    

# Create two columns
col1, col2 = st.columns(2)

# Streamlit inputs
with col1:
    intelligence = st.number_input("Enter the value for Intelligence")
    strength = st.number_input("Enter the value for Strength")
    speed = st.number_input("Enter the value for Speed")

with col2:
    combat = st.number_input("Enter the value for Combat")
    durability = st.number_input("Enter the value for Durability")
    power = st.number_input("Enter the value for Power")

alignment = st.selectbox("Whether you want to know about a good character or a bad character", ["good", "bad"])

# Load the data
file_path = 'preprocessed_super_heros_DataFrame.csv'
data = pd.read_csv(file_path)

# Ensure numerical columns are properly converted to numeric types
numerical_columns = ["Intelligence", "Strength", "Speed", "Combat", "Durability", "Power", "Total"]
data[numerical_columns] = data[numerical_columns].apply(pd.to_numeric, errors='coerce')

# User input
user_input = [intelligence, strength, speed, combat, durability, power]

# Calculate Euclidean distance
distances = []
for index, row in data.iterrows():
    hero_input = row[numerical_columns[:-1]].tolist()
    distance = np.linalg.norm(np.array(user_input) - np.array(hero_input))
    distances.append(distance)

# Find the indices of the heroes with the smallest distances
comparision_results = np.argsort(distances)[:5]

# Filter by alignment
final_result = data.iloc[comparision_results][data.iloc[comparision_results]["Alignment"] == alignment]

# Display the result
st.header("Top 5 matching super heroes:")
st.dataframe(final_result)
