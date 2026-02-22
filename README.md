# Predictive Maintenance for Industrial Vehicles

## Project Overview
Simulates industrial vehicle telematics and predicts when maintenance is required based on operational behavior (speed, RPM, idle time, load, acceleration, temperature).

## Dataset
- Synthetic telematics + maintenance data
- 1500 rows, 8 features + target `maintenance_required`
- Patterns injected to reflect real-world maintenance triggers

## Methodology
1. Data generation & preprocessing
2. Feature scaling (StandardScaler)
3. Random Forest Classifier for maintenance prediction
4. Visualization with Matplotlib

## Results
- Scatter plots show maintenance risk:
  - Hours since last maintenance vs Engine Temperature
  - Fuel Rate vs Idle Time
- Summary:
  - Total points: 1500
  - Maintenance required: ~5-10% (depending on patterns)

## Technologies Used
- Python, Pandas, NumPy, Scikit-learn, Matplotlib, Jupyter Notebook

## Future Improvements
- Use real telematics & maintenance logs
- Experiment with XGBoost / LightGBM
- Interactive dashboard for maintenance alerts
