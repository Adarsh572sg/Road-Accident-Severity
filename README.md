# Road Accident Severity Prediction

This repository provides a machine learning-based web application for predicting the severity of road accidents. Using input features like road type, weather conditions, lighting, area type, junction detail, and speed limit, the model predicts whether an accident's severity is likely to be Slight, Serious, or Fatal.

## Problem Statement

Road accidents are a significant public safety concern, often resulting in injuries, fatalities, and economic losses. Predicting the severity of road accidents can help authorities to take preventive measures and allocate resources effectively.

## Features

- **Web App**: Built with Flask, allowing users to input accident conditions and receive a prediction.
- **Machine Learning Model**: Trained to classify accident severity based on key features.
- **Interactive Form**: Users can select details such as road type, weather, light conditions, urban/rural area, junction detail, and speed limit.

## Project Structure

- `app.py`: Flask application backend, loads the trained model and handles prediction requests.
- `index.html`: Web form for user input and displaying predictions.
- `Road_Accident_Severity (5).ipynb`: Jupyter Notebook containing data analysis, model building, and training steps.
- `PPT-Predicting-Road-Accident-Severity.pdf`: Project presentation.
- Screenshots: Example outputs from the application.

## Usage

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Adarsh572sg/Road-Accident-Severity.git
   cd Road-Accident-Severity
   ```

2. **Install Dependencies**
   - Python 3.x
   - Flask
   - numpy
   - pickle (standard library)
   - Other dependencies as per Jupyter Notebook (see notebook for details).

   You can use pip to install Flask and numpy:
   ```sh
   pip install flask numpy
   ```

3. **Run the Application**
   Ensure `accident_severity_model.pkl` is present in the root directory (generated from the notebook).

   ```sh
   python app.py
   ```

4. **Open in Browser**
   Visit `http://127.0.0.1:5000` and fill in the form to get accident severity predictions.

## Model Input Features

- **Road Type:** Single Carriageway, Dual Carriageway, Roundabout, etc.
- **Weather Conditions:** Fine, Raining + high winds, Snowing, Unknown.
- **Light Conditions:** Daylight, Darkness - lights lit, Unknown.
- **Urban or Rural Area:** Urban, Rural, Unknown.
- **Junction Detail:** T or staggered junction, Crossroads, Roundabout, No junction, Other junction, Unknown.
- **Speed Limit:** Numeric value in km/h.

## Example

![Screenshot](Screenshot%202025-05-23%20095628.png)

## Project Presentation
For a detailed overview of the methodology and results, see: [Road_Accident_Severity (5).ipynb](Road_Accident_Severity (5).ipynb)
**Author**: [Adarsh572sg](https://github.com/Adarsh572sg)
