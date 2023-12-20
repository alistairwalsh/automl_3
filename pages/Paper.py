import streamlit as st

st.header('Introduction')

st.write('''
         Stroke rehabilitation is a critical domain in healthcare, aiming to restore and improve brain functions, independence, and overall quality of life for individuals affected by stroke. While traditional 
         approaches in rehabilitation have shown efficacy, recent advancements in machine learning, particularly neural networks, open new avenues for personalized and optimized interventions. 
         The demand for improved stroke rehabilitation methodologies is underscored by the need for solutions that consider the intricacies of each patient's condition and tailor interventions accordingly. 
         In this paper, we explore the intersection of
          machine learning and stroke rehabilitation. In particular,  emphasizing the significance of data size, model complexity and hyper parameter tuning in stroke research.
        With the overall aim of predicting stroke recovery trajectories and the possibility of personalized treatment strategies to acheive enhanced outcomes for stroke survivors.
         
        Artificial intelligence (AI) is a broader concept that refers to the development of computer systems capable of performing tasks that typically require human intelligence. Machine learning (ML) is a subset of AI, 
         focused on training algorithms to 
         learn patterns from data and make predictions or decisions without explicit programming. In essence, machine learning is a key technology within the field of artificial intelligence.
         Hyperparameter tuning involves optimizing the configuration settings, known as hyperparameters, of a machine learning model to achieve better performance. These hyperparameters are not learned from the 
         data but are set prior to the training process. The goal of hyperparameter tuning is to find the combination that results in the most effective and accurate model for a given task or dataset.

        Correlation matrices constructed from fMRI scans represent the functional connectivity between different brain regions. In the context of fMRI, these matrices capture the degree to which the blood oxygen 
         level-dependent (BOLD) signal fluctuations in one brain region correlate with those in another. By examining these correlation patterns, researchers gain insights into the synchronized activity and 
         communication between different brain areas, aiding in the understanding of functional networks and neural processes.

        The AAL Atlas (Automated Anatomical Labeling Atlas) is a widely used brain atlas in neuroimaging research. It provides a predefined set of 116 anatomical regions, each associated with specific brain 
         structures or functional areas. Researchers use the AAL Atlas to partition the brain into distinct regions, facilitating the analysis and interpretation of neuroimaging data, particularly from 
         techniques like functional Magnetic Resonance Imaging (fMRI).

        The touch discrimination task (TDT) in the context of sensory loss in stroke involves assessing an individual's ability to perceive and distinguish between different tactile stimuli. Stroke can lead to sensory 
         impairments, including changes in the ability to discriminate touch sensations. In the task, participants may be presented with various tactile stimuli, such as different textures, temperatures, 
         or pressure levels, and are asked to identify or discriminate between them.

        This task aims to evaluate the extent of sensory deficits, particularly in terms of the precision and accuracy with which individuals can perceive and differentiate tactile stimuli. The findings from touch 
         discrimination tasks contribute valuable insights into the impact of stroke on sensory processing and inform rehabilitation strategies tailored to address specific sensory impairments.

        Neural networks typically require larger amounts of data compared to classical machine learning models. This is because neural networks, especially deep learning models, have a high number of 
         parameters that need to be optimized, and a large dataset helps prevent overfitting and allows the model to generalize well to unseen data.

        Classical machine learning models, such as decision trees or linear regression, may perform reasonably well with smaller datasets, as they have fewer parameters and dependencies to learn.

        In summary, neural networks often benefit from big datasets to effectively learn complex patterns and relationships, while some classical machine learning models can perform adequately with smaller datasets.
         ''')

st.header('Method')

st.write('''The correlation matrices for each of 61 participants was initially flattened and repeated correlations removed (i.e. the upper triangle), as well as
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
         
        A baseline score was established calculating the error when the mean score is used as a prediction for every case, this simplest of models is then a comparison for the performance of more complex models.
        LightGBM, Xgboost, CatBoost, NeuralNetwork, and RandomForest models were trained and evaluated. Feature selection was perrformed useing Permutation based feature importance, and golden features created.
         Golden Features are combinations and permutations of features from the dataset that a decision tree analysis suggest performed well.

        Neural networks performed poorly, or at least inconsistently, compared to other types of models and ofter performed worse than baseline. This is not surprising given the limited amout of data
          for training and neural networks known poor performance without a large amount of training data. 
         
        Light Gradient Boosting Machine (LightGBM) performed consistently well, to the point where an attempt at creating an ensemble from the avaialable trained models did no better that the LightGBM with feature selection and Golden features
         acheived on its own. 
         
        LightGBM is a Machine Learning library that provides algorithms which utilise a gradient boosting framework.
         This model essentially ignores a significant proportion of data with small gradients in favour of features with larger gradients as these features play a more important role in prediction accuracy.
         Gradient-based One-Side Sampling (GOSS) can obtain quite accurate estimation of the information gain with a much smaller data size. 
           ''')

st.image('ldb_performance_boxplot.png')

st.write('''
         The process of creating new features found combinations that performed well and warrant further exploration for their efficacy in directing rehabilitation efforts and prediction of likely recovery outcomes.
         The ratio of the correlation between the Temporal_Inf_R <=> Cerebelum_7b_L and the Frontal_Inf_Oper_L <=> Supp_Motor_Area_L and the difference in correlation between the Insula_R <=> Temporal_Sup_R and 
         Cerebelum_3_L <=> Vermis_1_2 contain information that is a valuable predictor across the majority of the group.
         ''')

st.image('23_LightGBM_GoldenFeatures_SelectedFeatures/permutation_importance.png', caption='Permutation-based Importance')
         
st.write(r'''@inproceedings{NIPS2017_6449f44a,
 author = {Ke, Guolin and Meng, Qi and Finley, Thomas and Wang, Taifeng and Chen, Wei and Ma, Weidong and Ye, Qiwei and Liu, Tie-Yan},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {I. Guyon and U. Von Luxburg and S. Bengio and H. Wallach and R. Fergus and S. Vishwanathan and R. Garnett},
 pages = {},
 publisher = {Curran Associates, Inc.},
 title = {LightGBM: A Highly Efficient Gradient Boosting Decision Tree},
 url = {https://proceedings.neurips.cc/paper_files/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf},
 volume = {30},
 year = {2017}
}
''')
       

st.header('Discussion')





st.write('''As the plots including the Neural networks make it difficult to see the differences in the remaining models, neural networks will be excluded from 
         reporting in tables and images from this point on''')

