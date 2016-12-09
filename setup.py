from setuptools import setup, find_packages

setup(
    name='sparkgeo-devtools',
    version='0.0.1',
    install_requires=[
        'Click',
        'fabric',
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        sparkgeo=sparkgeo.main:cli
    '''

)
