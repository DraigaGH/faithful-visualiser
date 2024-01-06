import streamlit as st
import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt

# importing data and performing basic analysis
faithful_data = pd.read_csv("faithful.csv")

faithful_data = faithful_data.drop("rownames", axis = 1)
faithful_data = faithful_data.dropna()

# writing introduction and adding graph
st.write("This will be a basic analysis and visualisation of the faithful data set, built in with R.")
st.write("This data set contains 2 columns, one for the duration of a volcano's last eruption, and another for the " +  
         "length of time between eruptions. A plot of these variables can be found below.")

erputions = faithful_data["eruptions"]
waiting = faithful_data["waiting"]

fig, ax = plt.subplots()
ax.scatter(erputions, waiting)

st.pyplot(fig)
