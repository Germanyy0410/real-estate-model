from flask import Flask, request, jsonify # type: ignore
import joblib # type: ignore

app = Flask(__name__)

@app.route('/estate/estimate-price', methods=['POST'])
def predict():
    model = joblib.load('sample.pkl')
    data = request.json['inputData']

    result = model.predict(data)
    return jsonify({'output': result.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
