from flask import Flask, request, url_for, redirect, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("CSVfiles/TestTemplate.csv")

#MyArray = df.values
Kampala = df[df.Name == 'KAMPALA']
Kampala = Kampala[['Year','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']]

X = Kampala[['Year']].values
Y = Kampala[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']].values

mlp = MLPRegressor()
mlp.fit(X, Y)