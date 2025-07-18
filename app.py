import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder

st.title("✅ Streamlit Setup Test")

st.markdown("If you see this, your environment is working! 🎉")

st.write("TensorFlow version:", tf.__version__)
st.write("Pandas version:", pd.__version__)
st.write("NumPy version:", np.__version__)
