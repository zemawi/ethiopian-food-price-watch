from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def test_core_model_artifacts_exist():
    required_paths = [
        ROOT / 'models' / 'maize_forecast_model.joblib',
        ROOT / 'models' / 'spike_classifier_model.joblib',
        ROOT / 'models' / 'spike_threshold.json',
        ROOT / 'data' / 'eth_food_prices_clean.csv',
        ROOT / 'data' / 'eth_food_prices_features.csv',
    ]

    for path in required_paths:
        assert path.exists(), f'Missing required artifact: {path}'


def test_dashboard_module_loads_and_exposes_expected_api():
    app_path = ROOT / 'app.py'
    assert app_path.exists(), 'app.py should exist for the Streamlit dashboard'

    spec = importlib.util.spec_from_file_location('eth_food_watch_app', app_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert hasattr(module, 'load_forecast_data')
    assert hasattr(module, 'load_spike_data')
    assert hasattr(module, 'build_dashboard')
