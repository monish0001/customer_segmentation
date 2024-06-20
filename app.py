from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
import numpy as np
import joblib
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'monish'

# Load the saved KMeans model
saved_model_path = 'Kmeansmodel.joblib'
if not os.path.exists(saved_model_path):
    raise FileNotFoundError(f"Model file not found at path: {saved_model_path}")

saved_model = joblib.load(saved_model_path)

# Define the form class
class PredictionForm(FlaskForm):
    feature1 = FloatField('Annual Income (k$)', validators=[DataRequired()])
    feature2 = FloatField('Spending Score (1-100)', validators=[DataRequired()])
    submit = SubmitField('Predict')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PredictionForm()
    prediction = None
    if form.validate_on_submit():
        # Get the data from the form
        feature1 = form.feature1.data
        feature2 = form.feature2.data
        test_data = np.array([[feature1, feature2]])
        
        # Make predictions
        predictions = saved_model.predict(test_data)
        
        # Get the prediction
        prediction = int(predictions[0])
    
    return render_template('index.html', form=form, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
