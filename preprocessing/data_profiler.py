import pandas as pd
from pathlib import Path


class DataProfiler:

    def __init__(self):
        self.data_path = Path("data/raw/global_supply_chain_risk_2026.csv")
        self.report_path = Path("docs/data_quality_report.md")

    def profile(self):

        df = pd.read_csv(self.data_path)

        report = []

        report.append("# Enterprise Data Quality Report\n")
        report.append("## Dataset Overview\n")
        report.append(f"- Rows: {df.shape[0]}\n")
        report.append(f"- Columns: {df.shape[1]}\n\n")

        report.append("## Column Names\n")

        for col in df.columns:
            report.append(f"- {col}\n")

        report.append("\n## Missing Values\n")

        for col in df.columns:
            report.append(f"- {col}: {df[col].isnull().sum()}\n")

        report.append("\n## Duplicate Rows\n")
        report.append(f"{df.duplicated().sum()}\n")

        report.append("\n## Data Types\n")

        for col, dtype in df.dtypes.items():
            report.append(f"- {col}: {dtype}\n")

        with open(self.report_path, "w") as f:
            f.writelines(report)

        print("=" * 60)
        print("Enterprise Data Quality Report Generated")
        print("=" * 60)
        print(f"\nSaved to: {self.report_path}")


if __name__ == "__main__":
    profiler = DataProfiler()
    profiler.profile()