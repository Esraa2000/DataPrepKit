import pandas as pd

def identify_missing_values(data):

  missing_rows = data.isnull().sum(axis=1)
  missing_cols = data.isnull().sum(axis=0)
  return missing_rows.to_frame("Missing Values"), missing_cols.to_frame("Missing Values")

def handle_missing_values(data, strategy='mean', threshold=0.5):

  if strategy == 'mean':
    data = data.fillna(data.mean())
  elif strategy == 'median':
    data = data.fillna(data.median())
  elif strategy == 'most_frequent':
    data = data.fillna(data.mode().iloc[0])
  elif callable(strategy):
    # Custom function provided for imputation
    data = data.apply(strategy, axis=0)
  else:
    raise ValueError(f"Unsupported strategy for handling missing values: {strategy}")

  # Consider data sparsity before removing rows/columns
  missing_cols = data.isnull().sum(axis=0)
  cols_to_remove = missing_cols[missing_cols / len(data) > threshold].index
  data.dropna(subset=cols_to_remove, inplace=True)

  missing_rows = data.isnull().sum(axis=1)
  rows_to_remove = missing_rows[missing_rows > threshold * len(data.columns)].index
  data.dropna(axis=0, inplace=True)

  return data