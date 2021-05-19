from setuptools import find_packages, setup

setup(
    name='ts2pi',
    packages=find_packages(include=['ts2pi']),
    version='0.1.0',
    description='Python module to transform a time series into a persistence image representation',
    author='Clement Piat',
    license='MIT',
    install_requires=[
        'numpy==1.20.3',
        'gudhi==3.4.1',
        'sklearn==0.0'
    ]
)
