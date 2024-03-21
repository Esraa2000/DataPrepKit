import unittest
from data_io import read_csv

class TestDataIO(unittest.TestCase):

  def test_read_csv_success(self):
    data = read_csv("path/to/valid.csv")
    self.assertIsInstance(data, pd.DataFrame)  # Check if returned data is a DataFrame

  def test_read_csv_file_not_found(self):
    with self.assertRaises(FileNotFoundError):
      read_csv("non-existent_file.csv")

if __name__ == "__main__":
  unittest.main()
