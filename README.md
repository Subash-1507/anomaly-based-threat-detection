# 🔐 Anomaly-Based Threat Detection Dashboard

This project demonstrates an **Anomaly-Based Threat Detection system** built using **Machine Learning (Isolation Forest)** and deployed as an **interactive Streamlit dashboard**.

> Academic Project – DMML (Cybersecurity)

---

## 📌 Problem Statement
Traditional rule-based security systems often fail to detect unknown or zero-day attacks.  
This project uses **unsupervised anomaly detection** to identify suspicious system behavior patterns.

---

## 🧠 Approach
- Synthetic system activity logs generated to simulate real-world behavior
- Features used:
  - Login attempts per minute
  - Files accessed per minute
  - Average CPU usage
  - Network outbound traffic
  - Process count
- **Isolation Forest** used to detect anomalies
- Anomaly scores visualized via interactive dashboard

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Streamlit
- Plotly
- DigitalOcean VM (development)

---

## 📊 Dashboard Features
- Real-time anomaly threshold control
- CPU vs Network behavior clustering
- Anomaly score distribution
- Detected anomalies table with export option

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python generate_data.py
python detect_anamolies.py
streamlit run dashboard.py
