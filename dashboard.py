import streamlit as st
import psutil
import pandas as pd
import time
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="System Resource Monitor & Performance Logger    ",
    page_icon="🖥",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.metric-card {
    background-color: #1e1e2f;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 0 12px rgba(0,0,0,0.3);
}
.metric-title {
    font-size: 16px;
    color: #bbb;
}
.metric-value {
    font-size: 34px;
    font-weight: bold;
    color: white;
}
.alert-high {
    color: red;
    font-weight: bold;
}
.alert-ok {
    color: #00ff99;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🖥 System Resource Monitor & Performance Logger Dashboard")
st.caption("Real-time system performance tracking & health analytics")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙ Settings")
refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 1, 10, 2)
show_network = st.sidebar.checkbox("Show Network Usage", True)
show_logs = st.sidebar.checkbox("Show Historical Logs", True)

# ---------------- LIVE SYSTEM DATA ----------------
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
net = psutil.net_io_counters()

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

def metric_card(title, value, unit="%"):
    color = "#00ff99" if value < 80 else "red"
    return f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color:{color};">{value}{unit}</div>
    </div>
    """

with col1:
    st.markdown(metric_card("CPU Usage", cpu), unsafe_allow_html=True)

with col2:
    st.markdown(metric_card("RAM Usage", ram), unsafe_allow_html=True)

with col3:
    st.markdown(metric_card("Disk Usage", disk), unsafe_allow_html=True)

# ---------------- ALERT STATUS ----------------
st.subheader("🚨 System Health Status")

if cpu > 85 or ram > 85:
    st.error("⚠ High System Load Detected!")
else:
    st.success("✅ System Running Normally")

# ---------------- NETWORK SECTION ----------------
if show_network:
    st.subheader("🌐 Network Usage")
    net_col1, net_col2 = st.columns(2)

    net_col1.metric("Bytes Sent", f"{net.bytes_sent / 1024 / 1024:.2f} MB")
    net_col2.metric("Bytes Received", f"{net.bytes_recv / 1024 / 1024:.2f} MB")

# ---------------- HISTORICAL LOGS ----------------
if show_logs:
    try:
        data = pd.read_csv("data/system_logs.csv",
            names=["Time", "CPU", "RAM", "Disk", "Sent", "Recv"])

        st.subheader("📊 Performance History")

        fig = px.line(
            data.tail(200),
            x="Time",
            y=["CPU", "RAM", "Disk"],
            title="CPU / RAM / Disk Usage Over Time"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📋 Recent Logs")
        st.dataframe(data.tail(50))

    except:
        st.warning("⚠ No log data found. Start logger.py first.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built by: GARVIT RASTOGI. Using Python, psutil, Streamlit • © 2024 System Resource Monitor & Performance Logger Project")

# ---------------- AUTO REFRESH ----------------
time.sleep(refresh_rate)
st.rerun()
