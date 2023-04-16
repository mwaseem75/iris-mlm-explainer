
![](https://github.com/mwaseem75/iris-mlm-explorer/blob/main/irisMLMExp.gif)

# iris-mlm-explainer
This web application connects to InterSystems Cloud SQL, display a dashboard of all the trained models, and explains the workings of a fitted machine learning model. The dashboard provides interactive plots on model performance, feature importances, feature contributions to individual predictions, partial dependence plots, SHAP (interaction) values, visualisation of individual decision trees, etc.

The dashboard includes:
- SHAP values (i.e. what is the contribution of each feature to each individual prediction?)
- Permutation importances (how much does the model metric deteriorate when you shuffle a feature?)
- Partial dependence plots (how does the model prediction change when you vary a single feature?
- For Random Forests and xgboost models: visualization of individual trees in the ensemble.
- Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, PR AUC plot, etc
- For regression models: goodness-of-fit plots, residual plots, etc.

## Prerequisits
- You should have account with [InterSystems Cloud SQL](https://portal.sql-contest.isccloud.io/cloudservices). 
- You should have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally.
- You should have [Python3](https://www.python.org/downloads/) installed locally. 

## Running app locally 
1. Clone/git pull the repo into any local directory
```
https://github.com/mwaseem75/iris-mlm-explainer.git
```
2. Activate python environment venv:
Open terminal in the repository folder and call:
```
$ source venv/bin/activate
```
3. Run application
```
$ python3 expdash.py
```
