import joblib


class Model:
    def __init__(self, humidity, pressure, temperature, wind_direction, wind_speed):
        self.h = humidity
        self.p = pressure
        self.t = temperature
        self.wd = wind_direction
        self.ws = wind_speed

    def svm_predict(self):
        obj = [self.h, self.p, self.t, self.wd, self.ws]
        model = joblib.load('svm.model')
        result = model.predict_proba([obj])
        return result

    def lr_predict(self):
        obj = [self.h, self.p, self.t, self.wd, self.ws]
        model = joblib.load('LR.model')
        result = model.predict([obj])
        return result

