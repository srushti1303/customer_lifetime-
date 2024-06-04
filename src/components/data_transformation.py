import sys
import os 
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object 


@dataclass
class DataTransformationConfig:    # input 
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
        def __init__(self):
              self.data_transformation_config=DataTransformationConfig()
        '''Data Transformation'''
        def get_data_transformer_object(self):    #pickle files all tasks 
              try:
                    numerical_columns = ["Age", "Salary","Quantity","UnitPrice"]
                    categorical_columns = ["Country","CustomerType"]
                    # traing dataset 
                    num_pipeline =Pipeline(
                          steps=[
                                ("imputer",SimpleImputer(strategy="median")),
                                ("scaler",StandardScaler())
                          ]
                    )

                    cat_pipeline =Pipeline(
                          steps=[
                                ("imputer",SimpleImputer(strategy="most_frequent")),
                                ("one_hot_encoder",OneHotEncoder(handle_unknown="ignore")),
                                ("scaler",StandardScaler(with_mean=False))
                          ]
                    )

                    logging.info(f"Categorical colums: {categorical_columns}")
                    logging.info(f"Numerical colums: {numerical_columns}")
                    # combine numerical and categorical features above 
                    preprocessor=ColumnTransformer(
                          [
                                ("num_pipeline",num_pipeline,numerical_columns),
                                ("cat_pipeline",cat_pipeline,categorical_columns)
                          ]
                    )

                    return preprocessor
                
              except Exception as e:
                    raise CustomException(e,sys)
              
        def initiate_data_transformation(self,train_path,test_path):
              try:
                    train_df=pd.read_csv(train_path)
                    test_df=pd.read_csv(test_path)

                    logging.info("Read train and test data")
                    logging.info("Obtaining preprocessing object")
                    #model with all transformation
                    preprocessing_obj=self.get_data_transformer_object()
                    
                    target_column_name="TotalSpent"
                    numerical_columns =["Age", "Salary","Quantity","UnitPrice"]

                    # Separate features and target
                    input_feature_train_df = train_df.drop(columns=[target_column_name])
                    target_feature_train_df = train_df[target_column_name]
                    input_feature_test_df = test_df.drop(columns=[target_column_name])
                    target_feature_test_df = test_df[target_column_name]

                    logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

                    # Fit and transform the training data, transform the test data
                    input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
                    input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

                    # Combine transformed features with target
                    # Combine transformed features with target
                    # Combine transformed features with target
                    train_arr = np.hstack((input_feature_train_arr, np.expand_dims(np.array(target_feature_train_df), axis=1)))


                    test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

                    logging.info("Saved preprocessing object.")
                    #saving pickle file in hard dsik 
                    save_object(

                    file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj=preprocessing_obj

                    )
                    return (
                    train_arr,
                    test_arr,
                    self.data_transformation_config.preprocessor_obj_file_path,
                    )

              except Exception as e:
                    raise CustomException(e,sys)
              
                    
