import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


def log_reg(input_Age, input_Polyuria, input_polydipsia, input_weight_loss, 
input_weakness, input_Polyphagia, input_genital_thrush, input_visual_blur, 
input_itching, input_irritability, input_healing, input_paresis, 
input_muscle_stiff, input_alopecia, input_obesity, input_gender):
    df = pd.read_csv('diabetes_data_upload.csv')

    dummy = pd.get_dummies(df['Gender'], drop_first = True)
    dummy.head()

    df2 = pd.concat((df, dummy), axis = 1)
    df2 = df2.drop(['Gender'], axis = 1)
    df3 = df2.rename(columns = {'Male': 'Gender'})
    df3.head()

    lb = LabelEncoder()
    df3['Polyuria'] = lb.fit_transform(df3['Polyuria'])
    df3['Polydipsia'] = lb.fit_transform(df3['Polydipsia'])
    df3['sudden weight loss'] = lb.fit_transform(df3['sudden weight loss'])
    df3['weakness'] = lb.fit_transform(df3['weakness'])
    df3['Polyphagia'] = lb.fit_transform(df3['Polyphagia'])
    df3['Genital thrush'] = lb.fit_transform(df3['Genital thrush'])
    df3['visual blurring'] = lb.fit_transform(df3['visual blurring'])
    df3['Itching'] = lb.fit_transform(df3['Itching'])
    df3['Irritability'] = lb.fit_transform(df3['Irritability'])
    df3['delayed healing'] = lb.fit_transform(df3['delayed healing'])
    df3['partial paresis'] = lb.fit_transform(df3['partial paresis'])
    df3['muscle stiffness'] = lb.fit_transform(df3['muscle stiffness'])
    df3['Alopecia'] = lb.fit_transform(df3['Alopecia'])
    df3['Obesity'] = lb.fit_transform(df3['Obesity'])
    df3['class'] = lb.fit_transform(df3['class'])

    X = df3.drop(columns = 'class', axis = 1)  # Our features
    y = df3['class']  # Our target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 2)

    model = LogisticRegression()
    model.fit(X_train, y_train)  # Find the relationship between features and target

    features_input = (input_Age, input_Polyuria, input_polydipsia, input_weight_loss, 
    input_weakness, input_Polyphagia, input_genital_thrush, input_visual_blur, input_itching, 
    input_irritability, input_healing, input_paresis, input_muscle_stiff, input_alopecia, input_obesity, input_gender)

    data_to_numpy = np.asarray(features_input)
    data_reshape = data_to_numpy.reshape(1, -1)

    return model.predict(data_reshape)





