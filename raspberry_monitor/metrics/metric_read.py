import os
import re


def get():
    return {
        "memory": get_memory(),
        "temperature": get_temperature()
    }


def get_memory():
    stream = os.popen("free")
    output = stream.read().split("\n")
    memory_line = output[1][4:-1]
    memory_line = re.sub(r"\s+", " ", memory_line)
    memory = memory_line.split(" ")[1:]
    total, used, free = int(memory[0]), int(memory[1]), int(memory[2])
    return {
        "total": total,
        "used": used,
        "free": free,
        "total_in_gb": total / 1e+6,
        "used_in_gb": used / 1e+6,
        "free_in_gb": free / 1e+6,
    }


def get_temperature():
    stream = os.popen("cat /sys/class/thermal/thermal_zone0/temp")
    output = int(stream.read())
    return {"value": output / 1000, "unit": "Celsius"}
