import streamlit as st

st.header('Introduction')

st.write('''
         Stroke rehabilitation is a critical domain in healthcare, aiming to restore and improve motor functions, independence, and overall quality of life for individuals affected by stroke. While traditional 
         approaches in rehabilitation have shown efficacy, recent advancements in machine learning, particularly neural networks, open new avenues for personalized and optimized interventions. 
         The demand for improved stroke rehabilitation methodologies is underscored by the need for solutions that consider the intricacies of each patient's condition and tailor interventions accordingly. 
         In this paper, we explore the intersection of
          machine learning and stroke rehabilitation, emphasizing the significance of data size, model complexity, and personalized treatment strategies in achieving enhanced outcomes for stroke survivors.
         
Artificial intelligence (AI) is a broader concept that refers to the development of computer systems capable of performing tasks that typically require human intelligence. Machine learning (ML) is a subset of AI, 
         focused on training algorithms to 
         learn patterns from data and make predictions or decisions without explicit programming. In essence, machine learning is a key technology within the field of artificial intelligence.
         Hyperparameter tuning involves optimizing the configuration settings, known as hyperparameters, of a machine learning model to achieve better performance. These hyperparameters are not learned from the 
         data but are set prior to the training process. The goal of hyperparameter tuning is to find the combination that results in the most effective and accurate model for a given task or dataset.

         The AAL Atlas (Automated Anatomical Labeling Atlas) is a widely used brain atlas in neuroimaging research. It provides a predefined set of anatomical regions, each associated with specific brain 
         structures or functional areas. Researchers use the AAL Atlas to partition the brain into distinct regions, facilitating the analysis and interpretation of neuroimaging data, particularly from 
         techniques like functional Magnetic Resonance Imaging (fMRI).

Correlation matrices constructed from fMRI scans represent the functional connectivity between different brain regions. In the context of fMRI, these matrices capture the degree to which the blood oxygen 
         level-dependent (BOLD) signal fluctuations in one brain region correlate with those in another. By examining these correlation patterns, researchers gain insights into the synchronized activity and 
         communication between different brain areas, aiding in the understanding of functional networks and neural processes.

         Neural networks typically require larger amounts of data compared to classical machine learning models. This is because neural networks, especially deep learning models, have a high number of 
         parameters that need to be optimized, and a large dataset helps prevent overfitting and allows the model to generalize well to unseen data.

         
The touch discrimination task in the context of sensory loss in stroke involves assessing an individual's ability to perceive and distinguish between different tactile stimuli. Stroke can lead to sensory 
         impairments, including changes in the ability to discriminate touch sensations. In the task, participants may be presented with various tactile stimuli, such as different textures, temperatures, 
         or pressure levels, and are asked to identify or discriminate between them.

This task aims to evaluate the extent of sensory deficits, particularly in terms of the precision and accuracy with which individuals can perceive and differentiate tactile stimuli. The findings from touch 
         discrimination tasks contribute valuable insights into the impact of stroke on sensory processing and inform rehabilitation strategies tailored to address specific sensory impairments.

Classical machine learning models, such as decision trees or linear regression, may perform reasonably well with smaller datasets, as they have fewer parameters and dependencies to learn.

In summary, neural networks often benefit from big datasets to effectively learn complex patterns and relationships, while some classical machine learning models can perform adequately with smaller datasets.
         ''')