
import setuptools

with open("./README.md", mode="r") as file:
	long_description = file.read()

setuptools.setup(
	name="SearchEngineForJSON",
	version="0.0.2",
	entry_points={
		"console_script": [
			"hello=jsonSearch:main"
		]
	},
	author="AoiNakamura",
	author_email="sample@example.com",
	description="SearchEngineForJSON",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aoimaru/packagingTutorial",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
    ],
	python_requires='>=3.7',
	)

