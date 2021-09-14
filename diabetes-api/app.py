#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global variables
loadedModel = pickle.load(open('Diabetes Model.pkl', 'rb'))
app = Flask(__name__)

#Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    glucose = request.form['glucose']
    age = request.form['age']
    bmi = request.form['bmi']

    prediction = loadedModel.predict([[glucose, bmi, age]])

    if prediction[0] == 0:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"

    return render_template('index.html', api_output=prediction)    

#Main function
app.run(debug=True)