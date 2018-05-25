from setuptools import setup, find_packages

setup(
    name='op_stats',
    version='0.1.0',
    packages=['op_stats'],    
    install_requires=[
        'flask',
        'psutil'
    ]
)
