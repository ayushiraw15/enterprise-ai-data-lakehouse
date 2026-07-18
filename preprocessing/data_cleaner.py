import pandas as pd
from pathlib import Path


class DataCleaner:

    def __init__(self):
        self.input_path = Path("data/raw/global_supply_chain_risk_2026.csv")
        self.output_path = Path("data/processed/clean_supply_chain.csv")

    def clean_data(self):

        print("=" * 60)
        print("NovaVision Data Cleaning Pipeline")
        print("=" * 60)

        # Load Dataset
        df = pd.read_csv(self.input_path)

        print(f"\nOriginal Shape : {df.shape}")

        # Remove Duplicate Rows
        duplicates = df.duplicated().sum()
        df = df.drop_duplicates()

        print(f"Duplicate Rows Removed : {duplicates}")

        # Fill Missing Values
        for column in df.columns:

            if df[column].dtype == "object":
                mode = df[column].mode()

                if not mode.empty:
                    df[column] = df[column].fillna(mode[0])

            else:
                df[column] = df[column].fillna(df[column].median())

        print("Missing Values Handled")

        # Save Processed Dataset
        df.to_csv(self.output_path, index=False)

        print(f"\nProcessed Dataset Saved To : {self.output_path}")

        print(f"Final Shape : {df.shape}")


if __name__ == "__main__":

    cleaner = DataCleaner()
    cleaner.clean_data()