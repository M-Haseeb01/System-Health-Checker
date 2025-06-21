import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(f"Disk Free: {int(free)}%")
    return free > 20

def check_cpu_usage():
    p = psutil.cpu_percent(1)
    print(f"CPU being used: {int(p)}%")
    return p < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!!!!!!")
else:
    print("Everything is fine")
