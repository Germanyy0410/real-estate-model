# Real Estate Price Estimation Server
This project is a Flask server for estimating real estate prices using a pre-trained machine learning model. It provides an API endpoint for receiving input data and returning price estimates based on the model predictions.

## Overview
The server is built using Flask, a lightweight WSGI web application framework, and it utilizes the joblib library to load the pre-trained machine learning model from a file named model.pkl. The API endpoint /api/estate/estimate-price accepts POST requests with input data and returns price estimates calculated by the model.

## Features
- Real Estate Price Estimation: Predicts real estate prices based on input features.

## Installation and Setup
1. Clone the repository:
```bash
git clone https://github.com/Germanyy0410/real-estate-model
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the server:
```bash
python server.py
```