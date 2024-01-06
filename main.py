import streamlit as st
import pandas as pd
import numpy as np

# importing data and performing basic analysis
faithful_data = pd.read_csv("faithful.csv")

faithful_data = faithful_data.drop("rownames", axis = 1)
faithful_data = faithful_data.dropna()
