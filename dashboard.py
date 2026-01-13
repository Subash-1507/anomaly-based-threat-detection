import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Threat Detection Dashboard",
    layout="wide"
)

st.title("🔐 Threat Detection using Anomaly Detection")
st.caption("Isolation Forest | System Behavior Analytics")

# -------------------------------
# Load data
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("anomaly_results.csv")

df = load_data()

# -------------------------------
# Sidebar controls
# -------------------------------
st.sidebar.header("⚙️ Controls")

threshold = st.sidebar.slider(
    "Anomaly Score Threshold",
    min_value=float(df["anomaly_score"].min()),
    max_value=float(df["anomaly_score"].max()),
    value=0.0,
    step=0.01
)

# -------------------------------
# Derive anomaly flag (UI logic)
# -------------------------------
df["is_anomaly"] = df["anomaly_score"] < threshold

filtered_anomalies = df[df["is_anomaly"]]

# -------------------------------
# Top metrics
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Events", len(df))
col2.metric("Detected Anomalies", len(filtered_anomalies))
col3.metric("Threshold", round(threshold, 3))

st.divider()

# -------------------------------
# Scatter plot: CPU vs Network
# -------------------------------
st.subheader("📊 CPU Usage vs Network Out")

fig_scatter = px.scatter(
    df,
    x="cpu_usage_avg",
    y="network_out_mb",
    color="is_anomaly",
    color_discrete_map={
        False: "#4CAF50",  # Green → Normal
        True: "#F44336"    # Red → Anomaly
    },
    labels={
        "cpu_usage_avg": "CPU Usage (%)",
        "network_out_mb": "Network Out (MB)",
        "is_anomaly": "Is Anomaly"
    },
    title="Behavior Clustering"
)

# Make anomalies stand out more
fig_scatter.update_traces(
    marker=dict(size=8),
    selector=dict(mode="markers")
)

fig_scatter.update_traces(
    marker=dict(size=12, line=dict(width=1, color="black")),
    selector=dict(name="True")
)

st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------------
# Anomaly score distribution
# -------------------------------
st.subheader("📈 Anomaly Score Distribution")

fig_hist = px.histogram(
    df,
    x="anomaly_score",
    nbins=50,
    title="Distribution of Anomaly Scores"
)

fig_hist.add_vline(
    x=threshold,
    line_dash="dash",
    line_color="red",
    annotation_text="Threshold",
    annotation_position="top right"
)

st.plotly_chart(fig_hist, use_container_width=True)

# -------------------------------
# Anomaly table
# -------------------------------
st.subheader("🚨 Detected Anomalies")

st.dataframe(
    filtered_anomalies.sort_values("anomaly_score"),
    use_container_width=True
)

# -------------------------------
# Download button (nice polish)
# -------------------------------
st.download_button(
    label="⬇️ Download Detected Anomalies",
    data=filtered_anomalies.to_csv(index=False),
    file_name="detected_anomalies.csv",
    mime="text/csv"
)
