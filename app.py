from flask import Flask, render_template, request, redirect
from flask_material import Material
import intersystems_iris.dbapi._DBAPI as iris

  
app = Flask(__name__)
Material(app)

app.config['iris_host'] = ""
app.config['iris_port'] = 1972
app.config['iris_namespace'] = "USER"
app.config['iris_username'] = "SQLAdmin"
app.config['iris_password'] = ""
app.config['connection'] = None

@app.route('/')
def index():
    return redirect('/config')

@app.route('/config', methods=['GET', 'POST'])
def config():

    data = {
        "hostname": app.config['iris_host'],
        "port": int(app.config['iris_port']),
        "user": app.config['iris_namespace'],
        "namespace": app.config['iris_username'],
        "password": app.config['iris_password']
    }

    if request.method == 'POST':
        app.config['iris_host'] = request.form['hostname']
        app.config['iris_port'] = request.form['port']
        app.config['iris_namespace'] = request.form['user']
        app.config['iris_username'] = request.form['namespace']
        app.config['iris_password'] = request.form['password']

        try:

            app.config['connection'] = conn = iris.connect(
                app.config['iris_host'],
                int(app.config['iris_port']),
                app.config['iris_namespace'],
                app.config['iris_username'],
                app.config['iris_password']
            )

   
            return redirect('/predict')
        except Exception as e:
            return str(e)

    return render_template('config.html', data=data)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        rm = request.form['rm']
        brm = request.form['brm']
        population = request.form['population']
        connection = app.config['connection']
        #open cursor
        try:
            cur = connection.cursor()
        except Exception as e:
            print(e)
        #execute the cursor
        stat = "SELECT TOP 1 PREDICT(USAHousingPriceModel USE USAHousingPriceModel_t1 WITH (,,"+str(age)+","+str(rm)+","+str(brm)+","+str(population)+")) FROM  SQLUser.usa_housing_train"   
        try:
            cur.execute(stat)
            pred = cur.fetchall()
            pred = pred[0][0]
            pred = "${:,.0f}".format(float(pred))
            return render_template('index.html', age=age,rm=rm,brm=brm,population=population,pred=pred)
        except Exception as e:
            print(e)          
              
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)