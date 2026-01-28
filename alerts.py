from monitor import get_system_stats

CPU_LIMIT = 85
RAM_LIMIT = 85

def check_alerts():
    stats = get_system_stats()

    if stats["cpu"] > CPU_LIMIT:
        print("⚠ ALERT: High CPU Usage!")

    if stats["ram"] > RAM_LIMIT:
        print("⚠ ALERT: High RAM Usage!")

if __name__ == "__main__":
    while True:
        check_alerts()
