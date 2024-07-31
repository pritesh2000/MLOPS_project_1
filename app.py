from flask import render_template, Flask, request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)     #intializing a flask app

# Global flag to track if training has been done
training_done = False

def run_initial_training():
    global training_done
    os.system("python main.py")  # Run main.py once on startup
    training_done = True  # Set the flag to True after running

@app.route('/',methods = ['GET'])   # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])  # Route to train pipeline
def training():
    global training_done
    if not training_done:
        os.system("python main.py")
        training_done = True  # Set the flag to True after running
        return "Training Successful!"
    else:
        return "Training has already been executed."

@app.route('/predict', methods=['POST', 'GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1,11)
            
            # Example feature names (these should match the names used during model training)
            feature_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
            
            # Create a DataFrame with the same feature names
            frame = pd.DataFrame(data, 
                                columns=feature_names)

            obj = PredictionPipeline()
            predict = obj.predict(frame)

            return render_template('results.html', prediction = str(predict))
        
        except Exception as e:
            print("The Exception message is: ",e)
            return "Something is wrong"
        
    else:
        return render_template('index.html')

if __name__ == "__main__":
    run_initial_training() 
    app.run(host="0.0.0.0", port=8080, debug=False)