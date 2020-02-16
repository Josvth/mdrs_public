from setuptools import setup, find_packages

setup(
    name='mdrs',
    version='',
    url='',
    license='',
    author='Jos',
    author_email='',
    description='',
    packages=find_packages(),
    install_requires=['numpy',
                      'poliastro',
                      'scipy',
                      'astropy',
                      'mayavi',
                      'PyQt5',
                      'numba'],
    entry_points={
        'main': ["mmWaveISL=mmWaveISL.main:main"]}
)
