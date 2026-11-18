
from pathlib import Path
import pandas as pd


def read_excel_file(file_path):
    """
    Read the first worksheet from an Excel file.
    Returns the DataFrame and the original worksheet name.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {file_path}"
        )

    excel_file = pd.ExcelFile(file_path)

    if not excel_file.sheet_names:
        raise ValueError("The Excel file contains no worksheets.")

    sheet_name = excel_file.sheet_names[0]

    df = pd.read_excel(
        excel_file,
        sheet_name=sheet_name
    )

    print("\n1. DATA INGESTION")
    print("Source:", file_path)
    print("Worksheet:", sheet_name)
    print("Records:", len(df))
    print("Columns:", len(df.columns))

    return df, sheet_name
