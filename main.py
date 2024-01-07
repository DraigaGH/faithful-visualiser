import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# importing data and performing basic analysis
faithful_data = pd.read_csv("faithful.csv")

faithful_data = faithful_data.drop("rownames", axis = 1)
faithful_data = faithful_data.dropna()

# writing introduction and adding graph
st.write("This will be a basic analysis and visualisation of the faithful data set, built in with R.")
st.write("This data set contains 2 columns, one for the duration of a volcano's last eruption, and another for the " +  
         "length of time between eruptions. A plot of these variables can be found below.")

eruptions = faithful_data["eruptions"]
waiting = faithful_data["waiting"]

initial_plot, x1 = plt.subplots()
x1.scatter(eruptions, waiting)

st.pyplot(initial_plot)

# adding second interactive plot
st.write("The relation seems to be linear. Let's model it using linear regression.")

placeholder = st.empty()

# we create a container so that the slider can be shown below the graph
main_plot_container = st.container()
alpha_slider = st.slider("α", 0.0, 10.0, 1.0)
main_plot, x2 = plt.subplots()

model = linear_model.Ridge(alpha = alpha_slider)

print(model)

x2.scatter(eruptions, waiting)
x2.scatter([1], [alpha_slider])
main_plot_container.pyplot(main_plot)
