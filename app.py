import pickle
from flask import Flask, request, jsonify, render_template
import json
import numpy as np

#load model
model = pickle.load(open('model.pkl', 'rb'))

#Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return "Testing"

@app.route('/predict', methods = ['POST'])
def predict():

    inputData = request.get_json(force = True)
    print(inputData)

    inputList = []
    resList = [] #need to serve data in 2d array for model to understand
    inputList.append(inputData['petrolTax'])
    inputList.append(inputData['averageIncome'])
    inputList.append(inputData['pavedHighway'])
    inputList.append(inputData['popDriverLicense'])
    resList.append(inputList)
    pred = str(model.predict(resList))
    return pred


