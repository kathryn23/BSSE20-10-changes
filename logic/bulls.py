from flask import Flask, request, url_for, redirect, render_template, jsonify
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect('DRIVER={SQL Server};'
     'SERVER=DESKTOP-TA8M6SG;'
     'DATABASE=FarmFARS;'
     'Trusted_Connection=yes;')

cursor = conn.cursor()
statement = ('SELECT * FROM SampleTable')

df = pd.read_sql_query(statement, conn)

X = df[['PurchasePrice', 'Quantity', 'Feed', 'Labour', 'Vaccination', 'Dewormers',
 'Acaricides', 'Buildings', 'Water', 'SalePrice', 'Income']].values

Y = df['Risk'].values

model = LogisticRegression()
model.fit(X,Y)

'''print(model.predict(X[:4]))
print(Y[:4])

y_pred = model.predict(X)
Y == y_pred
print((Y == y_pred).sum()/Y.shape[0])

print(model.score(X, Y))'''

@app.route('/')
def home():
    return render_template("model.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final])
    prediction = model.predict(data_unseen)
    return render_template('model.html', pred='Expected Risk will be {}'.format(prediction))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port = 5000)