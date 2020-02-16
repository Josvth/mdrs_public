from setuptools import setup, find_packages

setup(
    name='mdrs_simulator',
    version='',
    url='',
    license='',
    author='Jos van t Hof',
    author_email='josvth@gmail.com',
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
        'main': ["mdrs_simulator=mmWaveISL.main:main"]}
)
