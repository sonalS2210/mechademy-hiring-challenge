
# Mechademy Intern Hiring Challenge

A complete end to end data modelling solution for prediction of Radial Vibration using sensor data from a set of equipments/machine.

The project involved multiple steps:
- Uploading mongo data dump
- Data extraction and building
- Feature engineering 
- Regression modelling.

## Task Description

| Files Provide |
|------|
|data_dump.rar|

* A specific **screenshot** of **sensor data from mongodb** had been sent as an input data initial format.
* This dump had to be **restored** on a local mongo db server
* Intial dataset preperation using pymongo for EDA and data cleaning.
* Creating a regression based Model for predicting **Radial Vibratrion**


### Mongo Data Extraction

1. Restore the data dump to local mongodb server on system.
2. Verify the documents in Mongo GUI.
3. Multiple Documents of a single sensor data were present, which had to be stipulated into single columns
    3.1. <img width="949" alt="Screenshot 2022-07-25 185203" src="https://user-images.githubusercontent.com/96237008/180787805-11a7e404-68eb-446c-9a8b-546b1cefa93d.png">
4. Furnish a notebook for csv data creation for EDA and modelling preperation.


### Feature Analysis
- The data had various sensor information of:
    - Power
    - Current
    - Shaft Speed
    - Pressure 
    - Temperature
    - Flow 
- The data was sampled at every 15 seconds and spanned of Jan 2018 to Jan 2020.

# Modelling

- Various modelling methods were used like:
    - Linear regression
    - Regularized Regression(Elastic Net)
    - Xgboost
    - Knn regressor

- Initial modelling gave moderate results with avergae error with 12-20%.
- Drift based evaluation of target variable showed that there was both gradual drift and recurrent drifts in data.

- ![image](https://user-images.githubusercontent.com/96237008/180780206-c9e62b44-ce61-481c-a71d-4580e1a258a9.png)


- Filterred the target column on basis of dates after which the main drift occured.
- Modelling on the new filtter data gave an everage error of 3-7%

### Modelling Result
|Model| mae | mse | r2|
|----|----|----|----|
| Linear regression|0.1608|0.0411|0.5453|
| XGB regessor| 0.1215| 0.0243| 0.7309 |
| KNN regressor | 0.115| 0.0217|0.7607|


## Acknowledgements

 - [Drifting in data](https://www.analyticsvidhya.com/blog/2021/10/mlops-and-the-importance-of-data-drift-detection/)
 - [Hyoerparameter tuning](https://www.kaggle.com/code/btyuhas/bayesian-optimization-with-xgboost/notebook)
 - [KNN regressor](https://www.kaggle.com/code/junkal/selecting-the-best-regression-model/notebook)
 - [KNN Elbow Method](https://www.analyticsvidhya.com/blog/2018/08/k-nearest-neighbor-introduction-regression-python/)



