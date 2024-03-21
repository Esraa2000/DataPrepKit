import pandas as pd
import numpy as np

def get_descriptive_stats(data, columns=None, data_type=None):

  if columns is None:
    if data_type is None:
      # Select all numerical columns
      columns = data.select_dtypes(include=[np.number])
    else:
      # Select columns of specific data type
      columns = data.select_dtypes(include=data_type)
  return columns.describe(percentiles=[0.25, 0.75])

def get_frequency_tables(data, columns=None):

  if columns is None:
    # Select all categorical columns (object or categorical dtype)
    columns = data.select_dtypes(include=[object])
  return data[columns].value_counts()
