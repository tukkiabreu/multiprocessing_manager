from setuptools import setup, find_packages

import multiprocessing_manager

setup(
    name='multiprocessing_manager',
    version=multiprocessing_manager.__version__,
    packages=find_packages(),
    include_package_data=True
)
