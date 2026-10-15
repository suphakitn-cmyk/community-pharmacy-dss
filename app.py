import os
import json
import html
import pandas as pd
import streamlit as st


# ============================================================
# COMMUNITY PHARMACY DSS
# FINAL DARK FUTURISTIC DASHBOARD
# ============================================================

st.set_page_config(
    page_title="Community Pharmacy DSS",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

METRICS_PATH = os.path.join(
    OUTPUT_DIR,
    "final_metrics.json"
)

PREDICTION_PATH = os.path.join(
    OUTPUT_DIR,
    "test_predictions.csv"
)

EXPIRY_PATH = os.path.join(
    OUTPUT_DIR,
    "expiry_monitoring_results.csv"
)

IMPORTANCE_PATH = os.path.join(
    OUTPUT_DIR,
    "gradient_boosting_feature_importance.csv"
)


# ============================================================
# DARK FUTURISTIC DESIGN SYSTEM
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 88% 4%,
                rgba(34, 211, 238, 0.08),
                transparent 24%
            ),
            radial-gradient(
                circle at 8% 92%,
                rgba(139, 92, 246, 0.08),
                transparent 27%
            ),
            #0A0E28;

        color: #F8FAFC;
    }


    .main .block-container {
        max-width: 1500px;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
    }


    /* ======================================================
       STREAMLIT TOP BAR
       IMPORTANT:
       Do NOT hide stToolbar because it contains
       the sidebar toggle button.
       ====================================================== */

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    .stDeployButton {
        display: none !important;
    }

    footer {
        visibility: hidden;
    }


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #0C1130 0%,
                #080C23 100%
            );

        border-right:
            1px solid rgba(34, 211, 238, 0.10);
    }


    section[data-testid="stSidebar"] > div {
        padding-top: 1.8rem;
    }


    section[data-testid="stSidebar"] * {
        color: #E2E8F0;
    }


    /* ======================================================
       SIDEBAR RADIO — CUSTOM DARK RADIO BUTTON
       ====================================================== */

    section[data-testid="stSidebar"] div[data-testid="stRadio"] > div {
        gap: 0.4rem !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label {
        display: flex !important;
        align-items: center !important;
        gap: 0.65rem !important;
        background: rgba(255,255,255,0.025) !important;
        border: 1px solid rgba(255,255,255,0.05) !important;
        border-radius: 12px !important;
        padding: 0.65rem 0.78rem !important;
        margin-bottom: 0.35rem !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label input[type="radio"] {
        appearance: none !important;
        -webkit-appearance: none !important;
        width: 15px !important;
        height: 15px !important;
        min-width: 15px !important;
        min-height: 15px !important;
        margin: 0 !important;
        padding: 0 !important;
        border: 1.5px solid #526080 !important;
        border-radius: 50% !important;
        background: transparent !important;
        box-shadow: none !important;
        outline: none !important;
        position: relative !important;
        cursor: pointer !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label input[type="radio"]:checked {
        border: 1.5px solid #22D3EE !important;
        background: rgba(34,211,238,0.08) !important;
        box-shadow: 0 0 8px rgba(34,211,238,0.30) !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label input[type="radio"]:checked::after {
        content: "" !important;
        position: absolute !important;
        width: 7px !important;
        height: 7px !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;
        border-radius: 50% !important;
        background: #22D3EE !important;
        box-shadow: 0 0 7px rgba(34,211,238,0.75) !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label p {
        color: #CBD5E1 !important;
        font-size: 0.80rem !important;
        font-weight: 500 !important;
        margin: 0 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label:has(input[type="radio"]:checked) {
        background: linear-gradient(90deg, rgba(34,211,238,0.10), rgba(139,92,246,0.07)) !important;
        border: 1px solid rgba(34,211,238,0.25) !important;
        box-shadow: inset 3px 0 0 #22D3EE, 0 0 16px rgba(34,211,238,0.04) !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label:has(input[type="radio"]:checked) p {
        color: #67E8F9 !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stRadio"] label:hover {
        background: rgba(34,211,238,0.055) !important;
        border-color: rgba(34,211,238,0.20) !important;
    }


    /* ======================================================
       TYPOGRAPHY
       ====================================================== */

    h1,
    h2,
    h3 {

        color:
            #F8FAFC !important;

        letter-spacing:
            -0.025em;
    }


    h1 {
        font-weight:
            800 !important;
    }


    h2,
    h3 {
        font-weight:
            700 !important;
    }


    p,
    li,
    label {
        color:
            #CBD5E1;
    }


    /* ======================================================
       HEADER
       ====================================================== */

    .dss-header {

        display:
            flex;

        justify-content:
            space-between;

        align-items:
            center;

        padding:
            1.15rem 1.35rem;

        margin-bottom:
            2rem;

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.055),
                rgba(255,255,255,0.018)
            );

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius:
            18px;

        box-shadow:
            0 0 35px rgba(34,211,238,0.035);
    }


    .brand-title {

        font-size:
            1.05rem;

        font-weight:
            800;

        color:
            #F8FAFC;

        letter-spacing:
            -0.01em;
    }


    .brand-subtitle {

        color:
            #94A3B8;

        font-size:
            0.73rem;

        margin-top:
            0.25rem;
    }


    .system-status {

        display:
            flex;

        align-items:
            center;

        gap:
            0.45rem;

        padding:
            0.45rem 0.75rem;

        border-radius:
            999px;

        background:
            rgba(34,211,238,0.06);

        border:
            1px solid rgba(34,211,238,0.18);

        color:
            #67E8F9;

        font-size:
            0.68rem;

        font-weight:
            800;

        letter-spacing:
            0.08em;
    }


    .status-dot {

        width:
            7px;

        height:
            7px;

        border-radius:
            50%;

        background:
            #22D3EE;

        box-shadow:
            0 0 10px #22D3EE;
    }


    /* ======================================================
       PAGE TITLE
       ====================================================== */

    .page-kicker {

        color:
            #22D3EE;

        font-size:
            0.70rem;

        font-weight:
            800;

        letter-spacing:
            0.16em;

        text-transform:
            uppercase;

        margin-bottom:
            0.35rem;
    }


    .page-description {

        color:
            #94A3B8;

        font-size:
            0.90rem;

        margin-bottom:
            1.5rem;
    }


    /* ======================================================
       GLASS CARD
       ====================================================== */

    .glass-card {

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.055),
                rgba(255,255,255,0.018)
            );

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius:
            18px;

        padding:
            1.25rem;

        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.025),
            0 15px 40px rgba(0,0,0,0.18);
    }


    /* ======================================================
       KPI
       ====================================================== */

    .kpi-grid {

        display:
            grid;

        grid-template-columns:
            repeat(4, minmax(0, 1fr));

        gap:
            1rem;

        margin:
            1rem 0 1.5rem 0;
    }


    .kpi-card {

        position:
            relative;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.065),
                rgba(255,255,255,0.025)
            );

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius:
            18px;

        padding:
            1.15rem 1.2rem;

        overflow:
            hidden;

        box-shadow:
            0 12px 30px rgba(0,0,0,0.12);
    }


    .kpi-card::before {

        content:
            "";

        position:
            absolute;

        top:
            0;

        left:
            0;

        width:
            45%;

        height:
            2px;

        background:
            linear-gradient(
                90deg,
                #22D3EE,
                #8B5CF6
            );
    }


    .kpi-label {

        color:
            #94A3B8;

        font-size:
            0.68rem;

        font-weight:
            700;

        letter-spacing:
            0.10em;

        text-transform:
            uppercase;
    }


    .kpi-value {

        color:
            #F8FAFC;

        font-size:
            2rem;

        font-weight:
            800;

        line-height:
            1.1;

        margin:
            0.55rem 0;
    }


    .kpi-caption {

        color:
            #64748B;

        font-size:
            0.70rem;
    }


    /* ======================================================
       STATUS
       ====================================================== */

    .status-grid {

        display:
            grid;

        grid-template-columns:
            repeat(4, minmax(0, 1fr));

        gap:
            1rem;
    }


    .status-card {

        background:
            rgba(255,255,255,0.035);

        border:
            1px solid rgba(255,255,255,0.07);

        border-radius:
            16px;

        padding:
            1rem;
    }


    .status-name {

        color:
            #94A3B8;

        font-size:
            0.73rem;

        font-weight:
            700;

        letter-spacing:
            0.08em;

        text-transform:
            uppercase;
    }


    .status-number {

        color:
            #F8FAFC;

        font-size:
            1.8rem;

        font-weight:
            800;

        margin-top:
            0.35rem;
    }


    .normal-dot {
        color:
            #22C55E;
    }

    .warning-dot {
        color:
            #F59E0B;
    }

    .critical-dot {
        color:
            #F97316;
    }

    .expired-dot {
        color:
            #EF4444;
    }


    /* ======================================================
       SECTION
       ====================================================== */

    .section-label {

        color:
            #F8FAFC;

        font-size:
            1rem;

        font-weight:
            750;

        margin-bottom:
            0.35rem;
    }


    .section-meta {

        color:
            #64748B;

        font-size:
            0.73rem;
    }


    /* ======================================================
       BARS
       ====================================================== */

    .bar-row {
        margin:
            0.8rem 0;
    }


    .bar-header {

        display:
            flex;

        justify-content:
            space-between;

        margin-bottom:
            0.35rem;
    }


    .bar-label {

        color:
            #CBD5E1;

        font-size:
            0.78rem;
    }


    .bar-value {

        color:
            #F8FAFC;

        font-size:
            0.78rem;

        font-weight:
            700;
    }


    .bar-track {

        width:
            100%;

        height:
            8px;

        border-radius:
            999px;

        background:
            rgba(255,255,255,0.06);

        overflow:
            hidden;
    }


    .bar-fill-cyan {

        height:
            100%;

        border-radius:
            999px;

        background:
            linear-gradient(
                90deg,
                #22D3EE,
                #38BDF8
            );

        box-shadow:
            0 0 14px rgba(34,211,238,0.25);
    }


    .bar-fill-purple {

        height:
            100%;

        border-radius:
            999px;

        background:
            linear-gradient(
                90deg,
                #8B5CF6,
                #A78BFA
            );

        box-shadow:
            0 0 14px rgba(139,92,246,0.22);
    }


    .bar-fill-green {

        height:
            100%;

        border-radius:
            999px;

        background:
            #22C55E;
    }


    .bar-fill-orange {

        height:
            100%;

        border-radius:
            999px;

        background:
            #F97316;
    }


    .bar-fill-red {

        height:
            100%;

        border-radius:
            999px;

        background:
            #EF4444;
    }


    /* ======================================================
       MODEL STATUS
       ====================================================== */

    .model-status {

        display:
            flex;

        align-items:
            center;

        justify-content:
            space-between;

        background:
            linear-gradient(
                110deg,
                rgba(34,211,238,0.06),
                rgba(139,92,246,0.06)
            );

        border:
            1px solid rgba(34,211,238,0.13);

        border-radius:
            16px;

        padding:
            1rem 1.15rem;

        margin-top:
            1rem;
    }


    .model-name {

        color:
            #F8FAFC;

        font-weight:
            750;
    }


    .model-meta {

        color:
            #94A3B8;

        font-size:
            0.74rem;

        margin-top:
            0.2rem;
    }


    .verified {

        color:
            #67E8F9;

        font-size:
            0.70rem;

        font-weight:
            800;

        letter-spacing:
            0.08em;
    }


    /* ======================================================
       CUSTOM DARK TABLE
       ====================================================== */

    .dark-table-wrapper {

        width:
            100%;

        overflow-x:
            auto;

        margin-top:
            0.9rem;

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius:
            16px;

        background:
            rgba(7, 11, 32, 0.75);

        box-shadow:
            0 12px 35px rgba(0,0,0,0.16);
    }


    .dark-table {

        width:
            100%;

        border-collapse:
            collapse;

        min-width:
            720px;

        font-size:
            0.76rem;
    }


    .dark-table thead th {

        position:
            sticky;

        top:
            0;

        z-index:
            2;

        background:
            #111936;

        color:
            #67E8F9;

        text-align:
            left;

        font-size:
            0.68rem;

        font-weight:
            800;

        letter-spacing:
            0.08em;

        text-transform:
            uppercase;

        padding:
            0.85rem 0.9rem;

        border-bottom:
            1px solid rgba(34,211,238,0.16);

        white-space:
            nowrap;
    }


    .dark-table tbody td {

        color:
            #CBD5E1;

        padding:
            0.72rem 0.9rem;

        border-bottom:
            1px solid rgba(255,255,255,0.045);

        white-space:
            nowrap;
    }


    .dark-table tbody tr {

        background:
            rgba(255,255,255,0.012);

        transition:
            background 0.15s ease;
    }


    .dark-table tbody tr:nth-child(even) {

        background:
            rgba(255,255,255,0.022);
    }


    .dark-table tbody tr:hover {

        background:
            rgba(34,211,238,0.055);
    }


    .table-count {

        color:
            #64748B;

        font-size:
            0.72rem;

        margin-top:
            0.65rem;
    }


    /* ======================================================
       TABLE BADGES
       ====================================================== */

    .badge {

        display:
            inline-block;

        padding:
            0.22rem 0.55rem;

        border-radius:
            999px;

        font-size:
            0.65rem;

        font-weight:
            800;
    }


    .badge-late {

        color:
            #FCA5A5;

        background:
            rgba(239,68,68,0.10);

        border:
            1px solid rgba(239,68,68,0.18);
    }


    .badge-not-late {

        color:
            #67E8F9;

        background:
            rgba(34,211,238,0.08);

        border:
            1px solid rgba(34,211,238,0.16);
    }


    .badge-normal {

        color:
            #86EFAC;

        background:
            rgba(34,197,94,0.08);

        border:
            1px solid rgba(34,197,94,0.16);
    }


    .badge-warning {

        color:
            #FCD34D;

        background:
            rgba(245,158,11,0.08);

        border:
            1px solid rgba(245,158,11,0.16);
    }


    .badge-critical {

        color:
            #FDBA74;

        background:
            rgba(249,115,22,0.08);

        border:
            1px solid rgba(249,115,22,0.16);
    }


    .badge-expired {

        color:
            #FCA5A5;

        background:
            rgba(239,68,68,0.08);

        border:
            1px solid rgba(239,68,68,0.16);
    }


    /* ======================================================
       INFO / WARNING
       ====================================================== */

    div[data-testid="stAlert"] {

        background:
            rgba(34,211,238,0.045);

        border:
            1px solid rgba(34,211,238,0.13);

        border-radius:
            14px;
    }


    /* ======================================================
       BUTTON
       ====================================================== */

    .stDownloadButton button {

        background:
            linear-gradient(
                90deg,
                rgba(34,211,238,0.12),
                rgba(139,92,246,0.12)
            ) !important;

        color:
            #E0F2FE !important;

        border:
            1px solid rgba(34,211,238,0.22) !important;

        border-radius:
            10px !important;
    }


    .stDownloadButton button:hover {

        border-color:
            rgba(34,211,238,0.45) !important;

        box-shadow:
            0 0 18px rgba(34,211,238,0.12);
    }


    /* ======================================================
       SLIDER
       ====================================================== */

    div[data-baseweb="slider"] div[role="slider"] {

        background-color:
            #22D3EE !important;

        box-shadow:
            0 0 10px rgba(34,211,238,0.45);
    }


/* ======================================================
   EXPIRY STATUS FILTER — CUSTOM CHECKBOX PILLS
   ====================================================== */

/* Filter label */
div[data-testid="stCheckbox"] {
    width: 100% !important;
}

/* Make each checkbox look like a dark status pill */
div[data-testid="stCheckbox"] label {
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    min-height: 44px !important;
    padding: 0.55rem 0.8rem 0.55rem 2.15rem !important;
    box-sizing: border-box !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    background: #111936 !important;
    color: #CBD5E1 !important;
    cursor: pointer !important;
    transition: all 0.18s ease !important;
}

/* Hide Streamlit's native checkbox without disabling it */
div[data-testid="stCheckbox"] label input[type="checkbox"] {
    position: absolute !important;
    opacity: 0 !important;
    width: 1px !important;
    height: 1px !important;
    margin: 0 !important;
    pointer-events: none !important;
}

/* Custom status indicator */
div[data-testid="stCheckbox"] label::before {
    content: "○" !important;
    position: absolute !important;
    left: 0.72rem !important;
    top: 50% !important;
    transform: translateY(-53%) !important;
    color: #64748B !important;
    font-size: 1.05rem !important;
    font-weight: 800 !important;
    line-height: 1 !important;
}

/* Selected state */
div[data-testid="stCheckbox"] label:has(input[type="checkbox"]:checked) {
    background: linear-gradient(135deg, rgba(34,211,238,0.16), rgba(34,211,238,0.07)) !important;
    background-color: #10283A !important;
    border-color: rgba(34,211,238,0.48) !important;
    color: #67E8F9 !important;
    box-shadow: 0 0 12px rgba(34,211,238,0.08) !important;
}

div[data-testid="stCheckbox"] label:has(input[type="checkbox"]:checked)::before {
    content: "✓" !important;
    color: #22D3EE !important;
    text-shadow: 0 0 8px rgba(34,211,238,0.45) !important;
}

/* Keep text/icons inside the pill aligned with the theme */
div[data-testid="stCheckbox"] label p,
div[data-testid="stCheckbox"] label span,
div[data-testid="stCheckbox"] label div {
    color: inherit !important;
}

/* Hover */
div[data-testid="stCheckbox"] label:hover {
    border-color: rgba(34,211,238,0.32) !important;
    background: rgba(34,211,238,0.07) !important;
    color: #E2E8F0 !important;
}

/* Keyboard focus */
div[data-testid="stCheckbox"] label:has(input[type="checkbox"]:focus-visible) {
    outline: 2px solid rgba(34,211,238,0.55) !important;
    outline-offset: 2px !important;
}

/* Remove extra vertical spacing inside the filter row */
div[data-testid="stCheckbox"] > label {
    margin-bottom: 0 !important;
}

       DIVIDER
       ====================================================== */

    hr {

        border-color:
            rgba(255,255,255,0.07) !important;
    }


    /* ======================================================
       RESPONSIVE
       ====================================================== */

    @media (max-width: 1000px) {

        .kpi-grid {

            grid-template-columns:
                repeat(2, minmax(0, 1fr));
        }


        .status-grid {

            grid-template-columns:
                repeat(2, minmax(0, 1fr));
        }


        .dss-header {

            flex-direction:
                column;

            align-items:
                flex-start;

            gap:
                0.8rem;
        }
    }


    @media (max-width: 600px) {

        .kpi-grid,
        .status-grid {

            grid-template-columns:
                1fr;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_metrics():

    with open(
        METRICS_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


@st.cache_data
def load_predictions():

    return pd.read_csv(
        PREDICTION_PATH
    )


@st.cache_data
def load_expiry():

    return pd.read_csv(
        EXPIRY_PATH
    )


@st.cache_data
def load_feature_importance():

    return pd.read_csv(
        IMPORTANCE_PATH
    )


try:

    metrics = load_metrics()

    predictions = load_predictions()

    expiry = load_expiry()

    importance = load_feature_importance()

except Exception as e:

    st.error(
        "ไม่สามารถโหลดข้อมูล Dashboard ได้"
    )

    st.code(
        str(e)
    )

    st.stop()


# ============================================================
# HELPERS
# ============================================================

def pct(value):

    return f"{value * 100:.2f}%"


def num(value):

    return f"{value:,}"


def safe(value):

    if pd.isna(value):

        return ""

    return html.escape(
        str(value)
    )


def prediction_badge(value):

    if int(value) == 1:

        return (
            '<span class="badge badge-late">'
            '● LATE'
            '</span>'
        )

    return (
        '<span class="badge badge-not-late">'
        '● NOT LATE'
        '</span>'
    )


def expiry_badge(value):

    value = str(value)

    mapping = {

        "Normal":
            "badge-normal",

        "Warning":
            "badge-warning",

        "Critical":
            "badge-critical",

        "Expired":
            "badge-expired"
    }

    css = mapping.get(
        value,
        "badge-not-late"
    )

    return (
        f'<span class="badge {css}">'
        f'{safe(value)}'
        '</span>'
    )


def render_dark_table(
    dataframe,
    columns,
    headers=None,
    max_rows=100,
    special_columns=None
):

    """
    Render a custom dark HTML table.

    dataframe:
        source dataframe

    columns:
        columns to display

    headers:
        optional display names

    special_columns:
        optional dictionary:
        {
            "column_name": "prediction",
            "column_name": "expiry"
        }
    """

    special_columns = (
        special_columns
        or {}
    )

    display_df = dataframe[
        [
            c for c in columns
            if c in dataframe.columns
        ]
    ].head(max_rows)

    if headers is None:

        headers = {
            c: c
            for c in display_df.columns
        }


    header_html = ""

    for col in display_df.columns:

        header_html += (
            "<th>"
            + safe(headers.get(col, col))
            + "</th>"
        )


    rows_html = ""

    for _, row in display_df.iterrows():

        rows_html += "<tr>"

        for col in display_df.columns:

            value = row[col]

            special = special_columns.get(
                col
            )

            if special == "prediction":

                cell = prediction_badge(
                    value
                )

            elif special == "expiry":

                cell = expiry_badge(
                    value
                )

            else:

                cell = safe(value)

            rows_html += (
                "<td>"
                + cell
                + "</td>"
            )

        rows_html += "</tr>"


    st.html(
        f"""
        <div class="dark-table-wrapper">

            <table class="dark-table">

                <thead>

                    <tr>
                        {header_html}
                    </tr>

                </thead>

                <tbody>
                    {rows_html}
                </tbody>

            </table>

        </div>

        <div class="table-count">
            Showing {len(display_df):,}
            of {len(dataframe):,} records
        </div>
        """
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        """
        <div style="
            padding: 0.3rem 0 1.2rem 0;
        ">

            <div style="
                font-size: 1.25rem;
                font-weight: 800;
                color: #F8FAFC;
                letter-spacing: -0.02em;
            ">
                💊 PHARMACY AI
            </div>

            <div style="
                color: #22D3EE;
                font-size: 0.68rem;
                font-weight: 800;
                letter-spacing: 0.12em;
                margin-top: 0.35rem;
            ">
                DECISION SUPPORT SYSTEM
            </div>

            <div style="
                color: #64748B;
                font-size: 0.70rem;
                margin-top: 0.45rem;
            ">
                Community Pharmacy DSS
            </div>

        </div>
        """
    )


    st.divider()


    st.caption(
        "COMMAND CENTER"
    )


    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Late Refill Risk",
            "Expiry Monitoring",
            "Model Evaluation"
        ],
        label_visibility="collapsed"
    )


    st.divider()


    st.html(
        """
        <div style="
            background:
                linear-gradient(
                    135deg,
                    rgba(34,211,238,0.055),
                    rgba(139,92,246,0.045)
                );

            border:
                1px solid rgba(34,211,238,0.12);

            border-radius:
                14px;

            padding:
                0.9rem;
        ">

            <div style="
                color: #67E8F9;
                font-size: 0.67rem;
                font-weight: 800;
                letter-spacing: 0.12em;
            ">
                SYSTEM STATUS
            </div>

            <div style="
                margin-top: 0.55rem;
                color: #CBD5E1;
                font-size: 0.78rem;
            ">
                ● VERIFIED
            </div>

            <div style="
                color: #64748B;
                font-size: 0.68rem;
                margin-top: 0.25rem;
            ">
                Prototype Mode
            </div>

        </div>
        """
    )


# ============================================================
# GLOBAL HEADER
# ============================================================

st.html(
    """
    <div class="dss-header">

        <div>

            <div class="brand-title">
                💊 Community Pharmacy Decision Support System
            </div>

            <div class="brand-subtitle">
                AI-powered pharmacy analytics & decision support
            </div>

        </div>

        <div class="system-status">

            <span class="status-dot"></span>

            SYSTEM VERIFIED

        </div>

    </div>
    """
)


# ============================================================
# PAGE 1 — OVERVIEW
# ============================================================

if page == "Overview":

    st.html(
        """
        <div class="page-kicker">
            COMMAND CENTER
        </div>
        """
    )


    st.title(
        "Pharmacy Intelligence Overview"
    )


    st.markdown(
        """
        <div class="page-description">
            ภาพรวมการวิเคราะห์และระบบสนับสนุนการตัดสินใจของร้านยา
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # KPI
    # --------------------------------------------------------

    st.html(
        f"""
        <div class="kpi-grid">

            <div class="kpi-card">

                <div class="kpi-label">
                    Test Predictions
                </div>

                <div class="kpi-value">
                    {num(metrics["test_rows"])}
                </div>

                <div class="kpi-caption">
                    Held-out test records
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    Model Accuracy
                </div>

                <div class="kpi-value">
                    {pct(metrics["accuracy"])}
                </div>

                <div class="kpi-caption">
                    Final test performance
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    Late Recall
                </div>

                <div class="kpi-value">
                    {pct(metrics["recall_late"])}
                </div>

                <div class="kpi-caption">
                    Detection capability
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    F1 Score
                </div>

                <div class="kpi-value">
                    {pct(metrics["f1_late"])}
                </div>

                <div class="kpi-caption">
                    Balanced performance
                </div>

            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # PREDICTION DISTRIBUTION
    # --------------------------------------------------------

    predicted_counts = (
        predictions[
            "predicted_is_late_refill"
        ]
        .value_counts()
    )


    not_late = int(
        predicted_counts.get(0, 0)
    )


    late = int(
        predicted_counts.get(1, 0)
    )


    max_prediction = max(
        not_late,
        late,
        1
    )


    # --------------------------------------------------------
    # EXPIRY
    # --------------------------------------------------------

    status_counts = (
        expiry[
            "expiry_status"
        ]
        .value_counts()
    )


    normal = int(
        status_counts.get(
            "Normal",
            0
        )
    )


    warning = int(
        status_counts.get(
            "Warning",
            0
        )
    )


    critical = int(
        status_counts.get(
            "Critical",
            0
        )
    )


    expired = int(
        status_counts.get(
            "Expired",
            0
        )
    )


    max_expiry = max(
        normal,
        warning,
        critical,
        expired,
        1
    )


    col1, col2 = st.columns(2)


    with col1:

        st.html(
            f"""
            <div class="glass-card">

                <div class="section-label">
                    Late Refill Prediction
                </div>

                <div class="section-meta">
                    Final model prediction distribution
                </div>


                <div class="bar-row">

                    <div class="bar-header">

                        <span class="bar-label">
                            Predicted Not Late
                        </span>

                        <span class="bar-value">
                            {num(not_late)}
                        </span>

                    </div>


                    <div class="bar-track">

                        <div
                            class="bar-fill-cyan"
                            style="
                                width:
                                {not_late / max_prediction * 100:.2f}%;
                            "
                        ></div>

                    </div>

                </div>


                <div class="bar-row">

                    <div class="bar-header">

                        <span class="bar-label">
                            Predicted Late
                        </span>

                        <span class="bar-value">
                            {num(late)}
                        </span>

                    </div>


                    <div class="bar-track">

                        <div
                            class="bar-fill-purple"
                            style="
                                width:
                                {late / max_prediction * 100:.2f}%;
                            "
                        ></div>

                    </div>

                </div>

            </div>
            """
        )


    with col2:

        st.html(
            f"""
            <div class="glass-card">

                <div class="section-label">
                    Inventory Expiry Status
                </div>

                <div class="section-meta">
                    Current inventory monitoring snapshot
                </div>


                <div class="bar-row">

                    <div class="bar-header">

                        <span class="bar-label">
                            Normal
                        </span>

                        <span class="bar-value">
                            {num(normal)}
                        </span>

                    </div>


                    <div class="bar-track">

                        <div
                            class="bar-fill-green"
                            style="
                                width:
                                {normal / max_expiry * 100:.2f}%;
                            "
                        ></div>

                    </div>

                </div>


                <div class="bar-row">

                    <div class="bar-header">

                        <span class="bar-label">
                            Warning
                        </span>

                        <span class="bar-value">
                            {num(warning)}
                        </span>

                    </div>


                    <div class="bar-track">

                        <div
                            class="bar-fill-orange"
                            style="
                                width:
                                {warning / max_expiry * 100:.2f}%;
                            "
                        ></div>

                    </div>

                </div>


                <div class="bar-row">

                    <div class="bar-header">

                        <span class="bar-label">
                            Critical
                        </span>

                        <span class="bar-value">
                            {num(critical)}
                        </span>

                    </div>


                    <div class="bar-track">

                        <div
                            class="bar-fill-orange"
                            style="
                                width:
                                {critical / max_expiry * 100:.2f}%;
                            "
                        ></div>

                    </div>

                </div>


                <div class="bar-row">

                    <div class="bar-header">

                        <span class="bar-label">
                            Expired
                        </span>

                        <span class="bar-value">
                            {num(expired)}
                        </span>

                    </div>


                    <div class="bar-track">

                        <div
                            class="bar-fill-red"
                            style="
                                width:
                                {expired / max_expiry * 100:.2f}%;
                            "
                        ></div>

                    </div>

                </div>

            </div>
            """
        )


    # --------------------------------------------------------
    # FINAL MODEL STATUS
    # --------------------------------------------------------

    st.html(
        f"""
        <div class="model-status">

            <div>

                <div class="model-name">
                    Gradient Boosting Classifier
                </div>

                <div class="model-meta">
                    {metrics["train_rows"]:,} training
                    ·
                    {metrics["validation_rows"]:,} validation
                    ·
                    {metrics["test_rows"]:,} test
                </div>

            </div>

            <div class="verified">
                ● FINAL MODEL VERIFIED
            </div>

        </div>
        """
    )


    st.info(
        "Prototype Dashboard — ข้อมูลเป็นข้อมูลสังเคราะห์ "
        "และผลการทำนายใช้ Test Set เพื่อสาธิตระบบ "
        "ไม่ใช่ระบบ Live Inference"
    )


# ============================================================
# PAGE 2 — LATE REFILL RISK
# ============================================================

elif page == "Late Refill Risk":

    st.html(
        """
        <div class="page-kicker">
            AI ANALYTICS
        </div>
        """
    )


    st.title(
        "Late Refill Risk"
    )


    st.markdown(
        """
        <div class="page-description">
            AI prediction monitor สำหรับประเมินความเสี่ยงการเติมยาล่าช้า
        </div>
        """,
        unsafe_allow_html=True
    )


    st.info(
        "ผลลัพธ์หน้านี้มาจาก Final Gradient Boosting Model "
        "บน Test Set เพื่อสาธิตระบบ "
        "ไม่ใช่การทำนายข้อมูลลูกค้าใหม่แบบ Live"
    )


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    predicted_counts = (
        predictions[
            "predicted_is_late_refill"
        ]
        .value_counts()
    )


    total = len(
        predictions
    )


    not_late = int(
        predicted_counts.get(
            0,
            0
        )
    )


    late = int(
        predicted_counts.get(
            1,
            0
        )
    )


    st.html(
        f"""
        <div
            class="kpi-grid"
            style="
                grid-template-columns:
                repeat(3,minmax(0,1fr));
            "
        >

            <div class="kpi-card">

                <div class="kpi-label">
                    Total Predictions
                </div>

                <div class="kpi-value">
                    {num(total)}
                </div>

                <div class="kpi-caption">
                    Test set
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    Predicted Not Late
                </div>

                <div class="kpi-value">
                    {num(not_late)}
                </div>

                <div class="kpi-caption">
                    Class 0
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    Predicted Late
                </div>

                <div class="kpi-value">
                    {num(late)}
                </div>

                <div class="kpi-caption">
                    Class 1
                </div>

            </div>

        </div>
        """
    )
        # --------------------------------------------------------
    # THRESHOLD
    # --------------------------------------------------------

    st.html(
        """
        <div class="glass-card">

            <div class="section-label">
                Threshold Control
            </div>

            <div class="section-meta">
                Adjust the probability threshold used to
                filter predicted late refill records
            </div>

        </div>
        """
    )


    threshold = st.slider(
        "Late Refill Probability Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.50,
        step=0.01
    )


    filtered = predictions[
        predictions[
            "late_refill_probability"
        ] >= threshold
    ].copy()


    st.html(
        f"""
        <div style="
            margin:
                0.8rem 0 1rem 0;

            color:
                #94A3B8;

            font-size:
                0.85rem;
        ">

            Probability ≥

            <span style="
                color:
                    #67E8F9;

                font-weight:
                    800;
            ">
                {threshold:.2f}
            </span>

            พบ

            <span style="
                color:
                    #F8FAFC;

                font-weight:
                    800;
            ">
                {len(filtered):,}
            </span>

            รายการ

        </div>
        """
    )


    min_probability = float(
        predictions[
            "late_refill_probability"
        ].min()
    )


    max_probability = float(
        predictions[
            "late_refill_probability"
        ].max()
    )


    st.caption(
        f"Test Set probability range: "
        f"{min_probability:.4f} – "
        f"{max_probability:.4f}"
    )


    # --------------------------------------------------------
    # CUSTOM DARK TABLE
    # --------------------------------------------------------

    render_dark_table(
        filtered,
        columns=[
            "prediction_id",
            "customer_id",
            "prediction_date",
            "age",
            "gender",
            "drug_category",
            "days_supplied",
            "history_cycles_count",
            "late_refill_probability",
            "predicted_is_late_refill"
        ],
        headers={
            "prediction_id":
                "Prediction ID",

            "customer_id":
                "Customer ID",

            "prediction_date":
                "Prediction Date",

            "age":
                "Age",

            "gender":
                "Gender",

            "drug_category":
                "Drug Category",

            "days_supplied":
                "Days Supplied",

            "history_cycles_count":
                "History Cycles",

            "late_refill_probability":
                "Late Probability",

            "predicted_is_late_refill":
                "Prediction"
        },
        max_rows=100,
        special_columns={
            "predicted_is_late_refill":
                "prediction"
        }
    )


    st.caption(
        "แสดงสูงสุด 100 รายการบนหน้าจอ "
        "สามารถดาวน์โหลดข้อมูลที่กรองทั้งหมดได้ด้านล่าง"
    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    csv_data = filtered.to_csv(
        index=False
    ).encode(
        "utf-8-sig"
    )


    st.download_button(
        label="⬇ Download Filtered Predictions",
        data=csv_data,
        file_name="late_refill_risk_filtered.csv",
        mime="text/csv"
    )


# ============================================================
# PAGE 3 — EXPIRY MONITORING
# ============================================================

elif page == "Expiry Monitoring":

    st.html(
        """
        <div class="page-kicker">
            INVENTORY CONTROL
        </div>
        """
    )


    st.title(
        "Expiry Monitoring"
    )


    st.markdown(
        """
        <div class="page-description">
            ระบบติดตามสถานะวันหมดอายุของสินค้าใน Inventory
        </div>
        """,
        unsafe_allow_html=True
    )


    st.warning(
        "เกณฑ์วันหมดอายุเป็น Prototype Rule "
        "เพื่อสาธิตระบบ ไม่ใช่ข้อกำหนดทางกฎหมายหรือ SOP "
        "ที่ผ่านการรับรอง"
    )


    # --------------------------------------------------------
    # STATUS COUNTS
    # --------------------------------------------------------

    status_counts = (
        expiry[
            "expiry_status"
        ]
        .value_counts()
    )


    normal = int(
        status_counts.get(
            "Normal",
            0
        )
    )


    warning = int(
        status_counts.get(
            "Warning",
            0
        )
    )


    critical = int(
        status_counts.get(
            "Critical",
            0
        )
    )


    expired = int(
        status_counts.get(
            "Expired",
            0
        )
    )


    st.html(
        f"""
        <div class="status-grid">

            <div class="status-card">

                <div class="status-name">
                    <span class="normal-dot">
                        ●
                    </span>
                    Normal
                </div>

                <div class="status-number">
                    {num(normal)}
                </div>

            </div>


            <div class="status-card">

                <div class="status-name">
                    <span class="warning-dot">
                        ●
                    </span>
                    Warning
                </div>

                <div class="status-number">
                    {num(warning)}
                </div>

            </div>


            <div class="status-card">

                <div class="status-name">
                    <span class="critical-dot">
                        ●
                    </span>
                    Critical
                </div>

                <div class="status-number">
                    {num(critical)}
                </div>

            </div>


            <div class="status-card">

                <div class="status-name">
                    <span class="expired-dot">
                        ●
                    </span>
                    Expired
                </div>

                <div class="status-number">
                    {num(expired)}
                </div>

            </div>

        </div>
        """
    )


    st.divider()


    # --------------------------------------------------------
    # FILTER
    # --------------------------------------------------------

    st.html(
        """
        <div style="
            color: #CBD5E1;
            font-size: 0.85rem;
            font-weight: 700;
            margin: 0.15rem 0 0.65rem 0;
        ">
            กรองสถานะ
        </div>
        """
    )


    filter_cols = st.columns(
        4,
        gap="small"
    )


    with filter_cols[0]:

        normal_selected = st.checkbox(
            "Normal",
            value=True,
            key="expiry_filter_normal"
        )


    with filter_cols[1]:

        warning_selected = st.checkbox(
            "Warning",
            value=True,
            key="expiry_filter_warning"
        )


    with filter_cols[2]:

        critical_selected = st.checkbox(
            "Critical",
            value=True,
            key="expiry_filter_critical"
        )


    with filter_cols[3]:

        expired_selected = st.checkbox(
            "Expired",
            value=True,
            key="expiry_filter_expired"
        )


    # --------------------------------------------------------
    # BUILD SELECTED STATUS LIST
    # --------------------------------------------------------

    selected_status = []


    if normal_selected:

        selected_status.append(
            "Normal"
        )


    if warning_selected:

        selected_status.append(
            "Warning"
        )


    if critical_selected:

        selected_status.append(
            "Critical"
        )


    if expired_selected:

        selected_status.append(
            "Expired"
        )


    # --------------------------------------------------------
    # FILTER DATA
    # --------------------------------------------------------

    filtered_expiry = expiry[
        expiry[
            "expiry_status"
        ].isin(
            selected_status
        )
    ].copy()


    st.html(
        f"""
        <div class="glass-card">

            <div class="section-label">
                Inventory / Expiry Details
            </div>

            <div class="section-meta">
                Showing
                {len(filtered_expiry):,}
                of
                {len(expiry):,}
                batches
            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # CUSTOM DARK TABLE
    # --------------------------------------------------------

    render_dark_table(
        filtered_expiry,
        columns=[
            "batch_id",
            "drug_id",
            "drug_name",
            "drug_category",
            "stock_quantity",
            "unit_price",
            "received_date",
            "expiry_date",
            "snapshot_date",
            "days_to_expiry",
            "expiry_status"
        ],
        headers={
            "batch_id":
                "Batch ID",

            "drug_id":
                "Drug ID",

            "drug_name":
                "Drug Name",

            "drug_category":
                "Category",

            "stock_quantity":
                "Stock",

            "unit_price":
                "Unit Price",

            "received_date":
                "Received",

            "expiry_date":
                "Expiry Date",

            "snapshot_date":
                "Snapshot",

            "days_to_expiry":
                "Days to Expiry",

            "expiry_status":
                "Status"
        },
        max_rows=120,
        special_columns={
            "expiry_status":
                "expiry"
        }
    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    csv_data = filtered_expiry.to_csv(
        index=False
    ).encode(
        "utf-8-sig"
    )


    st.download_button(
        label="⬇ Download Expiry Data",
        data=csv_data,
        file_name="expiry_monitoring_filtered.csv",
        mime="text/csv"
    )


# ============================================================
# PAGE 4 — MODEL EVALUATION
# ============================================================

elif page == "Model Evaluation":

    st.html(
        """
        <div class="page-kicker">
            AI MODEL CONTROL
        </div>
        """
    )


    st.title(
        "Model Evaluation"
    )


    st.markdown(
        """
        <div class="page-description">
            Final performance and interpretation of the
            Gradient Boosting model
        </div>
        """,
        unsafe_allow_html=True
    )


    st.info(
        "Test Set ถูกเก็บไว้โดยไม่ใช้ในการเลือก Hyperparameters "
        "และถูกใช้เฉพาะสำหรับ Final Evaluation"
    )


    # --------------------------------------------------------
    # MODEL CONFIGURATION
    # --------------------------------------------------------

    st.html(
        """
        <div class="glass-card">

            <div class="section-label">
                Final Model Configuration
            </div>

            <div class="section-meta">
                Gradient Boosting Classifier
            </div>

        </div>
        """
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "N Estimators",
            metrics["n_estimators"]
        )


    with c2:

        st.metric(
            "Learning Rate",
            metrics["learning_rate"]
        )


    with c3:

        st.metric(
            "Max Depth",
            metrics["max_depth"]
        )


    st.html(
        f"""
        <div class="model-status">

            <div>

                <div class="model-name">
                    Gradient Boosting Classifier
                </div>

                <div class="model-meta">
                    Train
                    {metrics["train_rows"]:,}

                    · Validation
                    {metrics["validation_rows"]:,}

                    · Test
                    {metrics["test_rows"]:,}
                </div>

            </div>

            <div class="verified">
                ● VERIFIED
            </div>

        </div>
        """
    )


    st.divider()


    # --------------------------------------------------------
    # FINAL PERFORMANCE
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-label">
            Final Test Performance
        </div>
        """
    )


    st.html(
        f"""
        <div
            class="kpi-grid"
            style="
                grid-template-columns:
                repeat(5,minmax(0,1fr));
            "
        >

            <div class="kpi-card">

                <div class="kpi-label">
                    Accuracy
                </div>

                <div class="kpi-value">
                    {pct(metrics["accuracy"])}
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    Precision
                </div>

                <div class="kpi-value">
                    {pct(metrics["precision_late"])}
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    Recall
                </div>

                <div class="kpi-value">
                    {pct(metrics["recall_late"])}
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    F1
                </div>

                <div class="kpi-value">
                    {pct(metrics["f1_late"])}
                </div>

            </div>


            <div class="kpi-card">

                <div class="kpi-label">
                    ROC-AUC
                </div>

                <div class="kpi-value">
                    {metrics["roc_auc"]:.4f}
                </div>

            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-label">
            Confusion Matrix
        </div>

        <div class="section-meta">
            Final model results on the held-out Test Set
        </div>
        """
    )


    cm = metrics[
        "confusion_matrix"
    ]


    cm_df = pd.DataFrame(
        cm,
        index=[
            "Actual Not Late",
            "Actual Late"
        ],
        columns=[
            "Predicted Not Late",
            "Predicted Late"
        ]
    )


    cm_html = f"""
    <div class="dark-table-wrapper">

        <table class="dark-table">

            <thead>

                <tr>
                    <th></th>
                    <th>Predicted Not Late</th>
                    <th>Predicted Late</th>
                </tr>

            </thead>

            <tbody>

                <tr>

                    <td>
                        <strong>
                            Actual Not Late
                        </strong>
                    </td>

                    <td>
                        {num(cm_df.iloc[0, 0])}
                    </td>

                    <td>
                        {num(cm_df.iloc[0, 1])}
                    </td>

                </tr>


                <tr>

                    <td>
                        <strong>
                            Actual Late
                        </strong>
                    </td>

                    <td>
                        {num(cm_df.iloc[1, 0])}
                    </td>

                    <td>
                        {num(cm_df.iloc[1, 1])}
                    </td>

                </tr>

            </tbody>

        </table>

    </div>
    """


    st.html(
        cm_html
    )


    st.divider()


    # --------------------------------------------------------
    # FEATURE IMPORTANCE
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-label">
            Feature Importance
        </div>

        <div class="section-meta">
            Importance extracted from the final
            Gradient Boosting model
        </div>
        """
    )


    importance_display = (
        importance
        .sort_values(
            "importance_percent",
            ascending=False
        )
        .copy()
    )


    max_importance = float(
        importance_display[
            "importance_percent"
        ].max()
    )


    for _, row in importance_display.iterrows():

        feature = str(
            row["base_feature"]
        )

        value = float(
            row["importance_percent"]
        )


        if max_importance > 0:

            width = (
                value
                / max_importance
                * 100
            )

        else:

            width = 0


        st.html(
            f"""
            <div class="bar-row">

                <div class="bar-header">

                    <span class="bar-label">
                        {safe(feature)}
                    </span>

                    <span class="bar-value">
                        {value:.2f}%
                    </span>

                </div>


                <div class="bar-track">

                    <div
                        class="bar-fill-purple"
                        style="
                            width:
                            {width:.2f}%;
                        "
                    ></div>

                </div>

            </div>
            """
        )


    # --------------------------------------------------------
    # FEATURE IMPORTANCE TABLE
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-label"
             style="margin-top:1.5rem;">
            Feature Importance Details
        </div>
        """
    )


    render_dark_table(
        importance_display,
        columns=[
            "rank",
            "base_feature",
            "importance_percent"
        ],
        headers={
            "rank":
                "Rank",

            "base_feature":
                "Feature",

            "importance_percent":
                "Importance"
        },
        max_rows=20
    )


    st.html(
        """
        <div style="
            margin-top: 1rem;
            color: #64748B;
            font-size: 0.72rem;
            line-height: 1.6;
        ">
            Feature importance indicates the relative contribution
            of variables to the model's predictive decisions.
            It does not imply causal relationships.
        </div>
        """
    )
    # ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div style="
        text-align: center;

        color:
            #475569;

        font-size:
            0.68rem;

        padding:
            2rem 0 0.5rem 0;

        letter-spacing:
            0.05em;
    ">

        COMMUNITY PHARMACY DSS
        ·
        DARK FUTURISTIC PROTOTYPE
        ·
        SYNTHETIC DATA

    </div>
    """
)