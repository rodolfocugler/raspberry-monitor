import subprocess


def shutdown():
    subprocess.Popen(["sudo", "shutdown", "-h", "0"])


def restart():
    subprocess.Popen(["sudo", "shutdown", "-r", "0"])
