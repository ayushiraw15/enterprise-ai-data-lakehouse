from ingestion.load_data import DataLoader
from preprocessing.data_profiler import DataProfiler
from preprocessing.data_cleaner import DataCleaner
from preprocessing.data_validator import DataValidator


def main():

    print("=" * 70)
    print("NOVACART ENTERPRISE AI DATA LAKEHOUSE")
    print("=" * 70)

    print("\nStep 1: Loading Dataset...")
    loader = DataLoader()
    loader.load_dataset()

    print("\nStep 2: Profiling Dataset...")
    profiler = DataProfiler()
    profiler.profile()

    print("\nStep 3: Cleaning Dataset...")
    cleaner = DataCleaner()
    cleaner.clean_data()

    print("\nStep 4: Validating Dataset...")
    validator = DataValidator()
    validator.validate()

    print("\nPipeline Executed Successfully!")


if __name__ == "__main__":
    main()