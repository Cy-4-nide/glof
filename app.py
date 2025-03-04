import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime

# Streamlit UI Setup - Move this to the very top
st.set_page_config(page_title="GLOF Early Warning System", layout="wide")

# Fetch latest sensor data
@st.cache_data(ttl=60)  # Cache the function for 60 seconds to avoid hitting the database too often
def fetch_latest_data():
    conn = sqlite3.connect("glof_data.db")
    query = "SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 100"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Streamlit UI Setup
st.title("🌊 GLOF Early Warning Dashboard")

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")
time_range = st.sidebar.slider("Select Time Range (hours)", 1, 48, 12)
refresh_time = st.sidebar.slider("Auto Refresh Interval (seconds)", 5, 60, 10)

# Auto Refresh Placeholder
placeholder = st.empty()

def update_dashboard():
    df = fetch_latest_data()
    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
        df_filtered = df[df["timestamp"] >= pd.Timestamp.now(tz='UTC') - pd.Timedelta(hours=time_range)]
        
        # Ensure GLOF_Risk exists
        glof_threshold = 5.0
        if "GLOF_Risk" not in df.columns:
            st.warning("⚠️ GLOF Risk Data Not Available - Generating Based on Water Level")
            df["GLOF_Risk"] = (df["water_level_m"] > glof_threshold).astype(int)
        
        # Display Data
        st.subheader("📊 Live Sensor Data (Metric Units)")
        st.write(df)
        
        # Graphs
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📈 Water Level Over Time (Meters)")
            fig = px.line(df_filtered, x="timestamp", y="water_level_m", 
                          title="📊 Real-Time Water Levels (m)",
                          labels={"water_level_m": "Water Level (m)", "timestamp": "Time"},
                          markers=True, line_shape='spline')
            st.plotly_chart(fig, use_container_width=True, key="water_level_chart")
        
        with col2:
            st.subheader("☁️ Weather Trends (°C, %, mm)")
            df_melted = df_filtered.melt(id_vars=["timestamp"], 
                                         value_vars=["temperature_c", "humidity", "rainfall_mm"],
                                         var_name="Weather Parameter", 
                                         value_name="Value")
            fig2 = px.line(df_melted, x="timestamp", y="Value", color="Weather Parameter",
                           title="🌡️ Temperature (°C), Humidity (%), Rainfall (mm) Trends",
                           labels={"Value": "Measurement", "timestamp": "Time"},
                           markers=True, line_shape="spline")
            st.plotly_chart(fig2, use_container_width=True, key="weather_trends_chart")
        
        # Risk Status & Alerts
        latest_water_level = df.iloc[0]["water_level_m"]
        risk_status = "✅ Safe"
        if latest_water_level > 4.5:
            risk_status = "⚠️ High Risk! Immediate Action Required!"
        
        st.subheader("🚨 GLOF Risk Status")
        st.markdown(f"### {risk_status}", unsafe_allow_html=True)
        
        # Display live time
        st.sidebar.text(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Initial update
update_dashboard()

# Use a button to refresh data manually
if st.button("Refresh Data"):
    update_dashboard()  # Trigger a manual refresh
