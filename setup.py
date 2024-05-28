"""
Setup script for aiodatabase package.
"""

from setuptools import setup, find_packages

setup(
    name="aiodatabase",
    version="0.1.7",
    install_requires=["PyYAML", "aiomysql", "aiosqlite"],
    packages=find_packages(),
    package_data={
        "": ["resources/sqlite.sql", "resources/config.yml"],
    },
    include_package_data=True,
    description="AioDatabase is a simple database abstraction layer for SQLite and MySQL.",
    author="AmitxD",
    url="https://github.com/Amitminer/AioDatabase",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
