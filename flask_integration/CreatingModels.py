def Create_Mode():
    # import required modules
    import pickle
    import os
    import pandas as pd
    import numpy as np
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    import csv
    # importing datasets
    df = pd.read_csv("../data/uploaded_file.csv", na_values="?")
    df.replace("?", np.NaN)


    # Replacing null value
    df.fillna(round(df.mean(), 2), inplace=True)

    #Only selecting a header except "Class"
    with open('../data/uploaded_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        headers.remove('Class')
        print(headers)



    # converting the target value to integer type
    df['Class'] = df['Class'].astype('int')


    # Define X and Y for Implement Models
    X = np.asarray(df[headers])
    X[0:5]
    y = np.asarray(df['Class'])
    y[0:5]

    # Normalize Dataset( We do not need this for this dataset)
    #X = preprocessing.StandardScaler().fit(X).transform(X)
    # print(X[0:5])

    # Spliting for Train & Test Dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
    # print ('Train set:', X_train.shape,  y_train.shape)
    # print ('Test set:', X_test.shape,  y_test.shape)

    # Logistic Regression
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)  # tranning the model with "loger" model
    Y_pred_lr = logreg.predict(X_test)

    # For result purpose
    acc_log = round(logreg.score(X_test, y_test) * 100, 2)
    print("Logistic Regression Accuracy: ", acc_log)

    #########################################
    # Creating a logistic_reg1.sav

    # Saving the model
    if not os.path.exists('../models'):
        os.makedirs('../models')

    MODEL_PATH = "../models/logistic_reg.sav"
    pickle.dump(logreg, open(MODEL_PATH, 'wb'))
    print("Your LogisticRegression model has been trained successfully !")
Create_Mode()