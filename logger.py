import csv
import time
from monitor import get_system_stats

LOG_FILE = "data/system_logs.csv"

def log_stats():
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        while True:
            stats = get_system_stats()
            row = [time.strftime("%Y-%m-%d %H:%M:%S"),
                   stats["cpu"], stats["ram"], stats["disk"],
                   stats["network_sent"], stats["network_recv"]]

            writer.writerow(row)
            file.flush()
            time.sleep(5)

if __name__ == "__main__":
    log_stats()
