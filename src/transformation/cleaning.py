
import pandas as pd


def clean_data(df):

    cleaned_df = df.copy()

    # Remove extra spaces from text columns
    text_columns = cleaned_df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:
        cleaned_df[column] = cleaned_df[column].apply(
            lambda value: value.strip()
            if isinstance(value, str)
            else value
        )

    # Standardize empty cells
    cleaned_df = cleaned_df.replace(r"^\s*$", pd.NA, regex=True)

    print("\nDATA TRANSFORMATION")
    print("-" * 40)
    print("Original rows:", len(df))
    print("Processed rows:", len(cleaned_df))
    print("Original columns:", len(df.columns))
    print("Processed columns:", len(cleaned_df.columns))

    return cleaned_df
