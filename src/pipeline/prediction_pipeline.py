import numpy as np 
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from src.utils import load_model

import sys
import os

class Predict_Pileline:
    def __init__():
        pass

    def predict(self,features):
        try:
            preprecessor_path = os.path.join('artifatcs','preprocessor.pkl')
            model_path = os.laod.join('artifacts','preprocessor.pkl')

            preprocessor = load_model(preprecessor_path)
            model = laod_model(model_path)
            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)
            
            return pred

        except Exception as e:
            logging.info('Exception ocur in predicted pipeline')
            raise CustomException(e,sys)

class Custom_Data:
    def __init__(self,
                age : int,
            	sex : float,
                bmi : float,
                children : int,
                smoker : float,
                region : float ):

                self.age = age,
                self.sex = sex,
                self.bmi = bmi,
                self.children = children,
                self.smoker = smoker,
                self.region = region

    def get_data_as_dataframe():
        try:
            custom_data_input_dict = {
                'age' : [self.age],
                'sex' : [self.sex],
                'bmi' : [self.bmi],
                'children' : [self.children],
                'smoker' : [self.smoker],
                'region' : [self.region]                   
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('data frame gathered')
            return df
        except Exception as e:
            logging.info('Exception Occur in prediction pipeline')
            raise CustomException(e,sys)

            

