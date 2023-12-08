import streamlit as st

with open('AutoML_3_results/README.md') as infile:
    st.markdown(infile.read())