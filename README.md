# Tehran House Price Prediction

A Machine Learning project that predicts approximate house prices in different areas of Tehran using property features and location information.

## Overview

This project uses a dataset containing more than 4,000 housing records from different areas of Tehran to estimate house prices based on several property characteristics.

The model takes property information as input and predicts an estimated price based on patterns learned from the dataset.

## Features

- Predicts approximate house prices in Tehran.
- Uses a dataset containing 4,000+ housing records.
- Considers property area (square meters).
- Uses the number of bedrooms as a feature.
- Considers whether the property has a parking space.
- Considers whether the property has a storage room.
- Uses location information to account for price differences between areas.

## Input Features

| Feature | Description |
|---|---|
| Area | Property size in square meters |
| Bedrooms | Number of bedrooms |
| Parking | Whether parking is available |
| Storage | Whether a storage room is available |
| Location | Property location or district in Tehran |

## How It Works

1. Loads housing data from a CSV file.
2. Processes the property features and location information.
3. Trains a Machine Learning model on the available dataset.
4. Uses the trained model to predict the approximate price of a house based on user-provided information.

## Dataset

The dataset contains more than 4,000 housing records from different areas of Tehran.

The model's predictions depend on the quality, accuracy, and coverage of the available data.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn *(if used in the implementation)*
- CSV for data storage

## Limitations

- Predictions are estimates, not guaranteed market prices.
- Accuracy depends on the quality and representativeness of the dataset.
- Housing prices can change over time.
- The model may be less accurate for locations or property types that are poorly represented in the training data.

## Future Improvements

- Evaluate the model using appropriate regression metrics.
- Compare different Machine Learning algorithms.
- Improve location-based feature engineering.
- Add data visualization and exploratory data analysis.
- Develop a simple web interface for making predictions.
- Retrain the model with updated housing data.

## Purpose

This project was developed as a practical application of Machine Learning concepts, with a focus on regression and real-world housing price prediction.

---

**Note:** This project is intended for educational and experimental purposes and should not be used as the sole basis for real estate investment decisions.
