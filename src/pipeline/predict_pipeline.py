import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifacts/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds 
        except Exception as e:
            raise CustomException(e,sys)
# mapping html to backend 
class CustomData:
    def __init__(self, 
        Age: int, Salary:int, 
        Quantity:int, UnitPrice: int,
        Country:str, CustomerType: str):
        self.Age = Age
        self.Salary=Salary
        self.Quantity=Quantity
        self.UnitPrice=UnitPrice
        self.Country=Country
        self.CustomerType=CustomerType

    def get_data_as_data_frame(self):
        try:
            custom_data_imput_dict = {
                "Age": [self.Age],
                "Salary": [self.Salary],
                "Quantity":[self.Quantity],
                "UnitPrice":[self.UnitPrice],
                "Country":[self.Country],
                "CustomerType":[self.CustomerType]
            }
            return pd.DataFrame(custom_data_imput_dict)
        
        except Exception as e:
            raise CustomException(e, sys) 