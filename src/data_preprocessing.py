"""
Data preprocessing module for Crime Prediction AI project.
"""

import pandas as pd

def load_and_clean_data(street_path, outcomes_path):
    street_df = pd.read_csv(street_path)
    outcomes_df = pd.read_csv(outcomes_path)

    # TODO: implement cleaning logic
    return street_df, outcomes_df
