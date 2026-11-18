
import pandas as pd
import pytest

from src.ingestion.excel_reader import read_excel_file


def test_read_excel_file_successfully(tmp_path):
    file_path = tmp_path / "test_clinics.xlsx"

    expected_df = pd.DataFrame({
        "Doctor": ["Doctor A", "Doctor B"],
        "Clinic": ["Clinic A", "Clinic B"]
    })

    expected_df.to_excel(
        file_path,
        index=False,
        sheet_name="Clinics"
    )

    df, sheet_name = read_excel_file(file_path)

    assert len(df) == 2
    assert list(df.columns) == ["Doctor", "Clinic"]
    assert sheet_name == "Clinics"


def test_read_excel_file_not_found(tmp_path):
    file_path = tmp_path / "missing.xlsx"

    with pytest.raises(FileNotFoundError):
        read_excel_file(file_path)
