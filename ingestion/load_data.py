import pandas as pd
from pathlib import Path


class DataLoader:
    """
    Loads the raw supply chain dataset.
    """

    def __init__(self):
        self.data_path = Path("data/raw/global_supply_chain_risk_2026.csv")

    def load_dataset(self):
        try:
            df = pd.read_csv(self.data_path)

            print("=" * 60)
            print("Dataset Loaded Successfully")
            print("=" * 60)

            print(f"\nRows : {df.shape[0]}")
            print(f"Columns : {df.shape[1]}")

            return df

        except FileNotFoundError:
            print("Dataset not found!")
            return None


if __name__ == "__main__":
    loader = DataLoader()
    dataset = loader.load_dataset()