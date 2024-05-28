"""
Setup script for aiodatabase package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aiodatabase",
    version="1.0.0",
    license="MIT",
    install_requires=["PyYAML", "aiomysql", "aiosqlite"],
    packages=find_packages(),
    package_data={
        "": ["resources/sqlite.sql", "resources/config.yml"],
    },
    include_package_data=True,
    description="AioDatabase is a simple database abstraction layer for SQLite and MySQL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AmitxD",
    url="https://github.com/Amitminer/AioDatabase",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
