from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["Greenlet", "RestrictedPython", ]

setup(
    name="ccpy",
    version="1",
    author="Morgan Metz",
    author_email="mlmi4@k12albemarle.org",
    description="A package to convert computercraft to python!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Morgandri1/Python-CC/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)