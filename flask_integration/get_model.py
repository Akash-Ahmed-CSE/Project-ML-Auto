import pickle
import pandas as pd
import csv
#from app import predictedClassName

class LoadModel:
    def __init__(self, MODEL_PATH, predictedClassName):
        self.loaded_model = pickle.load(open(MODEL_PATH, 'rb'))
        self.headers = self.get_headers(predictedClassName)

    def get_headers(self, predictedClassName):
        with open('../data/uploaded_file.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            headers = next(csv_reader)
            if predictedClassName in headers:
                headers.remove(predictedClassName)
            return headers

    def predict_class(self, *variable_values):
        data = [list(variable_values)]
        df = pd.DataFrame(data, columns=self.headers)
        new_pred = self.loaded_model.predict(df)
        return new_pred
#
#48,50,1.02,4,0,1,1,0,0,121,18,1.2,137.53,4.63,11.3,44,6000,4.71,1,1,0,1,0,0 -> for 1 (positive)
#82,60,1.025,0,0,1,1,0,0,137,17,0.4,147,4.7,14.3,34,6700,5.9,0,1,0,1,0,0 -> for 0 (Negative)

#Test LoadModel
if __name__ == '__main__':
    MODEL_PATH = "../models/logistic_reg.sav"
<<<<<<< Updated upstream
    model = LoadModel(MODEL_PATH)
    predicted_class = model.predict_class(48,50,1.02,4,0,1,1,0,0,121,18,1.2,137.53,4.63,11.3,44,6000,4.71,1,1,0,1,0,0)
    print(predicted_class)
=======
    # model = LoadModel(MODEL_PATH)
    # predicted_class = model.predict_class(48,50,1.02,4,0,1,1,0,0,121,18,1.2,137.53,4.63,11.3,44,6000,4.71,1,1,0,1,0,0)
    # print(predicted_class)
>>>>>>> Stashed changes


