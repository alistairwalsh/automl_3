import streamlit as st 

st.markdown('''# Summary of 23_LightGBM_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: regression
- **num_leaves**: 63
- **learning_rate**: 0.1
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.9
- **min_data_in_leaf**: 10
- **metric**: rmse
- **custom_eval_metric_name**: None
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
rmse

## Training time

2.2 seconds

### Metric details:
| Metric   |      Score |
|:---------|-----------:|
| MAE      |  12.653    |
| MSE      | 245.072    |
| RMSE     |  15.6548   |
| R2       |   0.440399 |
| MAPE     |   0.304021 |




''')

## Learning curves
st.images('23_LightGBM_GoldenFeatures_SelectedFeatures/learning_curves.png', caption='Learning curves')

## Permutation-based Importance
st.images('23_LightGBM_GoldenFeatures_SelectedFeatures/permutation_importance.png', caption='Permutation-based Importance')

## True vs Predicted
st.images('23_LightGBM_GoldenFeatures_SelectedFeatures/true_vs_predicted.png', caption='True vs Predicted')

## Predicted vs Residuals
st.images('23_LightGBM_GoldenFeatures_SelectedFeatures/predicted_vs_residuals.png', caption='Predicted vs Residuals')

