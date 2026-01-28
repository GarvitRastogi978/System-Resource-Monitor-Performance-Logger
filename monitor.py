import psutil
import time

def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_recv": psutil.net_io_counters().bytes_recv
    }

if __name__ == "__main__":
    while True:
        stats = get_system_stats()
        print(stats)
        time.sleep(2)
