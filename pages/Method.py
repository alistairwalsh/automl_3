import streamlit as st

st.header('Method')

st.write('''The correlation matrices for each 61 participants was initially flattened and repeated correlations removed (i.e. the upper triangle), as well as
             the diagonal that represents the correlation of an area to itself which is always 1. Each participant was scanned at two timepoints - 90 days and 365 
            days and a TDT was administered at the time of the scan. Giving 122 examples of scans with corresponding TDT score from the affected hand. 
            Thus the total data for training was 122 rows x 6670 columns and targets for prediction and scoring were 122 corresponding TDT scores. A train-test 
            split of 75% was performed with sklearn and selection fo model, tuning of hyper parameteres and creation of additional features was 
            performed with 75% of the data, with 25% of the data held aside as validation data. The data was stratified by timepoint to ensure a similair 
            mix of 90 day and 365 day data in both training and validation data. This information about which timepoint data was from was not included in the training data 
            ''')

st.write('''A 5 fold cross validation was used in the training runs, meaning that models were trained and tuned on 80% of the avaiable training 
            data and tested on the remaining 20% to detect overfitting.  

''')

st.header('Results')

st.write('''
 LightGBM, Xgboost, CatBoost, NeuralNetwork, and RandomForest models were trained and evaluated. Feature selection was perrformed and golden features created.
         ''')

st.header('Discussion')

st.write('''
         Neural networks performed poorly, or at least inconsistently, compared to other types of models. This is not surprising given the limited amout of data
          for training and neural networks known poor performance without a large amount of training data. 
         ''')

st.image('ldb_performance_boxplot.png')

st.write('''As the plots including the Neural networks make it difficult to see the differences in the remaining models, neural networks will be excluded from 
         reporting in tables and images from this point on''')