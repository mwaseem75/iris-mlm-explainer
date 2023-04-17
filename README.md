
![](https://github.com/mwaseem75/iris-mlm-explorer/blob/main/irisMLMExp.gif)

# iris-mlm-explainer
This web application connects to InterSystems Cloud SQL, displays a dashboard of all the trained models, and explains the workings of a fitted machine learning model. The dashboard provides interactive plots on model performance, feature importances, feature contributions to individual predictions, partial dependence plots, SHAP (interaction) values, visualization of individual decision trees, etc.

The dashboard includes:
- SHAP values (i.e. what is the contribution of each feature to each individual prediction?)
- Permutation importance (how much does the model metric deteriorate when you shuffle a feature?)
- Partial dependence plots (how does the model prediction change when you vary a single feature?)
- For Random Forests and xgboost models: visualization of individual trees in the ensemble.
- Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, PR AUC plot, etc
- For regression models: goodness-of-fit plots, residual plots, etc.

# Prerequisits
- You should have an account with [InterSystems Cloud SQL](https://portal.sql-contest.isccloud.io/cloudservices). 
- You should have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally.
- You should have [Python3](https://www.python.org/downloads/) installed locally. 

# Getting Started
We will follow the below steps to create and view the explainer dashboard of a model :
- Step 1 : Close/git Pull the repo
- Step 2 : Activate python virtual environment 
- Step 3 : Set InterSystems Cloud SQL connection parameters
- Step 4 : Running Jupyter notebook
- Step 5 : Explore USA housing (for USA housing price Prediction)
- Step 6 : Create table and import data
- Step 7 : Create Model
- Step 8 : Train Model
- Step 9 : Validate Model
- Step 10 : Do a Prediction
- Step 11 : Explore the Explainer dashboard

## Step 1 : Close/git Pull the repo
So Let us start with first Step

Create folder and Clone/git pull the repo into any local directory
```
git clone https://github.com/mwaseem75/iris-mlm-explainer.git
```

## Step 2 : Activate python virtual environment 
Repository already contains python virtual environment folder (venv) along with all the required libraries.

All we need is to just activate the environment
On Unix or MacOS:
```
$ source venv/bin/activate
```
On Windows:
```
venv\scripts\activate
```
## Step 3 : Set InterSystems Cloud SQL connection parameters
Repo contains config.py file. Just open and set the parameters
![image](https://user-images.githubusercontent.com/18219467/232424168-3fd4ce14-2a78-44bc-a42b-c65909d9696a.png)

## Step 4 : Running Jupyter notebook
Repo contains USA_Housing_train.csv and USA_Housing_validate.csv files under datasets folder, from which we will create tables and import data.

We will use USAHousingModelNotebook.ipynb notebook for next steps.

Repo also contains Jupyter notebook. In order to run it, just run runnotebook.bat under venv environment
```
runnotebook
```
![image](https://user-images.githubusercontent.com/18219467/232427181-21b2c7e3-3de8-40fb-8111-4b86a9042039.png)

Navigate to [http://localhost:8888/](http://localhost:8888/) to run the notebook
open USAHousingModelNotebook.ipynb notebook by clicking on it
![image](https://user-images.githubusercontent.com/18219467/232428806-89ba6cd3-8e49-4001-ae0d-f1f8e6873540.png)

It will open the notebook
![image](https://user-images.githubusercontent.com/18219467/232428992-0d0fe003-b368-46af-a031-495992d93268.png)

**NOTE : Make sure to select venv kernal by selecting main menu Kernal>Change kernal>venv**, so that notebook will use virtual environment libraries

![image](https://user-images.githubusercontent.com/18219467/232429659-cb4366e9-c14d-41fd-8408-e8447cea4710.png)

NOTE : Run the cells in sequence by just clicking the small arrow
![image](https://user-images.githubusercontent.com/18219467/232431439-8aaa7eac-900b-4cc8-9cca-ec6a44bb7920.png)

## Step 5 : Explore USA housing (for USA housing price Prediction)
![image](https://user-images.githubusercontent.com/18219467/232433366-f3457c94-1272-4613-8c06-37e4d107d07c.png)

## Step 6 : Create table and import data
![image](https://user-images.githubusercontent.com/18219467/232434992-f519049b-2278-4e07-adbf-13fa35457bbd.png)

## Step 7 : Create Model
![image](https://user-images.githubusercontent.com/18219467/232435694-7986ab85-1e49-4f1d-b7dc-95259c162206.png)

## Step 8 : Train Model
![image](https://user-images.githubusercontent.com/18219467/232435922-2f84b59e-0f92-427c-b508-5e733353eadf.png)

## Step 9 : Validate Model
![image](https://user-images.githubusercontent.com/18219467/232436161-c7af4e06-8a70-4d2d-a0e9-3e90814d7051.png)
![image](https://user-images.githubusercontent.com/18219467/232436385-9df76a7c-fc0f-46d8-b5bf-3c062cc2b7e6.png)

## Step 10 : Do a Prediction
![image](https://user-images.githubusercontent.com/18219467/232437235-7ba99b14-3f72-47ab-b644-fd995c37cca8.png)

## Step 11 : Explore the Explainer dashboard
Finaly, run the below command in virtual environment to start our main application
```
python expdash.py
```
![image](https://user-images.githubusercontent.com/18219467/232438579-26fc0a30-9f95-4df1-81ef-7f24270316c5.png)

## Credits
This application is derived from the [isc-cloud-sql-python-demo](https://openexchange.intersystems.com/package/isc-cloud-sql-python-demo) template by @Evgeny Shvarov

Thanks
