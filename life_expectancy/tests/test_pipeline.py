"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.load_save import load_data, save_data
from life_expectancy.cleaning import clean_data
from life_expectancy.pipeline import pipeline

from . import OUTPUT_DIR, FIXTURES_DIR


def test_load_data(pt_life_expectancy_expected):
    """Run the `load_data` function and compare """
    pass

def test_save_data(pt_life_expectancy_expected):
    """Run the `save_data` function and compare """
    pass


def test_cleaning_data(pt_life_expectancy_expected, eu_life_expectancy_sample):
    """Run the `clean_data` function and compare the output to the expected output"""
    pd.testing.assert_frame_equal(pt_life_expectancy_expected, clean_data(eu_life_expectancy_sample).reset_index().drop(columns='index'))


def test_pipeline_data(pt_life_expectancy_expected, eu_life_expectancy_sample):
    """Run the `pipeline` function and compare the output to the expected output"""
    pass