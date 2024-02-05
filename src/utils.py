import os 
import sys

import numpy as np
import pandas as pd
import dill 

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True) #exist_ok=True means if it exists, leaves directory unaltered & no error raised for existing path

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
        
    except Exception as e:
        raise CustomException(e, sys)