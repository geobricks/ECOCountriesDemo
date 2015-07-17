from setuptools import setup
from setuptools import find_packages

setup(
    name='ECOCountriesDemo',
    version='0.1.0',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Data acquisition for the ECO Countries demo.',
    install_requires=[
        'GeobricksCommon',
        'GeobricksMODIS',
        'GeobricksDownloader',
        'GeobricksProcessing-cors'
    ],
    url='http://pypi.python.org/pypi/ECOCountriesDemo/'
)
