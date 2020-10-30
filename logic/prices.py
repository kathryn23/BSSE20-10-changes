from flask import Flask, request, url_for, redirect, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

df = pd.read_csv("CSVfiles/KampalaBeansAv.csv")

X = df[['Year','ItemName','District']].values
Y = df['AvPrice'].values

regressor = LinearRegression()
regressor.fit(X,Y)

@app.route('/')
def home():
    return render_template("prices.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final])
    prediction = regressor.predict(data_unseen)
    return render_template('prices.html', pred='Expected Market Price in UGX per Kg will be {}'.format(prediction))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port = 5000)
