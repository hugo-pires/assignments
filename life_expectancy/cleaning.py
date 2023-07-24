"""Script for cleaning life expectancy data
"""

import pandas as pd

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
