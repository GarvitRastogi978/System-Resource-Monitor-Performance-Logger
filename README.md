# 🖥 System Resource Monitor & Performance Logger

A **professional-grade Python system monitoring tool** that tracks CPU, RAM, Disk, and Network usage in real time, logs historical performance data, generates visual dashboards, triggers alerts, and produces **enterprise-style PDF health reports**.

Built to demonstrate **Operating Systems concepts, backend engineering skills, performance monitoring, logging systems, and production-level reporting** — ideal for **SDE resumes & portfolios**.

---

## 🚀 Features

* 📊 Real-time **CPU, RAM, Disk, Network monitoring**
* 🗃 Performance logging to CSV
* 📈 Historical **graphs & usage charts**
* 🚨 High-load **alert system**
* 🖥 Live **Streamlit dashboard UI**
* 📄 **Auto-generated PDF System Health Reports**
* 📋 Summary analytics & peak performance metrics
* 🧠 OS-level resource tracking using `psutil`

---

## 🛠 Tech Stack

| Category          | Tools            |
| ----------------- | ---------------- |
| Language          | Python           |
| System Monitoring | psutil           |
| Dashboard UI      | Streamlit        |
| Data Processing   | Pandas           |
| Visualization     | Matplotlib       |
| PDF Reports       | FPDF             |
| Logging           | CSV File Logging |

---

## 📁 Project Structure

```
system_resource_monitor/
│
├── monitor.py              # Collects system metrics
├── logger.py               # Logs performance data
├── alerts.py               # High-usage alert engine
├── dashboard.py            # Live UI dashboard
├── report_generator.py     # PDF report creator
├── historical_graphs.py     # Historical Graph creator
│
├── data/
│   └── system_logs.csv     # Logged system history
│
├── reports/
│   ├── health_report.pdf
│   └── usage_graph.png
│
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/System-Resource-Monitor-Performance-Logger.git
cd System-Resource-Monitor-Performance-Logger
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install psutil pandas matplotlib streamlit fpdf
```

---

## ▶ How to Run the Project

### 🔹 Start System Logging

```bash
python logger.py
```

### 🔹 Run Live Dashboard UI

```bash
streamlit run dashboard.py
```

### 🔹 Run Alert Monitor

```bash
python alerts.py
```

### 🔹 Generate PDF Health Report

```bash
python report_generator.py
```

### 🔹 Generate Historical Graph

```bash
python historical_graphs.py
```

---

## 📊 Sample Dashboard Output

* Live CPU, RAM, Disk usage
* Historical performance graphs
* Performance trend visualization

---

## 📄 Sample PDF Report Includes

* Corporate-style header
* System health summary
* Average & peak performance metrics
* Embedded usage graphs
* Tabular recent system records
* Timestamped footer

---

## 🎯 Resume Description

**System Resource Monitor & Performance Logger**
Built a real-time system monitoring tool using Python and psutil to track CPU, RAM, disk, and network usage. Implemented historical performance logging, automated alerts for high resource utilization, a live Streamlit dashboard for visualization, and professional PDF health report generation. Demonstrated strong knowledge of operating systems, backend engineering, and performance analytics.

---

## 💡 Why This Project Stands Out

* Demonstrates **OS-level system engineering**
* Real-world **performance monitoring system**
* Production-style **logging & analytics**
* Enterprise-grade **reporting & visualization**
* Strong **portfolio impact for SDE roles**

---

## 📸 Recommended Enhancements (Future Scope)

* 🧠 Process Monitor (Task Manager view)
* 📡 Email alerts for critical usage
* ☁ Cloud logging (AWS / Firebase)
* 🖥 GUI version (Tkinter / PyQt)
* 📦 Windows/Linux executable (.exe)
* 🧪 Unit testing & CI/CD pipeline

---

## 👨‍💻 Author

**Garvit Rastogi**
📌 India
🎯 Aspiring Software Development Engineer & Data Analyst

---

## ⭐ If You Like This Project

Give it a **star ⭐ on GitHub** — it helps showcase your work to recruiters!

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.
