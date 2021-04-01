from setuptools import find_packages, setup

setup (
    name='allplots',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='My first python library',
    author='fanbyprinciple',
    license='MIT',
    install_requires=['matplotlib'],
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    test_suite='test'
)