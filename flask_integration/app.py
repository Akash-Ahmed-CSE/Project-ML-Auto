import os
import time
from flask import Flask, render_template, flash, request, session
from werkzeug.utils import secure_filename
from get_model import *
import csv

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
predictedClassName = ""

#Define home route
#@app.route("/")

def index():
    return render_template("index.html")
#Define diagnosis route
@app.route("/diagnosis", methods=['POST'])
def diagnosis():
    with open('../data/uploaded_file.csv') as csv_file:
        # creating an object of csv reader
        # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        # initializing the model


        variable_values = []
        for var_name in headers:
            if var_name != predictedClassName:  # Exclude 'Class' variable from variable_values
                var_value = request.form.get(var_name)
                variable_values.append(var_value)

        MODEL_PATH = "../models/logistic_reg.sav"
        print(predictedClassName)
        model = LoadModel(MODEL_PATH, predictedClassName)
        print(model)
        #Predict on the given parameters
        prediction = model.predict_class(*variable_values)
        print(prediction)

        #Route for result
        if int(prediction[0]) == 1:
            return render_template("positive.html", result="true")
        elif int(prediction[0]) == 0:
            return render_template("negetive.html", result="true")

#upload file to a specific directory
UPLOAD_FOLDER = '../data/'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FILE_NAME'] = 'uploaded_file.csv'


@app.route('/', methods=['GET', 'POST'])

def upload():

    if request.method == 'POST':
        file = request.files['file']
        file.filename = 'uploaded_file.csv'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        flash('File uploaded successfully')
        print(file.filename)
        global predictedClassName
        predictedClassName = request.form.get('className')

        import CreatingModels
        CreatingModels.Create_Model(predictedClassName)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
