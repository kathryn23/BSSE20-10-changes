from app import app, db
from flask import render_template
import numpy as np
import pandas as pd
import datetime

class Expenses(db.Model):
    ExpenseID = db.Column(db.Integer, primary_key =True)
    ExpenseName = db.Column(db.String(40), unique=False)
    Quantity = db.Column(db.Integer)
    UnitCost = db.Column(db.Numeric)
    TotalCost = db.Column(db.Numeric)
    ExpenseGroup = db.Column(db.String(20), unique=False)
    Year = db.Column(db.Integer)
    RecordDateTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, ExpenseName, Quantity, UnitCost, TotalCost, ExpenseGroup, Year):
        self.ExpenseName = ExpenseName
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.TotalCost = TotalCost
        self.ExpenseGroup = ExpenseGroup
        self.Year = Year

    def __repr__(self):
        return '<Expense %r>' % self.ExpenseName

class Income(db.Model):
    IncomeID = db.Column(db.Integer, primary_key =True)
    Revenue = db.Column(db.Numeric)
    Year = db.Column(db.Integer) 
    ReceivedDate = db.Column(db.DateTime)
    RecordDateTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, Revenue, Year, ReceivedDate):
        self.Revenue = Revenue
        self.Year = Year
        self.UnitCost = UnitCost
        self.ReceivedDate = ReceivedDate

    def __repr__(self):
        return '<Year %r>' % self.Year