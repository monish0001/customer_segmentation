# Customer Segmentation Prediction App

This is a Flask web application that predicts customer segments using a KMeans clustering model. Users can enter feature values to get predictions and view a customer segmentation plot.

## Live Demo

Check out the live app [here](https://customer-segmentation-rvbt.onrender.com).

## Features

- **User Input Form:** Enter features for prediction.
- **Prediction Display:** View the predicted customer segment.
- **Segmentation Plot:** Visual representation of customer segmentation.

## Technologies Used

- **Flask:** Web framework for building the application.
- **Flask-WTF:** Form handling with validation.
- **Matplotlib:** Plotting and visualization.
- **Joblib:** Model serialization and deserialization.
- **HTML/CSS:** Front-end structure and styling.

## Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/yourusername/customer-segmentation-app.git
    cd customer-segmentation-app
    ```

2. **Create and activate a virtual environment**:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Ensure you have the saved KMeans model file**:
    - Place the model file (`saved_model.pkl`) in the root directory of the project.

5. **Run the application**:
    ```
    python app.py
    ```

6. **Open your browser** and go to `http://127.0.0.1:5000/` to view the app.

## Project Structure

customer-segmentation-app/
├── app.py
├── templates/
│ └── index.html
├── static/
│ ├── customer_segmentation.png
│ └── style.css
├── saved_model.pkl
├── requirements.txt
└── README.md


## How It Works

1. **User Input**: Enter feature values (e.g., annual income and spending score) into the form.
2. **Model Prediction**: The app uses a pre-trained KMeans clustering model to predict the customer segment.
3. **Display Prediction**: The predicted customer segment is displayed on the same page.
4. **Show Plot**: A pre-generated plot of customer segmentation is shown below the prediction.


