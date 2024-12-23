import os

from setuptools import setup, find_packages

script_dir = os.path.dirname(os.path.abspath(__file__))
version_file_path = os.path.join(script_dir, "version")
with open(version_file_path, "r") as f:
    __version__ = f.read()

setup(
    name="Stayforge Python SDK",
    version=__version__,
    description="Stayforge Python SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TokujunSystems",
    author_email="support@stayforge.io",
    url="https://github.com/tokujun-t/stayforge-python",
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'typing_extensions',
        'urllib3',
        'python-dateutil',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: NoLicense",
    ],
    python_requires=">=3.12",
)
