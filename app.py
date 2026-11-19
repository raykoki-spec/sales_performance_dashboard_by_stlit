import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")
    df["date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["total_value"]
    return df

df = load_data()

st.title("Sales Performance Dashboard")
st.caption("Osman Wholesale Supplies, Nairobi")

st.info("Track sales performance by county and month. Use the filters on the left to explore specific regions or time periods." \
" Last updated: Monday 16 November 2026 at 08:00.")

# Filter 1: County
counties = ["All counties"] + sorted(df["county"].unique().tolist())
county = st.sidebar.selectbox("County", counties)


# Filter 2: Month
months = ["All months"] + sorted(df["date"].dt.strftime("%B %Y").unique().tolist())
month = st.sidebar.selectbox("Month", months)

# Apply filters
filtered = df.copy()
if county != "All counties": filtered = filtered[filtered["county"] == county]
if month != "All months": filtered = filtered[filtered["date"].dt.strftime("%B %Y") == month]


# KPI row
k1, k2, k3 = st.columns(3)
k1.metric("Total Revenue", f"KES {filtered['revenue'].sum():,.0f}")
k2.metric("Total Orders", len(filtered))
k3.metric("Avg Order Value", f"KES {filtered['revenue'].mean():,.0f}")