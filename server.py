from flask import Flask, request, jsonify # type: ignore
import joblib # type: ignore
import os

app = Flask(__name__)

@app.route('/api/estate/estimate-price', methods=['POST'])
def predict():
    model = joblib.load(str(os.getcwd()) + '/model.pkl')
    data = request.json['inputData']

    result = model.predict(data)
    return jsonify({'output': result.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
