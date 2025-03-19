# Weather Prediction App

This is a Flask-based weather prediction app with a frontend built using HTML and CSS.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-prediction-app.git
   cd weather-prediction-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open in browser:  
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoint

- **POST /predict**  
  - Input: JSON with weather parameters  
  - Output: Predicted weather  

Example request:
```python
import requests
url = "http://127.0.0.1:5000/predict"
data = {"temperature": 30, "humidity": 70, "pressure": 1015}
response = requests.post(url, json=data)
print(response.json())
```

## Files
- `app.py` – Flask API
- `model.pkl` – Trained model
- `templates/` – HTML frontend
- `static/` – CSS files

