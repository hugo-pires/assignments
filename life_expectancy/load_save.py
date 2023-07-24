"""Script for loading and saving life expectancy data
"""

from pathlib import Path
import pandas as pd

root_path = Path.cwd()
data_path = root_path / 'life_expectancy' / 'data'


def load_data() -> pd.DataFrame:
    """Loads raw data from file

    Returns:
        pd.DataFrame: Raw loaded from TSV file
    """
    raw_file = data_path / 'eu_life_expectancy_raw.tsv'

    return pd.read_csv(raw_file, sep='\t')


def save_data(cleaned_data: pd.DataFrame) -> None:
    """Saves the cleaned data into a file

    Args:
        cleaned_data (pd.DataFrame): _description_
    """
    cleaned_file = data_path / 'pt_life_expectancy.csv'
    cleaned_data.to_csv(cleaned_file, index=False)
