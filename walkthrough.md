# Electric Vehicle Range Prediction Project Walkthrough

## Overview
We have created a project to predict the electric range of vehicles using the Washington State EV Population dataset.

## Project Structure
## Project Structure (MLOps)
- `config/`: Configuration files (`config.yaml`).
- `params.yaml`: Model hyperparameters.
- `src/`: Source code.
  - `components/`: Logic for Ingestion, Transformation, Training.
  - `pipeline/`: Orchestration scripts.
  - `entity/`: Data classes for config.
- `app.py`: Flask Web Application.
- `main.py`: Training pipeline entry point.
- `templates/`: HTML templates.

## How to Run

1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Train the Model**
    Run the full pipeline to ingest, process, and train:
    ```bash
    python main.py
    ```

3.  **Run Web App**
    Start the prediction interface:
    ```bash
    python app.py
    ```
    Open `http://localhost:5000` in your browser.

## Pipeline Details
-   **Stage 01: Data Ingestion**: Downloads data from WA.gov.
-   **Stage 02: Data Transformation**: Cleans data and encodes features.
-   **Stage 03: Model Training**: Trains Random Forest and saves model.


## Key Features
-   **dataset**: Real-world government data from Washington State.
-   **model**: Random Forest for robust prediction.
-   **visuals**: Custom plots for "Range vs Year" and "Top Makes".
