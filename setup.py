import re
from setuptools import setup, find_packages

with open("src/CyInstaller/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name="CyInstaller",
    version=version,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "python>=3.8,<3.13",
        "click>=8.1.7",
        "cython>=3.0.10",
        "pyinstaller>=6.5.0",
        "pyyaml>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "CyInstaller=CyInstaller.__main__:build_command",
        ],
    },
)
