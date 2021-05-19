from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ts2pi',
    packages=find_packages(include=['ts2pi']),
    version='0.1.2',
    description='Python module to transform a time series into a persistence image representation',
    author='Clement Piat',
    url="https://github.com/clementpiat/time-series-persistence-image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'numpy==1.20.3',
        'gudhi==3.4.1',
        'sklearn==0.0'
    ]
)
