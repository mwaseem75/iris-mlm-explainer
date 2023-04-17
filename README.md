
![](https://github.com/mwaseem75/iris-mlm-explorer/blob/main/irisMLMExp.gif)

# iris-mlm-explainer
This web application connects to InterSystems Cloud SQL, display a dashboard of all the trained models, and explains the workings of a fitted machine learning model. The dashboard provides interactive plots on model performance, feature importances, feature contributions to individual predictions, partial dependence plots, SHAP (interaction) values, visualisation of individual decision trees, etc.

The dashboard includes:
- SHAP values (i.e. what is the contribution of each feature to each individual prediction?)
- Permutation importances (how much does the model metric deteriorate when you shuffle a feature?)
- Partial dependence plots (how does the model prediction change when you vary a single feature?)
- For Random Forests and xgboost models: visualization of individual trees in the ensemble.
- Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, PR AUC plot, etc
- For regression models: goodness-of-fit plots, residual plots, etc.

# Prerequisits
- You should have account with [InterSystems Cloud SQL](https://portal.sql-contest.isccloud.io/cloudservices). 
- You should have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally.
- You should have [Python3](https://www.python.org/downloads/) installed locally. 

# Getting Started
We will follow the below steps to create and view explainer dashboard of a model :
- Step 1 : Close/git Pull the repo
- Step 2 : Activate python virtual environment 
- Step 3 : Set InterSystems Cloud SQL parameters
- Step 4 : Explore USA housing (for USA housing price Prediction)
- Step 5 : Create table and import data
- Step 6 : Create Model
- Step 7 : Train Model
- Step 8 : Validate Model
- Step 9 : Do Prediction
- Step 10 : Explore Explainer dashboard

## Step 1 : Close/git Pull the repo
So Let us start with first Step

Create folder and Clone/git pull the repo into any local directory
```
git clone https://github.com/mwaseem75/iris-mlm-explainer.git
```

## Step 2 : Activate python virtual environment 
Repository already contains python virtual environment folder (venv) along with all the required libraries.
All we need is to just activate the environment
```
$ source venv/bin/activate
```
3. Run application
```
$ python3 expdash.py
```
