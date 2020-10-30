from app import app, db
from app import models
from flask import render_template, request, url_for, redirect, jsonify
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd
import os
import csv

app.config["CSV_UPLOADS"] = "C:/Users/HP/Desktop/Project"
app.config["ALLOWED_CSV_EXTENSIONS"] = ["CSV"]
ValidColumns = ['Name', 'Quantity', 'Unit Cost', 'Total Cost', 'Expense group', 'Year']

def allowed_files(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_CSV_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather')
def weather():
    return render_template("weather.html")

@app.route('/prices')
def prices():
    return render_template("prices.html")

@app.route('/importExpense', methods=["GET", "POST"])
def importExpenseCSV():
    if request.method == "POST":
        if request.files:
            mycsv = request.files["fileToUpload"]
            try:
                if mycsv.filename == "":
                    raise Exception("No filename") 

                if allowed_files(mycsv.filename):
                    filename = secure_filename(mycsv.filename)

                    mycsv.save(os.path.join(app.config["CSV_UPLOADS"], filename))
                    url = app.config["CSV_UPLOADS"]+"/"+filename
                    df = pd.read_csv(url)
                    
                    index = 0
                    for col_name in df.columns:
                        
                        if col_name == ValidColumns[index]:
                            index = index + 1
                            continue
                        else:
                            raise Exception("Invalid Column Name "+col_name) 

                    #models.SaveExpense(df.values)
                    arr = df.values
                    for i in range(len(arr)) : 
                        expense = models.Expenses(
                        ExpenseName = arr[i,0],
                        Quantity = arr[i,1],
                        UnitCost = arr[i,2],
                        TotalCost = arr[i,3],
                        ExpenseGroup = arr[i,4],
                        Year = arr[i,5]
                        )    
                        db.session.add(expense)
                        db.session.commit()

                    return render_template('importExpense.html', error="Records successfully inserted")
                else:
                    raise Exception("That file extension is not allowed") 

            except Exception as e:
                msg = str(e)
                return render_template('importExpense.html', error=msg)

    return render_template("importExpense.html")


@app.route('/importIncome', methods=["GET", "POST"])
def importIncomeCSV():
    if request.method == "POST":
        if request.files:
            mycsv = request.files["fileToUpload"]
            if mycsv.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_files(mycsv.filename):
                filename = secure_filename(mycsv.filename)
                mycsv.save(os.path.join(app.config["CSV_UPLOADS"], filename))
                print("CSV saved")
                return redirect(request.url)
            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("importIncome.html")


@app.route('/predictPrice',methods=['POST'])
def predictPrice():
    df = pd.read_csv("app/CSVfiles/KampalaBeansAv.csv")

    X = df[['Year','ItemName','District']].values
    Y = df['AvPrice'].values

    regressor = LinearRegression()
    regressor.fit(X,Y)

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final])
    prediction = regressor.predict(data_unseen)
    return render_template('prices.html', pred='Expected Market Price in UGX per Kg will be {}'.format(prediction))

@app.route('/predictWeather',methods=['POST'])
def predict():
    df = pd.read_csv("app/CSVfiles/TestTemplate.csv")

    #MyArray = df.values
    Kampala = df[df.Name == 'KAMPALA']
    Kampala = Kampala[['Year','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']]

    X = Kampala[['Year']].values
    Y = Kampala[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']].values

    mlp = MLPRegressor()
    mlp.fit(X, Y)

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final])
    prediction = mlp.predict(data_unseen)
    return render_template('weather.html', pred='Expected Rainfall in mm will be {}'.format(prediction))