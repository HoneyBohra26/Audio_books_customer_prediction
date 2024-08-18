from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pickle
import os

# Load scaler and model
scaler_deep_learning = pickle.load(open('scaler', 'rb'))
model = tf.keras.models.load_model('audioBooks_model.h5')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def data():
    prediction = []
    if 'data' not in request.files:
        return render_template("index.html", prediction=None)
    
    file = request.files['data']
    
    if file.filename == '':
        return render_template("index.html", prediction=None)
    
    if file and file.filename.endswith('.csv'):
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)
        raw_data = np.loadtxt(file_path, delimiter=',', skiprows=1)
        all_inputs = raw_data[:, 1:] 
        scaled_data = scaler_deep_learning.transform(all_inputs)
        predict_arr = np.argmax(model.predict(scaled_data), axis=1)
        prediction = predict_arr.tolist()

    return render_template("index.html", prediction=prediction, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)



