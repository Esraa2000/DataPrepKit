import pandas as pd
import logging

logger = logging.getLogger(__name__)  # Get logger for this module


def read_csv(filepath: str, **kwargs) -> pd.DataFrame:

  try:
    data = pd.read_csv(filepath, **kwargs)
    logger.info(f"Successfully read CSV file: {filepath}")
    return data
  except FileNotFoundError:
    logger.error(f"CSV file not found: {filepath}")
    raise
  except IOError as e:
    logger.error(f"Error reading CSV file: {filepath} - {e}")
    raise


def read_excel(filepath: str, sheet_name: str = None, **kwargs) -> pd.DataFrame:

  try:
    data = pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)
    logger.info(f"Successfully read Excel file: {filepath}")
    return data
  except FileNotFoundError:
    logger.error(f"Excel file not found: {filepath}")
    raise
  except IOError as e:
    logger.error(f"Error reading Excel file: {filepath} - {e}")
    raise


def read_json(filepath: str, **kwargs) -> pd.DataFrame:

  try:
    data = pd.read_json(filepath, **kwargs)
    logger.info(f"Successfully read JSON file: {filepath}")
    return data
  except FileNotFoundError:
    logger.error(f"JSON file not found: {filepath}")
    raise
  except IOError as e:
    logger.error(f"Error reading JSON file: {filepath} - {e}")
    raise
