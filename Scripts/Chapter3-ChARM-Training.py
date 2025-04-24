#!/usr/bin/env python3

"""
Chapter3-ChARM-Training.py

This script performs preprocessing, trains a Random Forest classifier with hyperparameter tuning,
and evaluates performance on the given dataset.

Input:
- A tab-separated file with features and a 'status' column as labels

Output:
- Trained best model (.joblib)
- Performance summary printed to console

Author: Ruthwick | Thesis Scripts | IIT Gandhinagar

"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from joblib import dump

# --- Input filenames from user ---
data_file = "Training Data"
file_title = "Title for the result files"

# --- Load data ---
data = pd.read_csv(data_file, sep='\t', header=0)
print('\nData loaded successfully.')

# --- Drop rows with missing values ---
initial_row_count = data.shape[0]
data.dropna(inplace=True)
rows_dropped = initial_row_count - data.shape[0]
print(f"Dropped {rows_dropped} rows containing NaN values.")

# --- Change working directory to data file's location ---
directory = os.path.dirname(data_file)
os.chdir(directory)
print('Working directory changed to data file location.')

# --- Define feature matrix (X) and target vector (y) ---
X = data.drop(columns=['status'])
y = data['status']
print('Features and labels defined.')

# --- Split data into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)
print('Data split into training and testing sets.')

# --- Set up hyperparameter grid for Random Forest ---
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}
print('Parameter grid defined for GridSearchCV.')

# --- Initialize classifier ---
rf = RandomForestClassifier(random_state=42)
print('RandomForestClassifier initialized.')

# --- Perform grid search with cross-validation ---
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    n_jobs=-1,
    verbose=2,
    scoring='accuracy'
)
print('\n🔍 Starting Grid Search...')
grid_search.fit(X_train, y_train)

# --- Extract and save the best model ---
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_
model_file = file_title + '_best.joblib'
dump(best_model, model_file)
print(f'\nModel trained and saved: {model_file}')
print(f'Best parameters: {best_params}')

# --- Model performance on training data ---
print('\nTraining data performance:')
y_pred_train = best_model.predict(X_train)
print(classification_report(y_train, y_pred_train))

# --- Model performance on test data ---
print('\nTest data performance:')
y_pred_test = best_model.predict(X_test)
print(classification_report(y_test, y_pred_test))

# --- Confusion matrix (raw values) ---
print('\nConfusion Matrix (Test Data):')
print(confusion_matrix(y_test, y_pred_test))
