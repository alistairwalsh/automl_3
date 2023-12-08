import streamlit as st

st.markdown('''
| Best model   | name                                                                                                               | model_type     | metric_type   |   metric_value |   train_time |   single_prediction_time |
|:-------------|:-------------------------------------------------------------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|-------------------------:|
|              | [1_Default_LightGBM](1_Default_LightGBM/README.md)                                                                 | LightGBM       | rmse          |        20.8802 |       359.17 |                   7.2528 |
|              | [2_Default_Xgboost](2_Default_Xgboost/README.md)                                                                   | Xgboost        | rmse          |        21.0542 |       398.91 |                   7.0758 |
|              | [3_Default_CatBoost](3_Default_CatBoost/README.md)                                                                 | CatBoost       | rmse          |        21.1623 |      5937.15 |                   7.9031 |
|              | [4_Default_NeuralNetwork](4_Default_NeuralNetwork/README.md)                                                       | Neural Network | rmse          |        45.6435 |       437    |                   4.6103 |
|              | [5_Default_RandomForest](5_Default_RandomForest/README.md)                                                         | Random Forest  | rmse          |        21.5598 |       663.11 |                   7.3164 |
|              | [10_LightGBM](10_LightGBM/README.md)                                                                               | LightGBM       | rmse          |        21.2921 |       318.76 |                   7.144  |
|              | [6_Xgboost](6_Xgboost/README.md)                                                                                   | Xgboost        | rmse          |        21.0385 |       411.18 |                   7.084  |
|              | [14_CatBoost](14_CatBoost/README.md)                                                                               | CatBoost       | rmse          |        21.194  |      6341.69 |                   7.9407 |
|              | [18_RandomForest](18_RandomForest/README.md)                                                                       | Random Forest  | rmse          |        21.3399 |       573.33 |                   7.2818 |
|              | [22_NeuralNetwork](22_NeuralNetwork/README.md)                                                                     | Neural Network | rmse          |        65.8275 |       448.96 |                   4.8031 |
|              | [11_LightGBM](11_LightGBM/README.md)                                                                               | LightGBM       | rmse          |        20.9617 |       343.69 |                   7.0348 |
|              | [7_Xgboost](7_Xgboost/README.md)                                                                                   | Xgboost        | rmse          |        21.226  |       419.76 |                   7.1905 |
|              | [15_CatBoost](15_CatBoost/README.md)                                                                               | CatBoost       | rmse          |        21.3664 |      6479.17 |                   8.2723 |
|              | [19_RandomForest](19_RandomForest/README.md)                                                                       | Random Forest  | rmse          |        20.8596 |       559.84 |                   7.5127 |
|              | [19_RandomForest_GoldenFeatures](19_RandomForest_GoldenFeatures/README.md)                                         | Random Forest  | rmse          |        20.8555 |       627.35 |                   7.7939 |
|              | [1_Default_LightGBM_GoldenFeatures](1_Default_LightGBM_GoldenFeatures/README.md)                                   | LightGBM       | rmse          |        19.3684 |       350.68 |                   7.5617 |
|              | [11_LightGBM_GoldenFeatures](11_LightGBM_GoldenFeatures/README.md)                                                 | LightGBM       | rmse          |        19.5927 |       346.27 |                   7.633  |
|              | [1_Default_LightGBM_GoldenFeatures_RandomFeature](1_Default_LightGBM_GoldenFeatures_RandomFeature/README.md)       | LightGBM       | rmse          |        19.2729 |       355.92 |                   7.5849 |
|              | [1_Default_LightGBM_GoldenFeatures_SelectedFeatures](1_Default_LightGBM_GoldenFeatures_SelectedFeatures/README.md) | LightGBM       | rmse          |        15.8603 |         2.58 |                   0.2998 |
|              | [19_RandomForest_GoldenFeatures_SelectedFeatures](19_RandomForest_GoldenFeatures_SelectedFeatures/README.md)       | Random Forest  | rmse          |        20.0925 |         2.83 |                   0.3148 |
|              | [6_Xgboost_SelectedFeatures](6_Xgboost_SelectedFeatures/README.md)                                                 | Xgboost        | rmse          |        21.037  |         2.17 |                   0.1356 |
|              | [4_Default_NeuralNetwork_SelectedFeatures](4_Default_NeuralNetwork_SelectedFeatures/README.md)                     | Neural Network | rmse          |        22.558  |         3.93 |                   0.1685 |
| **the best** | [23_LightGBM_GoldenFeatures_SelectedFeatures](23_LightGBM_GoldenFeatures_SelectedFeatures/README.md)               | LightGBM       | rmse          |        15.6548 |         2.53 |                   0.3155 |
|              | [24_LightGBM_GoldenFeatures](24_LightGBM_GoldenFeatures/README.md)                                                 | LightGBM       | rmse          |        19.153  |       359.58 |                   7.4443 |
|              | [25_RandomForest_GoldenFeatures_SelectedFeatures](25_RandomForest_GoldenFeatures_SelectedFeatures/README.md)       | Random Forest  | rmse          |        20.0925 |         2.89 |                   0.3201 |
|              | [26_RandomForest_GoldenFeatures](26_RandomForest_GoldenFeatures/README.md)                                         | Random Forest  | rmse          |        20.8555 |       559.83 |                   8.0123 |
|              | [27_Xgboost_SelectedFeatures](27_Xgboost_SelectedFeatures/README.md)                                               | Xgboost        | rmse          |        21.037  |         2.42 |                   0.1919 |
|              | [28_Xgboost_SelectedFeatures](28_Xgboost_SelectedFeatures/README.md)                                               | Xgboost        | rmse          |        21.037  |         2.42 |                   0.1444 |
|              | [29_Xgboost](29_Xgboost/README.md)                                                                                 | Xgboost        | rmse          |        21.0527 |       408.67 |                   7.4142 |
|              | [30_Xgboost](30_Xgboost/README.md)                                                                                 | Xgboost        | rmse          |        21.0488 |       414.92 |                   7.0018 |
|              | [31_CatBoost](31_CatBoost/README.md)                                                                               | CatBoost       | rmse          |        21.2881 |      6305.28 |                   7.9402 |
|              | [32_LightGBM_GoldenFeatures_SelectedFeatures](32_LightGBM_GoldenFeatures_SelectedFeatures/README.md)               | LightGBM       | rmse          |        15.9167 |         2.6  |                   0.2835 |
|              | [33_LightGBM_GoldenFeatures_SelectedFeatures](33_LightGBM_GoldenFeatures_SelectedFeatures/README.md)               | LightGBM       | rmse          |        15.6548 |         2.67 |                   0.2844 |
|              | [34_LightGBM_GoldenFeatures_SelectedFeatures](34_LightGBM_GoldenFeatures_SelectedFeatures/README.md)               | LightGBM       | rmse          |        15.7616 |         2.66 |                   0.2857 |
|              | [35_LightGBM_GoldenFeatures_SelectedFeatures](35_LightGBM_GoldenFeatures_SelectedFeatures/README.md)               | LightGBM       | rmse          |        15.8603 |         2.58 |                   0.286  |
|              | [36_RandomForest_GoldenFeatures_SelectedFeatures](36_RandomForest_GoldenFeatures_SelectedFeatures/README.md)       | Random Forest  | rmse          |        20.0925 |         2.95 |                   0.3087 |
|              | [37_RandomForest_GoldenFeatures_SelectedFeatures](37_RandomForest_GoldenFeatures_SelectedFeatures/README.md)       | Random Forest  | rmse          |        20.004  |         2.97 |                   0.3081 |
|              | [38_RandomForest_GoldenFeatures_SelectedFeatures](38_RandomForest_GoldenFeatures_SelectedFeatures/README.md)       | Random Forest  | rmse          |        20.0925 |         2.97 |                   0.3053 |
|              | [39_RandomForest_GoldenFeatures_SelectedFeatures](39_RandomForest_GoldenFeatures_SelectedFeatures/README.md)       | Random Forest  | rmse          |        20.004  |         3.01 |                   0.3094 |
|              | [40_Xgboost_SelectedFeatures](40_Xgboost_SelectedFeatures/README.md)                                               | Xgboost        | rmse          |        21.9875 |         2.3  |                   0.2    |
|              | [41_Xgboost_SelectedFeatures](41_Xgboost_SelectedFeatures/README.md)                                               | Xgboost        | rmse          |        19.6178 |         2.36 |                   0.2021 |
|              | [42_Xgboost_SelectedFeatures](42_Xgboost_SelectedFeatures/README.md)                                               | Xgboost        | rmse          |        21.9596 |         2.48 |                   0.146  |
|              | [43_Xgboost_SelectedFeatures](43_Xgboost_SelectedFeatures/README.md)                                               | Xgboost        | rmse          |        19.6178 |         2.52 |                   0.1817 |
|              | [48_NeuralNetwork_SelectedFeatures](48_NeuralNetwork_SelectedFeatures/README.md)                                   | Neural Network | rmse          |        21.5829 |         3.99 |                   0.1665 |
|              | [49_NeuralNetwork_SelectedFeatures](49_NeuralNetwork_SelectedFeatures/README.md)                                   | Neural Network | rmse          |        21.6049 |         4    |                   0.1683 |
|              | [50_NeuralNetwork](50_NeuralNetwork/README.md)                                                                     | Neural Network | rmse          |        22.3208 |       438.55 |                   4.7116 |
|              | [51_NeuralNetwork](51_NeuralNetwork/README.md)                                                                     | Neural Network | rmse          |        97.3493 |       437.84 |                   4.7767 |
|              | [Ensemble](Ensemble/README.md)                                                                                     | Ensemble       | rmse          |        15.6548 |         0.11 |                   0.3057 |


''')

### AutoML Performance
st.image('ldb_performance.png', caption='AutoML Performance')

### AutoML Performance Boxplot
st.image('ldb_performance_boxplot.png', caption='AutoML Performance Boxplot')

### Features Importance
st.image('features_heatmap.png', caption='features importance across models')

### Spearman Correlation of Models
st.image('correlation_heatmap.png', caption='models spearman correlation')

with open('golden_features.json') as infile:
    st.json(infile.read())