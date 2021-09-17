#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('KNN Model.pkl', 'rb'))

#Routes
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    glucose = request.form['glucose']
    bmi = request.form['bmi']
    age = request.form['age']

    prediction = loadedModel.predict([[glucose, bmi, age]])

    if prediction[0] == 0:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"

    return render_template('form.html', api_output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)
