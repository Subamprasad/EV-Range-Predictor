import pandas as pd
try:
    df = pd.read_csv('electric-vehicle-range-prediction/data/ev_population.csv')
    print("SUCCESS: Data loaded. Shape:", df.shape)
    print("Columns:", df.columns.tolist())
except Exception as e:
    print("FAILURE:", e)
