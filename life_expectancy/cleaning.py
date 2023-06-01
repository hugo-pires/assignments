"""Script for cleaning life expectancy data
"""

from pathlib import Path
import argparse
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

def clean_data(data: pd.DataFrame, region: str='PT') -> None:
    """Cleans the data and filter it according to region supplied

    Args:
        data (pd.DataFrame): _description_
        region (str, optional): _description_. Defaults to 'PT'.

    """

    cleaned_data = (
        data['unit,sex,age,geo\\time'].str.split(pat=',', expand=True)
        .join(data)
        .drop(columns='unit,sex,age,geo\\time')
        .rename(columns={0:'unit', 1:'sex', 2:'age', 3:'region'})
        .melt(id_vars=['unit','sex','age','region'], var_name="year", value_name="value")
        .loc[lambda x: x['region'] == region]
        .assign(value=lambda row: row.value.str.extract(r'(\d+.\d+)').astype('float'))
        .assign(year=lambda row: row.year.astype('int'))
        .dropna(subset=['value'])
        )
    return cleaned_data

def save_data(cleaned_data: pd.DataFrame) -> None:
    """Saves the cleaned data into a file

    Args:
        cleaned_data (pd.DataFrame): _description_
    """
    cleaned_file = data_path / 'pt_life_expectancy.csv'
    cleaned_data.to_csv(cleaned_file, index=False)

def main(region:str = 'PT') -> None:
    """Pipeline function
    """
    raw_data = load_data()
    cleaned_data = clean_data(raw_data, region)
    save_data(cleaned_data)


if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description='App to process life expectancy data')
    parser.add_argument('--region', type=str, help='Region to filter', default='PT')
    args = parser.parse_args()
    main(args.region)
