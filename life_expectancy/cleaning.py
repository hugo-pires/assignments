"""_summary_
"""

from pathlib import Path
import argparse
import pandas as pd


def clean_data(region: str='PT') -> None:
    """_summary_
    """
    root_path = Path.cwd()
    data_path = root_path / 'life_expectancy' / 'data'
    raw_file = data_path / 'eu_life_expectancy_raw.tsv'
    cleaned_file = data_path / 'pt_life_expectancy.csv'

    data = pd.read_csv(raw_file, sep='\t')
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
    cleaned_data.to_csv(cleaned_file, index=False)


if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description='App to process life expectancy data')
    parser.add_argument('--region', type=str, help='Region to filter', default='PT')
    args = parser.parse_args()
    clean_data(args.region)
