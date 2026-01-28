from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load data
data = pd.read_csv("data/system_logs.csv",
                   names=["Time", "CPU", "RAM", "Disk", "Net Sent", "Net Recv"])

# Compute stats
avg_cpu = data["CPU"].mean()
avg_ram = data["RAM"].mean()
avg_disk = data["Disk"].mean()

max_cpu = data["CPU"].max()
max_ram = data["RAM"].max()
max_disk = data["Disk"].max()

# Health score logic
def health_status(value):
    if value < 60:
        return "GOOD"
    elif value < 85:
        return "MODERATE"
    return "CRITICAL"

cpu_status = health_status(avg_cpu)
ram_status = health_status(avg_ram)
disk_status = health_status(avg_disk)

# Generate graph image
plt.figure(figsize=(8, 4))
plt.plot(data["CPU"], label="CPU Usage")
plt.plot(data["RAM"], label="RAM Usage")
plt.plot(data["Disk"], label="Disk Usage")
plt.title("System Usage Over Time")
plt.legend()
plt.savefig("reports/usage_graph.png")
plt.close()

# PDF Class
class PDF(FPDF):
    def header(self):
        self.set_fill_color(30, 30, 30)
        self.rect(0, 0, 210, 25, "F")
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", "B", 16)
        self.cell(0, 15, "SYSTEM HEALTH REPORT", ln=True, align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_text_color(120, 120, 120)
        self.set_font("Arial", size=9)
        self.cell(0, 10, f"Generated on {datetime.now()}", align="C")

# Create PDF
pdf = PDF()
pdf.add_page()

# Reset text color
pdf.set_text_color(0, 0, 0)

# Section Title
def section_title(title):
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 10, title, ln=True, fill=True)
    pdf.ln(2)

# Summary Section
section_title("System Summary")

pdf.set_font("Arial", size=11)
pdf.cell(0, 8, f"Average CPU Usage: {avg_cpu:.2f}% ({cpu_status})", ln=True)
pdf.cell(0, 8, f"Average RAM Usage: {avg_ram:.2f}% ({ram_status})", ln=True)
pdf.cell(0, 8, f"Average Disk Usage: {avg_disk:.2f}% ({disk_status})", ln=True)

pdf.ln(4)

# Max Usage Section
section_title("Peak Performance Metrics")

pdf.cell(0, 8, f"Highest CPU Recorded: {max_cpu:.2f}%", ln=True)
pdf.cell(0, 8, f"Highest RAM Recorded: {max_ram:.2f}%", ln=True)
pdf.cell(0, 8, f"Highest Disk Recorded: {max_disk:.2f}%", ln=True)

pdf.ln(4)

# Health Score Section
section_title("System Health Rating")

pdf.set_font("Arial", "B", 14)
pdf.set_text_color(0, 102, 0 if cpu_status == "GOOD" else 150)
pdf.cell(0, 12, f"Overall Health: {cpu_status}", ln=True)

pdf.set_text_color(0, 0, 0)
pdf.ln(4)

# Chart Section
section_title("Usage Trends Graph")

pdf.image("reports/usage_graph.png", x=15, w=180)
pdf.ln(5)

# Table Section
section_title("Recent Usage Records")

pdf.set_font("Arial", "B", 10)
pdf.cell(40, 8, "Time", border=1)
pdf.cell(25, 8, "CPU", border=1)
pdf.cell(25, 8, "RAM", border=1)
pdf.cell(25, 8, "Disk", border=1)
pdf.ln()

pdf.set_font("Arial", size=9)

for _, row in data.tail(12).iterrows():
    pdf.cell(40, 8, str(row["Time"]), border=1)
    pdf.cell(25, 8, f"{row['CPU']:.1f}%", border=1)
    pdf.cell(25, 8, f"{row['RAM']:.1f}%", border=1)
    pdf.cell(25, 8, f"{row['Disk']:.1f}%", border=1)
    pdf.ln()

# Save PDF
output_path = "reports/health_report.pdf"
pdf.output(output_path)

print(f"✅ Professional PDF Report Generated: {output_path}")
