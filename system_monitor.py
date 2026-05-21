import time
import psutil

def check_system_health():
    print("Starting System Health Monitor...")
    print("To stop monitoring, press Ctrl + C\n")
    print("--------------------------------------------------")
    print("CPU Usage | RAM Usage | Disk Usage | Status")
    print("--------------------------------------------------")

    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            if cpu > 80 or ram > 80:
                status = "HIGH LOAD!"
            elif cpu > 50 or ram > 50:
                status = "WARNING"
            else:
                status = "HEALTHY"

            print(f"{cpu}%       | {ram}%       | {disk}%        | {status}")
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped successfully.")

if __name__ == "__main__":
    check_system_health()
