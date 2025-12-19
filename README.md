# Electric Vehicle Range Prediction

A Machine Learning project to predict the electric range of BEV and PHEV vehicles using Washington State EV population data.

## 🚀 Features
- **Data Ingestion & Transformation**: Automated pipelines for processing raw data.
- **Model Training**: Regression model training with optimized hyperparameters.
- **Web Interface**: Interactive Flask application with cascading dropdowns for real-time predictions.
- **CI/CD**: GitHub Actions workflow included.

## 📂 Project Structure
```
├── .github/workflows   # CI/CD Configurations
├── config/             # Configuration files
├── src/                # Source code for pipelines and components
├── static/             # CSS and JS assets
├── templates/          # HTML templates
├── app.py              # Flask Web Application entry point
├── main.py             # Model Training entry point
└── requirements.txt    # Project dependencies
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Subamprasad/EV-Range-Predictor.git
   cd EV-Range-Predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Usage

### 1. Train the Model
To run the full data pipeline and train a new model:
```bash
python main.py
```
*This will generate artifacts in the `artifacts/` directory.*

### 2. Run the Web App
To start the prediction interface:
```bash
python app.py
```
Open your browser at `http://localhost:5000`.

## 📊 Dataset
Sourced from [Washington State Department of Licensing](https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD).
