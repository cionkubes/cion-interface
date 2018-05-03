from setuptools import setup, find_packages
setup(
    name="cion_interface",
    version="1.0.0",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        'workq'
    ],
    dependency_links=[
        'git+https://github.com/cionkubes/workq'
    ]
)
