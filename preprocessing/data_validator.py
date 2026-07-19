import pandas as pd
from pathlib import Path


class DataValidator:

    def __init__(self):
        self.input_path = Path("data/processed/clean_supply_chain.csv")

    def validate(self):

        df = pd.read_csv(self.input_path)

        print("=" * 60)
        print("NOVAVISION DATA VALIDATION")
        print("=" * 60)

        print("\nValidation Results")

        print("-"*40)

        # Null values
        total_nulls = df.isnull().sum().sum()
        print(f"Total Missing Values : {total_nulls}")

        # Duplicate Rows
        duplicates = df.duplicated().sum()
        print(f"Duplicate Rows : {duplicates}")

        # Empty Dataset
        print(f"Dataset Empty : {df.empty}")

        # Shape
        print(f"Rows : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("-"*40)

        if total_nulls == 0 and duplicates == 0:
            print("DATA VALIDATION PASSED")
        else:
            print("DATA VALIDATION FAILED")


if __name__ == "__main__":

    validator = DataValidator()
    validator.validate()