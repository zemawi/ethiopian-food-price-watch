# Ethiopian Food Price Watch

A data science and forecasting project for monitoring food prices in Ethiopia, detecting unusual spikes, and visualizing the strongest market signals in a Streamlit dashboard.

## Project goals
- Track food-price movements across markets and commodities
- Analyze trends and seasonality over time
- Forecast representative price series
- Detect abnormal spike events using engineered features
- Present results in a clear dashboard and reproducible notebooks

## Repository structure
- `data/` — cleaned and engineered datasets
- `models/` — trained model artifacts and saved metrics
- `notebooks/` — analysis and modeling workflow
- `images/` — plots and figures
- `app.py` — Streamlit dashboard entry point
- `Dockerfile` — container configuration for deployment
- `requirements.txt` — Python dependencies

## Data sources
The project uses cleaned Ethiopian food-price data and engineered features such as:
- lags
- rolling averages and volatility
- percentage change
- relative price-to-mean ratios
- spike flags

## Local setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run app.py
   ```
4. Open the local Streamlit URL shown in the terminal.

## Dashboard
The dashboard provides:
- market and commodity filtering
- price trend plots
- model performance comparison
- spike detection summary
- forecast and alert signals

## Model summary
Key outputs are saved under the `models/` folder:
- `forecast_metrics.csv`
- `spike_metrics.csv`
- `maize_forecast_model.joblib`
- `spike_classifier_model.joblib`
- `spike_threshold.json`

## Testing
Run the smoke tests:
```bash
pytest -q
```

## Docker
Build the project container:
```bash
docker build -t ethiopian-food-price-watch .
```
Run it locally:
```bash
docker run -p 8501:8501 ethiopian-food-price-watch
```

## Deployment
This project is set up for a simple deployment flow:
1. containerize with Docker
2. deploy on a cloud host or container service
3. expose port 8501 for the dashboard
4. keep model artifacts under `models/`

## Documentation and next steps
- Keep the notebooks as the main reproducibility record
- Use the dashboard for stakeholder-facing exploration
- Keep model metrics updated when retraining occurs
- Extend the app with alerts, map views, or downloadable reports when needed

## Recommended workflow
1. Explore data in notebooks
2. Validate model performance
3. Run the dashboard locally or in Docker
4. Deploy the container
5. Share the dashboard and key metrics with stakeholders
