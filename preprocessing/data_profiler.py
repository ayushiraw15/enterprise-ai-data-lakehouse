import pandas as pd
from pathlib import Path


class DataProfiler:

    def __init__(self):
        self.data_path = Path("data/raw/global_supply_chain_risk_2026.csv")

    def profile(self):

        df = pd.read_csv(self.data_path)

        print("=" * 70)
        print("NOVAVISION DATA QUALITY REPORT")
        print("=" * 70)

        print("\nDataset Shape")
        print(df.shape)

        print("\nColumns")
        print(df.columns.tolist())

        print("\nData Types")
        print(df.dtypes)

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

        print("\nSummary Statistics")
        print(df.describe(include="all"))


if __name__ == "__main__":

    profiler = DataProfiler()
    profiler.profile()