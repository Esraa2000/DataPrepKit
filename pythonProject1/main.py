import unittest
import pandas as pd
from data_io import read_csv



def read_data():
  filepath = input("Enter the data file path: ")
  print(filepath)
  extension = filepath.split(".")[-1].lower()
  if extension == "csv":
    return pd.read_csv(filepath)
  elif extension == "xlsx":
    return pd.read_excel(filepath)
  elif extension == "json":
    return pd.read_json(filepath)
  else:
    raise ValueError(f"Unsupported file format: {extension}")



class TestDataIO(unittest.TestCase):

  def test_read_csv_success(self):
    data = read_csv("path/to/valid.csv")
    self.assertIsInstance(data, pd.DataFrame)  # Check if returned data is a DataFrame

  def test_read_csv_file_not_found(self):
    with self.assertRaises(FileNotFoundError):
      read_csv("non-existent_file.csv")


