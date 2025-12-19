# Electric Vehicle Range Prediction 🚗⚡

## Limitless Range, Intelligent Prediction

Welcome to the **Electric Vehicle Range Prediction** project! This application is designed to help EV owners and enthusiasts accurately estimate the driving range of various electric vehicles based on real-world data.

**Data Source**: This project harnesses the comprehensive [Washington State EV Population Data](https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD) to drive its predictions.

Built with a focus on precision and user experience, this tool leverages Machine Learning to analyze key vehicle characteristics—like Make, Model, Year, and EV Type—to predict how far you can go on a single charge.

---

## 🌟 Project Overview

As the world shifts towards sustainable transportation, "Range Anxiety" remains a concern for many. This project aims to bridge that information gap. By building a robust pipeline that learns from thousands of vehicle records, I created a system that provides accurate and instant range estimates.

**Key Goals of this Project:**
*   **Predictive Accuracy:** Using regression analysis to model the relationship between vehicle specs and range.
*   **User-Centric Design:** A clean, modern Web Interface using **Glassmorphism** styling.
*   **MLOps Best Practices:** Implementing a modular pipeline for reproducibility and scalability.

---

## � Architecture

This project follows a modular **Component-Based Architecture**:

```
├── .github/workflows   # Github Actions for CI/CD
├── artifacts/          # Generated models and processed data
├── config/             # YAML configurations
├── src/                # Core logic
│   ├── components/     # DataIngestion, Transformation, Trainer
│   ├── pipeline/       # Orchestration logic
│   └── utils/          # Helper functions
├── static/             # Assets (CSS/JS)
├── templates/          # Jinja2 HTML Templates
├── app.py              # Application Entry Point
└── main.py             # Pipeline Entry Point
```

---

## �🚀 Key Features

*   **Dynamic UI**: 
    *   **Cascading Dropdowns**: Filters intelligently! Selecting 'Tesla' shows only Tesla models; selecting 'Model 3' shows only relevant years.
    *   **Searchable Inputs**: Type to find your specific model instantly.
    *   **Modern Aesthetics**: Built with **Tailwind CSS** for a responsive, premium blue-themed design.
    
*   **Intelligent Backend**:
    *   **Flask Web Server**: A lightweight, fast Python backend serving the model.
    *   **Machine Learning Pipeline**: 
        1.  **Ingestion**: Automates data downloading and validation.
        2.  **Transformation**: Handles categorical encoding (OneHot) and scaling.
        3.  **Training**: Optimizes a Regression model for best performance.
    *   **Robust Error Handling**: Gracefully handles missing data or invalid inputs with default fallbacks.

*   **Automation**:
    *   **CI/CD Integration**: Includes GitHub Actions workflows for automated testing and validation.

---

## 🛠️ Tech Stack

*   **Language**: Python 3.10+
*   **Web Framework**: Flask
*   **Data Manipulation**: Pandas, NumPy
*   **Machine Learning**: Scikit-Learn (Dill/Pickle for serialization)
*   **Frontend**: HTML5, JavaScript (ES6+), Tailwind CSS
*   **Version Control**: Git & GitHub

---

## 🏃‍♂️ How to Run

### 1. Installation
Clone the repository and install the required dependencies.

```bash
git clone https://github.com/Subamprasad/EV-Range-Predictor.git
cd EV-Range-Predictor
pip install -r requirements.txt
```

### 2. Training the Model
If you want to retrain the model from scratch (ingest fresh data, transform, and train):

```bash
python main.py
```
*This will create the `artifacts/` folder with the trained model (`model.pkl`).*

### 3. Launching the App
To start the web interface:

```bash
python app.py
```
Open your web browser and go to: `http://localhost:5000`

---

## 👨‍💻 Author

**Subam Prasad**  
*ML Consultant & Developer*

I designed and developed this end-to-end MLOps solution to demonstrate the power of combining data science with intuitive software engineering. Feel free to explore, fork, and contribute!

