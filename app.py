from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('accident_severity_model.pkl', 'rb'))

# Example mappings
road_type_mapping = {
    'Single Carriageway': 1,
    'Dual Carriageway': 2,
    'Roundabout': 3,
    'One way street': 4,
    'Slip road': 5,
    'Unknown': 6
}

weather_mapping = {
    'Fine no high winds': 1,
    'Raining + high winds': 2,
    'Snowing no high winds': 3,
    'Unknown': 0
}

light_mapping = {
    'Daylight': 1,
    'Darkness - lights lit': 2,
    'Unknown': 0
}

urban_mapping = {
    'Urban': 1,
    'Rural': 2,
    'Unknown': 0
}

junction_mapping = {
    'T or staggered junction': 1,
    'Crossroads': 2,
    'Roundabout': 3,
    'No junction': 4,
    'Other junction': 5,
    'Unknown': 0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get all form values
    road_type = request.form['Road_Type']
    weather = request.form['Weather_Conditions']
    light = request.form['Light_Conditions']
    urban = request.form['Urban_or_Rural_Area']
    junction = request.form['Junction_Detail']
    speed_limit = request.form['Speed_limit']

    # Map categorical features
    mapped_road_type = road_type_mapping.get(road_type, 0)
    mapped_weather = weather_mapping.get(weather, 0)
    mapped_light = light_mapping.get(light, 0)
    mapped_urban = urban_mapping.get(urban, 0)
    mapped_junction = junction_mapping.get(junction, 0)
    speed_limit = float(speed_limit)  # speed_limit should be numeric

    # Create final feature array
    final_features = np.array([mapped_road_type, mapped_weather, mapped_light, mapped_urban, mapped_junction, speed_limit]).reshape(1, -1)

    # Predict
    prediction = model.predict(final_features)

    # Interpret prediction
    if prediction[0] == 0:
        severity = "Slight Severity"
    elif prediction[0] == 1:
        severity = "Serious Severity"
    else:
        severity = "Fatal Severity"

    # Return result
    return render_template('index.html', prediction_text=f'Accident Severity Prediction: {severity}')

if __name__ == "__main__":
    app.run(debug=True)
