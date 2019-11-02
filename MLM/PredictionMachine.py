from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from DB.dbHandler import dbHandler as DB
import numpy as np


class PredictionMachine:
    menu = DB.get_menu()
    X = np.array([[dish.dish_type, dish.energy, dish.output] for dish in menu.values()])
    le = LabelEncoder()
    X[:, 0] = le.fit_transform(X[:, 0])
    mapping = dict(zip(le.classes_, range(len(le.classes_))))
    y = np.array([dish.price for dish in menu.values()])
    model = LinearRegression()
    model.fit(X, y)

    @staticmethod
    def predict(X):
        return round(PredictionMachine.model.predict(X)[0], 2)

    @staticmethod
    def get_code(dish_type):
        return PredictionMachine.mapping[dish_type]
