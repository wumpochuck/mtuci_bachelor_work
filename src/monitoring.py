import psutil
import time

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} |CPU Usage: {cpu_percent}% | Memory Usage: {memory.percent}% | Memory Available: {memory.available / (1024**3):.2f} GB")
    
    time.sleep(1)