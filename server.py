from flask import Flask, request, jsonify # type: ignore
import joblib # type: ignore
import os
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['http://localhost:5173'])

@app.route('/api/estate/estimate-price', methods=['POST'])
def predict():
    model = joblib.load(str(os.getcwd()) + '/model.pkl')
    data = request.json['inputData']

    result = model.predict(data)
    return jsonify({'output': result.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
