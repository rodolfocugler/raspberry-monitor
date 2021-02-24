import os
import re


def get():
    return {
        "memory": get_memory(),
        "disk": get_disk(),
        "temperature": get_temperature(),

    }


def get_memory():
    stream = os.popen("free")
    output = stream.read().split("\n")
    memory_line = output[1][4:-1]
    memory_line = re.sub(r"\s+", " ", memory_line)
    memory = memory_line.split(" ")[1:]
    total, used, free = int(memory[0]), int(memory[1]), int(memory[2])
    return calculate_total_used_free(total, used, free)


def get_temperature():
    stream = os.popen("cat /sys/class/thermal/thermal_zone0/temp")
    output = int(stream.read())
    return {"value": output / 1000, "unit": "Celsius"}


def get_disk():
    stream = os.popen("df -a")
    output = stream.read().split("\n")
    output = list(filter(lambda x: "/dev/mmcblk0p2" in x, output))[0][16:]
    output = re.sub(r"\s+", " ", output)
    output = output.split(" ")
    total, used, free = int(output[0]), int(output[1]), int(output[2])
    return calculate_total_used_free(total, used, free)


def calculate_total_used_free(total, used, free):
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
