
import pandas as pd

from src.transformation.cleaning import clean_data


def test_clean_data_preserves_all_records():

    df = pd.DataFrame({
        "العيادة (Clinic)": [" جراحة العظام ", "أمراض القلب"],
        "الطبيب (Doctor)": [" د-أحمد ", "د-محمد"],
        "الدرجة العلمية (Qualification)": ["استشاري", None]
    })

    cleaned_df = clean_data(df)

    assert len(cleaned_df) == 2


def test_clean_data_removes_extra_spaces():

    df = pd.DataFrame({
        "العيادة (Clinic)": [" جراحة العظام "],
        "الطبيب (Doctor)": [" د-أحمد "]
    })

    cleaned_df = clean_data(df)

    assert cleaned_df.iloc[0]["العيادة (Clinic)"] == "جراحة العظام"
    assert cleaned_df.iloc[0]["الطبيب (Doctor)"] == "د-أحمد"


def test_clean_data_preserves_missing_values():

    df = pd.DataFrame({
        "الطبيب (Doctor)": ["د-أحمد"],
        "الدرجة العلمية (Qualification)": [None]
    })

    cleaned_df = clean_data(df)

    assert pd.isna(
        cleaned_df.iloc[0]["الدرجة العلمية (Qualification)"]
    )
