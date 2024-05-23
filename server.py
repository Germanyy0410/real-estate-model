from flask import Flask, request, jsonify # type: ignore
import joblib # type: ignore
import os
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://real-estate-frontend-ip46.vercel.app"])

@app.route('/api/estate/estimate-price', methods=['POST'])
def predict():
    try:
        model = joblib.load(os.path.join(os.getcwd(), 'model.pkl'))
        data = request.json['inputData']
        result = model.predict(data)
        return jsonify({'output': result.tolist()})
    except:
        return jsonify({'status': 'Error occured while loading model!'})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'Server is running'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
