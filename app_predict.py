import streamlit as st
import pandas as pd
import joblib
from scripts.app_function import calendar_features
from datetime import date

model = joblib.load("/home/onyxia/work/Python_Project_2A/joblib/ridge_pipeline.joblib")
NUM_FEATURES = [
    "QV2M",
    "CLRSKY_SFC_SW_DWN",
    "ALLSKY_SFC_SW_DWN",
    "saison",
    "PS",
    "RH2M",
    "GWETROOT",
    "T2M_RANGE", 
    "month",
    "is_weekend",
]
CAT_FEATURES = ["Regions"]

# --------Streamlit UI------------------
st.set_page_config(
    page_title="Electricity Consumption Prediction",
    layout="centered",
)

st.title("Daily Electricity Consumption Prediction")

st.markdown(
    """
This application uses the **Ridge regression** model built in the project 
to predict daily electricity consumption (MWh) by region.
"""
)

st.markdown("### 1. Selection of the region and the date")

col_1, col_2 = st.columns(2)

with col_1:
    region = st.selectbox(
        "Région",
        [
            "Auvergne-Rhône-Alpes",
            "Bourgogne-Franche-Comté",
            "Bretagne",
            "Centre-Val de Loire",
            "Grand Est",
            "Hauts-de-France",
            "Île-de-France",
            "Normandie",
            "Nouvelle-Aquitaine",
            "Occitanie",
            "Pays de la Loire",
            "Provence-Alpes-Côte d'Azur",
        ],
        index=0, 
    )

with col_2:
    forecast_date = st.date_input(
        "Date ",
        value=date(2024, 1, 15),
        min_value=date(2020, 1, 1),
        max_value=date(2025, 12, 31),
    )
month, is_weekend, saison = calendar_features(forecast_date)
st.markdown("### 2. Meteorological variables")
sub_col1, sub_col2 = st.columns(2)

with sub_col1:
    qv2m = st.number_input("QV2M (humidity)", value=0.007)
    rh2m = st.number_input("RH2M (Humidity 2m) (%)", value=70.0)
    ps = st.number_input("Pressure (Pa)", value=97.706)
    gwetroot = st.number_input("GWETROOT(Soil moisture)", value=0.6)

with sub_col2:
    clrsky = st.number_input("CLRSKY_SFC_SW_DWN (Radiation clear-sky) (W/m²)", value=6.86)
    allsky = st.number_input("ALLSKY_SFC_SW_DWN (Radiation all-sky) (W/m²)", value=5.494)
    t2m_range = st.number_input("T2M_RANGE (°C)", value=5.310)

# -------Build input and predict-------
st.markdown("---")
if st.button("Predict"):
    x_dict = {
        "QV2M": qv2m,
        "CLRSKY_SFC_SW_DWN": clrsky,
        "ALLSKY_SFC_SW_DWN": allsky,
        "PS": ps,
        "RH2M": rh2m,
        "GWETROOT": gwetroot,
        "T2M_RANGE": t2m_range,
        "month": month,
        "is_weekend": is_weekend,
        "saison": saison,
        "Regions": region,
    }

    X_new = pd.DataFrame([x_dict])

    # Predict
    y_pred = model.predict(X_new)[0]

    st.subheader("Prediction result")
    st.metric(
        "Predicted electricity consumption (MWh)",
        f"{y_pred:,.0f}".replace(",", " "),
    )

    st.caption(
        "The prediction is based on a Ridge model trained on data from 2020–2024. "
    )
else:
    st.info("Please enter the values and click **« Predict »**.")
