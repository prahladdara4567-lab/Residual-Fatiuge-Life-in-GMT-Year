import streamlit as st
from GMT_engine import calculate_fatigue_life

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(page_title="IRS Simplified Fatigue Assessment")

st.title("IRS Simplified Fatigue Assessment")

# ============================================================
# LOADING TYPE
# ============================================================

loading_type = st.selectbox(
    "Loading Type",
    ["25T", "32.5T"],
    key="loading_type"
)

# ============================================================
# TRAIN TYPE
# ============================================================

if loading_type == "25T":

    train = st.selectbox(
        "Train Type",
        [
            "Train-1",
            "Train-2",
            "Train-3",
            "Train-4",
            "Train-5",
            "Train-6",
            "Train-7",
            "Train-8",
            "Train-9",
            "Train-10",
            "Train-11",
        ],
        key="train25"
    )

else:

    train = st.selectbox(
        "Train Type",
        [
            "Train-1",
            "Train-2",
            "Train-3",
            "Train-4",
            "Train-5",
            "Train-6",
            "Train-7",
        ],
        key="train32"
    )

# ============================================================
# SPAN
# ============================================================

span = st.selectbox(
    "Span (m)",
    [
        0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5,
        6, 7, 8, 9, 10, 12.5, 15, 17.5, 20,
        25, 30, 35, 40, 45, 50, 60, 70, 80,
        90, 100
    ],
    key="span"
)

# ============================================================
# INPUTS
# ============================================================

annual_gmt = st.number_input(
    "Annual Traffic (GMT/Year)",
    min_value=0.0,
    value=25.0
)

stress_range = st.number_input(
    "Stress Range (MPa)",
    min_value=0.0,
    value=50.0
)

detail_category = st.selectbox(
    "Detail Category",
    [
        "36","50","56","63",
        "71","80","90","100",
        "112","125","140","160"
    ],
    key="detail_category"
)

consumed_gmt_years = st.number_input(
    "Consumed GMT Years",
    min_value=0.0,
    value=1000.0
)

# ============================================================
# TRACK TYPE
# ============================================================

track_type = st.radio(
    "Track Type",
    ["Single Track", "Double Track"]
)

single_track = track_type == "Single Track"

delta_sigma1 = None
delta_sigma12 = None

if not single_track:

    delta_sigma1 = st.number_input(
        "Δσ1 (MPa)",
        min_value=0.0,
        value=80.0
    )

    delta_sigma12 = st.number_input(
        "Δσ1+2 (MPa)",
        min_value=0.0,
        value=100.0
    )

# ============================================================
# CALCULATE
# ============================================================

if st.button("Calculate Fatigue Life"):

    result = calculate_fatigue_life(
        loading_type=loading_type,
        span=span,
        train=train,
        annual_gmt=annual_gmt,
        stress_range=stress_range,
        detail_category=detail_category,
        consumed_gmt_years=consumed_gmt_years,
        single_track=single_track,
        delta_sigma1=delta_sigma1,
        delta_sigma12=delta_sigma12
    )

    st.subheader("Results")

    for key, value in result.items():
        st.write(f"**{key}** : {value}")