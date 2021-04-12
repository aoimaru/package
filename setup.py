
from setuptools import setup, find_packages
from os import path

# here = path.abspath(path.dirname(__file__))

with open("./README.md", mode="r") as file:
	long_description = file.read()

setup(
	name="SearchEngineForJSON",
	version="0.1.3",
	author="AoiNakamura",
	author_email="sample@example.com",
	description="SearchEngineForJSON",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aoimaru/packagingTutorial",
	packages=find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
    ],
	python_requires='>=3.7',
	)

