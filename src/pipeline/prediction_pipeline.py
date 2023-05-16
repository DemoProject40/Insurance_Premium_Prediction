import numpy as np 
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from src.utils import load_model

import sys
import os

class Predict_Pileline:   
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprecessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_model(preprecessor_path)
            model = load_model(model_path)
            logging.info('preprocesor',preprocessor)
            logging.info('preprocesor',model)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

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

    def get_data_as_dataframe(self):
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

            

