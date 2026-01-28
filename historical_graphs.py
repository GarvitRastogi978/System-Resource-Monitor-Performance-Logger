import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "data/system_logs.csv",
    names=["Time", "CPU", "RAM", "Disk", "Net Sent", "Net Recv"]
)

plt.figure()
plt.plot(data["CPU"], label="CPU Usage")
plt.plot(data["RAM"], label="RAM Usage")
plt.plot(data["Disk"], label="Disk Usage")

plt.legend()
plt.title("System Usage History")
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.show()
