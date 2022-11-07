import psutil as ps
import time
from datetime import datetime
import requests
import json
import subprocess

url = "https://api.powerbi.com/beta/0aa66ad4-f98f-4515-b7c9-b60fd37ad027/datasets/4fdcc3fe-dd5f-4026-a97e-640fd091a794/rows?refreshAccessToken=true&key=rnhHNVSMr2wbncfYEIPoQsjNZo9v6yl4F0V2xrgFvPSOFR%2Fg7IQXA39G7F5OYlK6Y02CYA6YV0F5txRfPNKmpw%3D%3D"

while True:
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
    result = str(subprocess.Popen('nvidia-smi',
                                  cwd=r'C:\Windows\System32\DriverStore\FileRepository\nvaci.inf_amd64_017f799b1b210f75',
                                  stdout=subprocess.PIPE, shell=True).communicate())
    data = [{
        "datetime_value": now,
        "cpu_load": ps.cpu_percent(),
        "ram_load": ps.virtual_memory().used / 1024 / 1024,
        "battery_percentage": ps.sensors_battery()[0],
        "diskC": ps.disk_usage("C:")[3],
        "diskD": ps.disk_usage("D:")[3],
        "upTime": datetime.fromtimestamp(ps.boot_time()).strftime("%Y-%m-%dT%H:%M:%S%Z"),
        "gpu_load": int(result.split("%")[0].split("|")[24].replace(" ", "")),
        "gpu_temperature": int(result.split("C")[7].split("N/A")[2]),
        "gpu_used_memory": int(result.split("MiB")[0].split("|")[23])
    }]

    headers = {"Content-Type" : "application/json"}

    response = requests.post(
        url,
        data=json.dumps(data)
    )
    time.sleep(5)
