import pandas as pd
import os
from src.logging import logger
from sklearn.ensemble import RandomForestRegressor
from src.entity.config_entity import ModelTrainerConfig
import joblib
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.iloc[:, :-1]
        train_y = train_data.iloc[:, -1]
        test_x = test_data.iloc[:, :-1]
        test_y = test_data.iloc[:, -1]

        logger.info("Training Model...")
        rf_model = RandomForestRegressor(
            n_estimators=self.config.n_estimators, 
            random_state=self.config.random_state,
            max_depth=self.config.max_depth
        )
        rf_model.fit(train_x, train_y)

        joblib.dump(rf_model, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model saved at {os.path.join(self.config.root_dir, self.config.model_name)}")

        # Evaluation
        y_pred = rf_model.predict(test_x)
        rmse = np.sqrt(mean_squared_error(test_y, y_pred))
        r2 = r2_score(test_y, y_pred)
        
        logger.info(f"Model Evaluation Metrics: RMSE={rmse}, R2={r2}")
        print(f"Model Evaluation Metrics: RMSE={rmse}, R2={r2}")
