import os
import re
import json
from pathlib import Path

from raspberry_monitor import config

conf = config.Config()


def get():
    metrics = {
        "memory": get_memory(),
        "disk": get_disk(),
        "temperature": get_temperature(),
        "cpu": get_cpu(),
        "network": get_network()
    }

    if conf.BACKUP_PATH is not None:
        metrics["backups"] = get_backups()
    return metrics


def get_memory():
    stream = os.popen("free")
    output = stream.read().split("\n")
    memory_line = output[1][4:-1]
    memory_line = re.sub(r"\s+", " ", memory_line)
    memory = memory_line.split(" ")[1:]
    total, used, free = int(memory[0]), int(memory[1]), int(memory[2])
    return calculate_total_used_free_memory(total, used, free)


def get_temperature():
    stream = os.popen("cat /sys/class/thermal/thermal_zone0/temp")
    output = int(stream.read())
    return {"value": output / 1000, "unit": "Celsius"}


def get_disk():
    stream = os.popen("df /host/ -a")
    output = stream.read().split("\n")
    output = list(filter(lambda x: "/dev/mmcblk0p2" in x, output))[0][15:]
    output = re.sub(r"\s+", " ", output.strip())
    output = output.split(" ")
    total, used, free = int(output[0]), int(output[1]), int(output[2])
    return calculate_total_used_free_memory(total, used, free)


def get_backups():
    backups = []
    for path in sorted(Path(conf.BACKUP_PATH).iterdir(), key=os.path.getmtime):
        user_path = f"{conf.BACKUP_PATH}/{path.name}/localhost/home"
        for user in os.listdir(user_path):
            folders = os.listdir(f"{user_path}/{user}")
            if len(folders) > 0:
                backups.append(path.name)

    return backups


def get_cpu():
    stream = os.popen("mpstat -o JSON")
    output = json.loads(stream.read())
    return output["sysstat"]["hosts"][0]["statistics"][0]["cpu-load"][0]


def get_network():
    return {
        "eth0": get_network_interface("eth0"),
        "wlan0": get_network_interface("wlan0")
    }


def get_network_interface(interface):
    stream = os.popen(f"bmon -r 2 -o 'ascii:quitafter=2' -p {interface}")
    output = stream.read().split("\n")[3]
    output = re.sub(r"\s+", " ", output).split(" ")
    rx, tx = int(re.sub(r"\D", "", output[2])), int(re.sub(r"\D", "", output[4]))
    rx_unit, tx_unit = re.sub(r"\d", "", output[2]), re.sub(r"\d", "", output[4])
    return {"rx": rx, "rx_unit": rx_unit, "tx": tx, "tx_unit": tx_unit}


def calculate_total_used_free_memory(total, used, free):
    return {
        "total": total,
        "used": used,
        "free": free,
        "used (%)": (used / total) * 100,
        "free (%)": 100 - ((used / total) * 100),
        "total_in_gb": total / 1e+6,
        "used_in_gb": used / 1e+6,
        "free_in_gb": free / 1e+6,
    }


def calculate_total_used_free(total, used, free):
    return {
        "total": total,
        "used": used,
        "free": free,
        "used (%)": (used / total) * 100,
        "free (%)": 100 - ((used / total) * 100)
    }
