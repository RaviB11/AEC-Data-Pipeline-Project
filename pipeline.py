# pipeline.py
# An example ETL script for the AEC Project Data Pipeline.

import pandas as pd
from datetime import datetime

def perform_etl(source_file):
    """
    This function performs the Extract, Transform, and Load process.
    """
    print("Starting the ETL process...")

    # --- 1. EXTRACT ---
    # Read the raw data from the source CSV file.
    print(f"EXTRACT: Reading data from {source_file}...")
    try:
        df = pd.read_csv(source_file)
        print("...Data extracted successfully.")
    except FileNotFoundError:
        print(f"Error: Source file not found at {source_file}")
        return

    # --- 2. TRANSFORM ---
    print("TRANSFORM: Cleaning and transforming data...")
    
    # Data Quality Check: Handle missing values.
    # For this example, we'll fill missing 'Cost' with 0 and drop rows with missing dates.
    df['Cost'].fillna(0, inplace=True)
    df.dropna(subset=['StartDate', 'EndDate'], inplace=True)

    # Transform data types for accurate calculations.
    df['StartDate'] = pd.to_datetime(df['StartDate'])
    df['EndDate'] = pd.to_datetime(df['EndDate'])

    # Feature Engineering: Create a new 'Duration' column.
    df['DurationInDays'] = (df['EndDate'] - df['StartDate']).dt.days
    
    print("...Data transformed successfully.")
    print("...New 'DurationInDays' column added.")

    # --- 3. LOAD ---
    # Save the cleaned and transformed data to a new CSV file.
    # In a real-world scenario, this would load to a database or data warehouse (e.g., Azure Synapse).
    output_file = 'cleaned_projects.csv'
    print(f"LOAD: Saving cleaned data to {output_file}...")
    df.to_csv(output_file, index=False)
    print("...Data loaded successfully.")

    print("\nETL process complete!")
    print("\nPreview of the cleaned data:")
    print(df.head())

# --- Run the pipeline ---
if __name__ == "__main__":
    raw_data_file = 'projects.csv'
    perform_etl(raw_data_file)
