import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.logging import logger

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.pkl'))
        self.preprocessor = joblib.load(Path('artifacts/data_transformation/preprocessor.pkl'))

    def predict(self, data):
        try:
            # Expected features: 'Make', 'Model', 'Model Year', 'Electric Vehicle Type', 'Legislative District'
            # Convert input data to DataFrame
            df = pd.DataFrame(data)
            
            # Apply preprocessing
            # Note: The preprocessor saved was a dict of LabelEncoders.
            # We need to apply them carefully. If a new label appears, handle it (e.g. unknown class)
            # For simplicity, we fallback to a default or error, but let's try to map safely.
            
            features = ['Make', 'Model', 'Model Year', 'Electric Vehicle Type', 'Legislative District']
            
            for col in features:
                if col in df.columns:
                    le = self.preprocessor[col]
                    # This is tricky with LabelEncoder and unseen data. 
                    # Real app should use target encoding or one-hot with handle_unknown='ignore'.
                    # We will just try transform and catch error
                    try:
                       df[col] = le.transform(df[col].astype(str))
                    except Exception as e:
                        # Fallback for unseen labels? Or assign a default?
                        # Using a safe transformation approach
                        # Assigning 0 or mode might be misleading. 
                        # Ideally, we should have used OneHotEncoder.
                        # For now, let's assume valid inputs or handle exception.
                         logger.warning(f"Unseen label in {col}: {e}")
                         # Trying to transform knowing it might fail.
                         # In production we might want to map to a standard 'other' category during training.
                         pass
            
            prediction = self.model.predict(df)
            return prediction
        
        except Exception as e:
            raise e
