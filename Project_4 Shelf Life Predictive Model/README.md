## Shelf life Predictive Model

# Overview

1.	To analyze the dataset to identify key factors affecting the shelf life of food products
2.	To develop a predictive model that can estimate the shelf life based on the identified factors    
3.	To validate the model’s accuracy and reliability in predicting product condition 

# Features

This data is sourced from in house data collection throughout the 2023 calendar year through an electronic data collection system. The is pulled using an approved API and loaded in CSV format and stored in a shared folder. The dataset consists of 7,495 records with 17 features related to product details, production and sample dates, quality indicators, and conditions affecting shelf life.

Variables:
Record Number -> Unique identifier  -> int
Date / Time -> Date and time the record was entered -> date / time
Location -> Location of meat production and sample collection -> categorical
Type -> Type of muscle cut 'Bone In' or 'Boneless' -> categorical
Product -> Product type of the muscle cut sampled -> categorical
Production_Date -> Date of meat production - date
Sample_Date -> Date of shelf life sample - date
Age -> Age of product at time of sample - int
TPC_Value -> TPC Micro result in LOG - int
Packaging_Condition -> Condition of packaging at time of sample -> categorical
Purge -> Grade of Purge in packaging at time of sample -> categorical
Odor -> Grade of odor at time of sample -> categorical
Color -> Grade of coor at time of sample -> categorical 
Surface -> Grade of surface texture at time of sample - categorical 
Product_condition -> Overall assessment of product at the time of sample - categorical 

## Method

1) Data Processing / Cleansing
2) Exploratory Data Analysis
3) Model Selection
4) Model Train / Test
5) Validation / Conclusion

## Analysis / Conclusion

**Model Selection**
Log regression and SVC models were found to have the highest accuracy rating with each model performing exceptionally well
	•	Logistic Regression - 0.96
	•	SVC Model - 0.97

**Model Train / Test**
	•	Decision boundary is used on the SVC Model to plot TPC values and Age by target Product Condition
 	•	ROC Curve for LOG Regression displays the percentage of true positives predicted by the model with an AUC = 0.99

  **Interpretation of Results**
  	•	High Accuracy: Both the logistic regression and SVC Models were able to predict with high accuracy. Each model achieves above 95% accuracy indicating effective classification of data correctly most of the time
   •	Good Precision and Recall: Both models present high precision and high recall scores. High precision relates to the low false positive rate, and high recall relates to the low false negative rate
  •	Balance: Both metrics are above 95% for each model used, showing that the models are well-balanced in identifying both positive and negative classes

