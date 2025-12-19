from flask import Flask, render_template, request
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline
import os
from src.logging import logger
import json

app = Flask(__name__)

# --- Global Data Loading ---
make_model_year_map = {}
unique_districts = []
unique_ev_types = []

def load_dropdown_data():
    global make_model_year_map, unique_districts, unique_ev_types
    try:
        data_path = 'artifacts/data_ingestion/data.csv'
        if not os.path.exists(data_path):
            data_path = 'data/ev_population.csv'
        
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
            
            # 1. Legislative Districts
            unique_districts = sorted([int(x) for x in df['Legislative District'].dropna().unique()])

            # 2. EV Types
            unique_ev_types = sorted(df['Electric Vehicle Type'].dropna().unique().tolist())

            # 3. Hierarchy: Make -> Model -> Years
            grouped = df.groupby(['Make', 'Model'])['Model Year'].unique().apply(lambda x: sorted([int(y) for y in x], reverse=True))
            
            make_model_year_map = {}
            for (make, model), years in grouped.items():
                if make not in make_model_year_map:
                    make_model_year_map[make] = {}
                make_model_year_map[make][model] = years
            
            logger.info("Dropdown data loaded successfully globally.")
        else:
            logger.warning("Data file not found. Dropdowns will be empty.")

    except Exception as e:
        logger.error(f"Error loading dropdown data: {e}")

# Load on startup
load_dropdown_data()

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html", data_map=make_model_year_map, districts=unique_districts, ev_types=unique_ev_types)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        make = request.form.get('Make')
        model = request.form.get('Model')
        # Handle potential connection reuse where fields might be empty if bad request
        model_year = int(request.form.get('Model Year')) if request.form.get('Model Year') else 0
        ev_type = request.form.get('Electric Vehicle Type')
        leg_district = float(request.form.get('Legislative District')) if request.form.get('Legislative District') else 0.0

        data = {
            'Make': [make],
            'Model': [model],
            'Model Year': [model_year],
            'Electric Vehicle Type': [ev_type],
            'Legislative District': [leg_district]
        }
        
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(data)
        
        return render_template("index.html", 
                               prediction_text=f"{round(prediction[0], 2)}",
                               data_map=make_model_year_map,
                               districts=unique_districts,
                               ev_types=unique_ev_types,
                               selected_make=make,
                               selected_model=model,
                               selected_year=model_year,
                               selected_district=int(leg_district) if leg_district else None,
                               selected_ev_type=ev_type)

    except Exception as e:
        # Render template with error but keep dropdowns populated
        return render_template("index.html", 
                               prediction_text=f"Error: {e}",
                               data_map=make_model_year_map,
                               districts=unique_districts,
                               ev_types=unique_ev_types)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
