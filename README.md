![image](https://user-images.githubusercontent.com/18219467/233314974-71c44cf3-8abd-4f92-b550-9f5f578ac331.png)
# iris-mlm-explainer
This web application connects to InterSystems Cloud SQL to create, train, validate, and predict ML models, make Predictions and display a dashboard of all the trained models with an explanation of the workings of a fitted machine learning model.
The dashboard provides interactive plots on model performance, feature importances, feature contributions to individual predictions, partial dependence plots, SHAP (interaction) values, visualization of individual decision trees, etc.

The Application includes the following:
- Web Application to view the Prediction
- Web Application for explainer dashboard which includes the following:
  - SHAP values (i.e. what is the contribution of each feature to each individual prediction?)
  - Permutation importance (how much does the model metric deteriorate when you shuffle a feature?)
  - Partial dependence plots (how does the model prediction change when you vary a single feature?)
  - For Random Forests and xgboost models: visualization of individual trees in the ensemble.
  - Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, PR AUC plot, etc
  - For regression models: goodness-of-fit plots, residual plots, etc.
- Jupyter Notebook to explore data, create, train, validate, and predict model

![](https://github.com/mwaseem75/iris-mlm-explorer/blob/main/irisMLMExp.gif)

# Prerequisits
- You should have an account with [InterSystems Cloud Service Portal](https://portal.sql-contest.isccloud.io/cloudservices). 
- You should have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally.
- You should have [Python3](https://www.python.org/downloads/) installed locally. 

# Getting Started
We will follow the below steps to create and view the explainer dashboard of a model :
- Step 1 : Close/git Pull the repo
- Step 2 : Login to InterSystems Cloud SQL Service Portal
  - Step 2.1 : Add and Manage Files
  - Step 2.2 : Import DDL and data files
  - Step 2.3 : Create Model
  - Step 2.4 : Train Model
  - Step 2.5 : Validate Model  
- Step 3 : Activate python virtual environment 
- Step 4 : Set InterSystems Cloud SQL connection parameters
- Step 5 : Run Web Application for prediction   
- Step 6 : Explore the Explainer dashboard

## Step 1 : Close/git Pull the repo
So Let us start with first Step

Create folder and Clone/git pull the repo into any local directory
```
git clone https://github.com/mwaseem75/iris-mlm-explainer.git
```

## Step 2 : Login to InterSystems Cloud SQL Service Portal
Login to [InterSystems Cloud Service Portal](https://portal.sql-contest.isccloud.io/cloudservices)
![image](https://user-images.githubusercontent.com/18219467/233755660-7a9dcf01-927e-4d5d-a901-2ef018c33876.png)
Select the running deployment
![image](https://user-images.githubusercontent.com/18219467/233755738-53ef3e59-c890-4d5b-8b7c-17fd0077fb3b.png)

## Step 2.1 : Add and Manage Files
Click on Add and Manage Files
![image](https://user-images.githubusercontent.com/18219467/233757122-0a976333-c448-4ad4-9925-10794a1c08ab.png)
Repo contains USA_Housing_tables_DDL.sql(DDL to create tables), USA_Housing_train.csv(Traning data) and USA_Housing_validate.csv(For validation) files under the datasets folder. Select upload button to add these files.
![AddFiles](https://user-images.githubusercontent.com/18219467/233757254-826532d4-7c86-4f87-a124-9a8d14ca2069.JPG)

## Setp 2.2 : Import DDL and data files
Click on Import files, then click on DDL or DML statemet(s) radio button, then click next button
![ImportDDL](https://user-images.githubusercontent.com/18219467/233757429-dde9ae1d-32ac-4417-97c5-f126c539a287.JPG)
Click on Intersystems IRIS radio button and then click on next
![IsIRIS](https://user-images.githubusercontent.com/18219467/233757466-94af3c32-e248-40da-9045-d0c94675c2f2.JPG)
Select USA_Housing_tables_DDL.sql file and then press import button
![ImportFileDDL](https://user-images.githubusercontent.com/18219467/233757496-2df03ecf-d038-42fb-9461-084b87c286f7.JPG)
Click on Import to create the table
![importconfirm](https://user-images.githubusercontent.com/18219467/233757743-acd85bae-9fd9-449b-bbc8-856a5feaad90.jpg)
![importDone](https://user-images.githubusercontent.com/18219467/233757755-e976c16d-164c-42bd-a0d6-fabe322153cf.jpg)
Click on SQL Query tools to verify that tables are created
![checkTblCreated](https://user-images.githubusercontent.com/18219467/233757934-a99b77ba-562b-4796-83c3-73f718e45d37.JPG)

#### Import data files
Click on Import files, then click on CSV data radio button, then click next button
![csv1](https://user-images.githubusercontent.com/18219467/233757953-b322654d-c6b9-4fc7-96d8-02f5f41edfde.JPG)
Select USA_Housing_train.csv file and click next button
![csv2](https://user-images.githubusercontent.com/18219467/233757971-87734bf4-1d18-4a92-9491-5f491e51814c.JPG)
Select USA_Housing_train.csv file from dropdownlist, check import rows as header row and Field names in header row match column names in selected table and click import files
![csv3](https://user-images.githubusercontent.com/18219467/233758084-ac6fa086-40b4-4a09-98d1-73e9d93b5f74.jpg)
click on import in confirmation dialog
![csv4](https://user-images.githubusercontent.com/18219467/233758167-cc4af63f-71a6-436c-bb83-f2a10b88069e.jpg)
4000 rows should be copied 
![csv5](https://user-images.githubusercontent.com/18219467/233758188-15ecaf0f-bc32-4b25-8730-4f86645ada88.jpg)
Do the same steps to import USA_Housing_validate.csv file which contain 1500 records
![csv6](https://user-images.githubusercontent.com/18219467/233758219-d2f62c9f-01b9-48d3-a102-184b14ec46f0.jpg)

## Setp 2.3 : Create Model
Click on IntegratedM tools and select Create Panel.

Enter USAHousingPriceModel in Model Name field, Select usa_housing_train table and Price in field to predict dropdown. Click on create model button to create the model
![createModel](https://user-images.githubusercontent.com/18219467/233758287-111e2a8e-12a9-4bc3-af29-6a752f2a30ab.JPG)

## Setp 2.4 : Train Model
select Train Panel, Select USAHousingPriceModel from model to train dropdownlist and enter USAHousingPriceModel_t1 in train model name feild
![TRAIN1](https://user-images.githubusercontent.com/18219467/233758471-e8e1779f-0cee-4131-9306-568c13465088.jpg)
Model will be trained once Run Status completed
![TRAIN2](https://user-images.githubusercontent.com/18219467/233758563-629542da-01a0-4050-9a1f-79c947efba07.jpg)

## Setp 2.5 : Validate Model
Select Validatge Panel, Select USAHousingPriceModel_t1 from Trained model to validate dropdownlist, select usa_houseing_validate from Table to validate model from dropdownlist and click on validate model button
![image](https://user-images.githubusercontent.com/18219467/233758810-9891f2f1-0825-45f3-9e12-5ccae3000ec7.png)
Click on show validation metrics to view metrics
![showValidation](https://user-images.githubusercontent.com/18219467/233758865-c20a0275-70aa-4af5-ba0f-1d7c153589c4.JPG)
Click on chart icon to view Prediction VS Actual graph 
![validationChart](https://user-images.githubusercontent.com/18219467/233759007-49fd2bce-badc-4036-8c46-b72e4145b6d5.JPG)



## Step 3 : Activate python virtual environment 
Repository already contains python virtual environment folder (venv) along with all the required libraries.

All we need is to just activate the environment
On Unix or MacOS:
```
$ source venv/Scripts/activate
```
On Windows:
```
venv\scripts\activate
```
## Step 4 : Set InterSystems Cloud SQL connection parameters
Repo contains config.py file. Just open and set the parameters
![image](https://user-images.githubusercontent.com/18219467/232424168-3fd4ce14-2a78-44bc-a42b-c65909d9696a.png)

Put same values used in InterSystems Cloud SQL
![image](https://user-images.githubusercontent.com/18219467/232485432-4b100781-1127-45b0-b3d8-95570124d977.png)


## Step 5 : Run Web Application for prediction   
Run the below command in virtual environment to start our main application
```
python app.py
```
![image](https://user-images.githubusercontent.com/18219467/233229144-4ecac12f-15b4-4318-a6ea-0ad6790038ae.png)

Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to run the application

![image](https://user-images.githubusercontent.com/18219467/233230031-63c27a25-910c-4b16-9a5a-9466f2e57354.png)

Enter Age of house, No of rooms, No of bedroom and Area population to get the prediction 


## Step 6 : Explore the Explainer dashboard
Finaly, run the below command in virtual environment to start our main application
```
python expdash.py
```
![image](https://user-images.githubusercontent.com/18219467/232438579-26fc0a30-9f95-4df1-81ef-7f24270316c5.png)
![image](https://user-images.githubusercontent.com/18219467/232478449-557091da-3a7d-4534-bd0f-13c12e682e4c.png)
![image](https://user-images.githubusercontent.com/18219467/232478562-70200f16-4161-4738-bf13-fd043a21d194.png)

Navigate to [http://localhost:8050/](http://localhost:8050/) to run the application

![image](https://user-images.githubusercontent.com/18219467/233049477-3c62aa02-952e-4ea1-8334-699f8c8eb215.png)


Application will list all the trained models along with our USAHousingPriceModel. Navigate to "go to dashboard" hyperlink to view model explainer

Feature Importances. Which features had the biggest impact?
![image](https://user-images.githubusercontent.com/18219467/232486985-1719d884-295c-4521-a5cd-85ac034eded9.png)

Quantitative metrics for model performance, How close is the predicted value to the observed?
![image](https://user-images.githubusercontent.com/18219467/232487163-cbaceee4-54c7-4b7e-a3c7-c775cb873419.png)

Prediction and How has each feature contributed to the prediction?
![image](https://user-images.githubusercontent.com/18219467/232487390-81a06116-ac72-495c-9b1d-be117f69ff08.png)

Adjust the feature values to change the prediction
![image](https://user-images.githubusercontent.com/18219467/232487500-0c772ce6-b665-40ab-8316-ee5cdf43f3c7.png)

Shap Summary, Ordering features by shap value
![image](https://user-images.githubusercontent.com/18219467/232487656-d2a5bf90-c09b-45b0-b05c-0a1f6570d2cb.png)

Interactions Summary,Ordering features by shap interaction value
![image](https://user-images.githubusercontent.com/18219467/232487941-c9f4b9a3-d727-4895-887a-68b825a2bb6b.png)

Decision Trees, Displaying individual decision trees inside Random Forest
![image](https://user-images.githubusercontent.com/18219467/232488582-99b93bb2-5017-4670-a85b-27d19860cc92.png)




## Using Jupyter notebook to create,train,validate and predict ML model (OPTIONAL)
We can also use jupyter notebook to create,train,validate and predict ML model if not created by using Cloud SQL Service Portal

Repo also contains USAHousingModelNotebook.ipynb Jupyter notebook. In order to run it, just run runnotebook.bat under venv environment
```
runnotebook
```
![image](https://user-images.githubusercontent.com/18219467/232427181-21b2c7e3-3de8-40fb-8111-4b86a9042039.png)

Navigate to [http://localhost:8888/](http://localhost:8888/) to run the notebook
open USAHousingModelNotebook.ipynb notebook by clicking on it
![image](https://user-images.githubusercontent.com/18219467/232428806-89ba6cd3-8e49-4001-ae0d-f1f8e6873540.png)

It will open the notebook
![image](https://user-images.githubusercontent.com/18219467/233067990-cc24b4d2-3cce-4650-9f0e-d9e8f2418fee.png)

**NOTE : Make sure to select venv kernal by selecting main menu Kernal>Change kernal>venv**, so that notebook will use virtual environment libraries

![image](https://user-images.githubusercontent.com/18219467/232429659-cb4366e9-c14d-41fd-8408-e8447cea4710.png)

NOTE : Run the cells in sequence by just clicking the small arrow
![image](https://user-images.githubusercontent.com/18219467/232431439-8aaa7eac-900b-4cc8-9cca-ec6a44bb7920.png)



## About Dataset
[USA Housing dataset](https://www.kaggle.com/datasets/vedavyasv/usa-housing) is taken from [Kaggle](https://www.kaggle.com/)<br> [LICENCE:Public Domain](https://docs.data.world/en/59261-59714-2--Common-license-types-for-datasets.html)

USA_Housing dataset contains the following columns:

- 'Avg. Area Income': Avg. The income of residents of the city house is located in.
- 'Avg. Area House Age': Avg Age of Houses in the same city
- 'Avg. Area Number of Rooms': Avg Number of Rooms for Houses in the same city
- 'Avg. Area Number of Bedrooms': Avg Number of Bedrooms for Houses in the same city
- 'Area Population': The population of city house is located in
- 'Price': Price that the house sold at
NOTE: Column Name are modified and Id column is added in the dataset


## Credits
This application is derived from the [isc-cloud-sql-python-demo](https://openexchange.intersystems.com/package/isc-cloud-sql-python-demo) template by @Evgeny Shvarov

Thanks
