from setuptools import setup, find_packages

setup(
    name="fmLib",
    version="1.0.0",
    author="Nic Gunter",
    description="A wrapper for assorted file handling functions.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.10',
    install_requires=[]
)