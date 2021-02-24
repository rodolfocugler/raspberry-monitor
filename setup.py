import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="raspberry_monitor",
    version="1.0.0",
    url="https://github.com/rodolfocugler/raspberry-monitor",
    license="Apache 2.0",
    maintainer="Rodolfo Cugler",
    maintainer_email="rodolfocugler@outlook.com",
    description="Rest API to monitor a Raspberry PI 4.0 (Ubuntu 64bits)",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
)