from explainerdashboard.datasets import titanic_survive, titanic_fare
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from explainerdashboard import ClassifierExplainer, ExplainerDashboard, ExplainerHub, RegressionExplainer
import dash_bootstrap_components as dbc
from sklearn.preprocessing import OrdinalEncoder
import utility

#Establish connection with InterSystems IRIS Cloud
connection = utility.get_db_connection()
#Create cursor 
cur = connection.cursor()
#Execute the cursor to retrieve all the models
cur.execute('SELECT MODEL_NAME,DESCRIPTION,DEFAULT_TRAINING_QUERY,PREDICTING_COLUMN_NAME FROM INFORMATION_SCHEMA.ML_MODELS')
#Fetch all the records in data
data = cur.fetchall()
dblst=[]
#Iterate all the records and check if model is trained
for i in range(len(data)):
    #check if model is trained
    cur.execute("select lower(max(model_type)) from information_schema.ML_TRAINED_MODELS where model_name = '"+data[i][0]+"'")
    data2 = cur.fetchall()
    #if Model type is regression
    if data2[0][0] == 'regression':
        #explainer = RegressionExplainer(RandomForestClassifier().fit(X_train, y_train), X_test, y_test)
        #X_train, y_train, X_test, y_test = utility.get_model_train_test(data[i][2],data[i][3])
        #X_train, y_train, X_test, y_test = utility.get_model_train_test("SELECT top 100 * FROM  SQLUser . yellow_tripdata_train",data[i][3])
        #X_train = X_train.drop(columns=['store_and_fwd_flag'])
        #X_test = X_test.drop(columns=['store_and_fwd_flag'])   
        #X_train = X_train.drop(columns=['tpep_pickup_datetime'])
        #X_test = X_test.drop(columns=['tpep_pickup_datetime'])   
        #X_train = X_train.drop(columns=['tpep_dropoff_datetime'])
        #X_test = X_test.drop(columns=['tpep_dropoff_datetime'])   
           
        #X_train.to_csv("x_train.csv")
        #y_train.to_csv("y_train.csv")
        #X_test.to_csv("x_test.csv")
        #y_test.to_csv("y_test.csv")
        
        #Get train and test data
        X_train, y_train, X_test, y_test = titanic_fare()
        #X_train._convert(convert_numeric=True).dropna()
        #X_train2 = X_train.drop(columns=['store_and_fwd_flag'])
        #encoder = OrdinalEncoder()
        #X_train = encoder.fit_transform(X_train)
        #X_test = encoder.fit_transform(X_test)
        #Generate model
        model = RandomForestRegressor(n_estimators=50, max_depth=10).fit(X_train, y_train)
        #Initiate explainer 
        explainer = RegressionExplainer(model, X_test, y_test)
        #Append exlpaner to the list, so can be added to ExplainerHub
        dblst.append(ExplainerDashboard(explainer,title="Model : "+data[i][0], name="db"+ str(i+1),description=data[i][1]+", Training Query : "+data[i][2]))
    #If Model type is classification
    elif data2[0][0] == 'classification':
        #X_train, y_train, X_test, y_test = utility.get_model_train_test(data[i][2],data[i][3])
        #Get train and test data
        X_train, y_train, X_test, y_test = titanic_survive()
        encoder = OrdinalEncoder()
        X_train = encoder.fit_transform(X_train)
        #Initiate explainer 
        explainer = ClassifierExplainer(RandomForestClassifier().fit(X_train, y_train), X_test, y_test)
        #Append exlpaner to the list, so can be added to ExplainerHub
        dblst.append(ExplainerDashboard(explainer,title="Model : "+data[i][0], name="db"+ str(i+1),description=data[i][1]+", Training Query : "+data[i][2],bootstrap=dbc.themes.SLATE))
    else:
        pass
    
#close connection
cur.close() 
connection.close()
#initate ExplanerHub by passing all the explaners
hub = ExplainerHub(dblst, bootstrap=dbc.themes.MORPH, title="InterSystems IRIS Cloud Integrated ML explorer",description="Give your applications direct access to the advanced relational database capabilities of InterSystems IRIS® Data Platform without the burden of provisioning, configuring, and maintaining cloud infrastructure. The IRIS Cloud IntegratedML option lets you define and execute predictive models by applying automated functions directly from SQL, without requiring extensive machine learning expertise.")
#Run application
hub.run()
