from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR
OUTPUT_DIR = BASE_DIR
FILE_1 = DATA_DIR / "Unemployment in India.csv"
FILE_2 = DATA_DIR / "Unemployment_Rate_upto_11_2020.csv"

def clean_common(df):
    df.columns = df.columns.str.strip()
    for column in df.select_dtypes(include=["object", "string"]).columns:
        df[column] = df[column].astype("string").str.strip()
        df[column] = df[column].replace("", pd.NA)
    df = df.dropna(how="all").copy()
    df = df.drop_duplicates().copy()
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    return df

def clean_first_dataset(path):
    df = pd.read_csv(path)
    df = clean_common(df)
    numeric_columns = [
        "Estimated Unemployment Rate (%)",
        "Estimated Employed",
        "Estimated Labour Participation Rate (%)"
    ]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df["Frequency"] = df["Frequency"].str.strip().str.title()
    df["Region"] = df["Region"].str.strip()
    df["Area"] = df["Area"].str.strip().str.title()
    df = df.dropna(subset=["Region", "Date", "Frequency", "Area"])
    df = df.dropna(subset=numeric_columns)
    df = df.drop_duplicates()
    return df.sort_values(["Date", "Region", "Area"]).reset_index(drop=True)

def clean_second_dataset(path):
    df = pd.read_csv(path)
    df = clean_common(df)
    numeric_columns = [
        "Estimated Unemployment Rate (%)",
        "Estimated Employed",
        "Estimated Labour Participation Rate (%)",
        "longitude",
        "latitude"
    ]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df["Frequency"] = df["Frequency"].str.strip().str.upper()
    df["Region"] = df["Region"].str.strip()
    df["Region.1"] = df["Region.1"].str.strip().str.title()
    df = df.dropna(subset=["Region", "Date", "Frequency", "Region.1"])
    df = df.dropna(subset=numeric_columns)
    df = df.drop_duplicates()
    return df.sort_values(["Date", "Region"]).reset_index(drop=True)

def main():
    first = clean_first_dataset(FILE_1)
    second = clean_second_dataset(FILE_2)
    first.to_csv(OUTPUT_DIR / "unemployment_india_cleaned.csv", index=False)
    second.to_csv(OUTPUT_DIR / "unemployment_rate_upto_nov2020_cleaned.csv", index=False)
    print("Preprocessing completed.")
    print(f"Dataset 1: {first.shape[0]} rows, {first.shape[1]} columns")
    print(f"Dataset 2: {second.shape[0]} rows, {second.shape[1]} columns")
    print("Cleaned datasets saved in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
