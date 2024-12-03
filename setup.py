from setuptools import setup, find_packages

setup(
    name="sortimports",
    version="1.0.0",
    author="Your Name",
    description="A Python CLI tool to sort imports according to CIA conventions.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sortimports=sortimports.cli:main",
        ],
    },
    python_requires=">=3.6",
)
