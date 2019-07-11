# Upload package to PyPi.

from setuptools import setup

setup(name='yalegatewayservicemetrics',
      version='0.1.4',
      description='Library for fetching data from the Yale GatewaySericeMetrics API.',
      url='https://github.com/ErikBoesen/yalegatewayservicemetrics',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='GPL',
      packages=['yalegatewayservicemetrics'],
      install_requires=['requests'])
