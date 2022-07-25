
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

