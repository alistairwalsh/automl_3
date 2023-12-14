import streamlit as st

st.header('Method')

st.markdown('''The correlation matrices for each 61 participants was initially flattened and repeated correlations removed (i.e. the upper triangle), as well as
             the diagonal that represents the correlation of an area to itself which is always 1. Each participant was scanned at two timepoints - 90 days and 365 
            days and a TDT was administered at the time of the scan. Giving 122 examples of scans with corresponding TDT score from the affected hand. 
            Thus the total data for training was 122 rows x 6670 columns and targets for prediction and scoring were 122 corresponding TDT scores. A train-test 
            split of 75% was performed with sklearn and selection fo model, tuning of hyper parameteres and creation of additional features was 
            performed with 75% of the data, with 25% of the data held aside as validation data. The data was stratified by timepoint to ensure a similair 
            mix of 90 day and 365 day data in both training and testing. This information about which timepoint data was from was not included in the training data 
            ''')