from setuptools import setup

setup(
    name='sparkgeo',
    version='0.0.1',
    install_requires=[
        'Click',

    ],
    packages=['sparkgeo'],
    entry_points='''
        [console_scripts]
        sparkgeo=sparkgeo.main:cli
    '''

)
