import streamlit as st

st.title("Framework AI Product Ops")

st.write("People · Process · Data · Tech · Policy")

people = st.slider("People", 0, 5, 3)
process = st.slider("Process", 0, 5, 3)
data = st.slider("Data", 0, 5, 3)
tech = st.slider("Tech", 0, 5, 3)
policy = st.slider("Policy", 0, 5, 3)
