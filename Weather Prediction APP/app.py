from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form  

        features = [
            float(data['date']),
            float(data['precipitation']),
            float(data['temp_max']),
            float(data['temp_min']),
            float(data['wind']),
            float(data['weather'])
        ]

        prediction = model.predict([features])[0]

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)