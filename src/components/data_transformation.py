import os
from src.logging import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder # Added Standard Scaler and OneHotEncoder as potential needs
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd
from src.entity.config_entity import DataTransformationConfig
from src.utils.common import save_object
from pathlib import Path

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            # We will use LabelEncoder as in the notebook for simplicity as per user request
            # But normally OneHotEncoder is better for nominal categorical data. 
            # I will stick to LabelEncoder for now to match the notebook logic exactly as requested.
            pass 
        except Exception as e:
            raise e

    def initiate_data_transformation(self):
        try:
            data = pd.read_csv(self.config.data_path)
            logger.info("Read data completed")
            
            logger.info("Obtaining preprocessing object")

            # Dropping 0 range rows as per notebook
            df_clean = data[data['Electric Range'] > 0].copy()
            
            features_to_use = ['Make', 'Model', 'Model Year', 'Electric Vehicle Type', 'Legislative District']
            target = 'Electric Range'
            
            df_clean = df_clean.dropna(subset=features_to_use)
            
            # Label Encoding
            le_dict = {}
            for col in features_to_use:
                le = LabelEncoder()
                df_clean[col] = le.fit_transform(df_clean[col].astype(str))
                le_dict[col] = le
            
            # Save preprocessor (saving the dict of LEs)
            save_object(self.config.preprocessor_path, le_dict)
            logger.info(f"Saved preprocessing object.")

            X = df_clean[features_to_use]
            y = df_clean[target]

            logger.info("Splitting data into train and test sets")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            train_data = pd.concat([X_train, y_train], axis=1)
            test_data = pd.concat([X_test, y_test], axis=1)

            train_data.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Data transformation completed")
            logger.info(f"Train data shape: {train_data.shape}")
            logger.info(f"Test data shape: {test_data.shape}")

        except Exception as e:
            raise e
