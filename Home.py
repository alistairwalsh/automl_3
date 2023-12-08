import streamlit as streamlit

with open('AutoML_3_results/README.md') as infile:
    st.markdown(infile.read())