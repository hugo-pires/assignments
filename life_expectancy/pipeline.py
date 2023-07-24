"""Script for running a data pipeline
"""
import sys
sys.path.append("/home/hugo/Dev/assignments/")
import argparse

from life_expectancy.load_save import load_data, save_data
from life_expectancy.cleaning import clean_data


def pipeline(region:str = 'PT') -> None:
    """Pipeline function
    """
    raw_data = load_data()
    cleaned_data = clean_data(raw_data, region)
    save_data(cleaned_data)


if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description='App to process life expectancy data')
    parser.add_argument('--region', type=str, help='Region to filter', default='PT')
    args = parser.parse_args()
    pipeline(args.region)
