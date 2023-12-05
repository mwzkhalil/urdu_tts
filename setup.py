# setup.py
from setuptools import setup, find_packages

setup(
    name='urdu-tts',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'transformers',
    ],
)
