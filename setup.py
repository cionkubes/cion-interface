from setuptools import setup, find_packages
setup(
    name="cion_interface",
    version="0.1",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        'workq'
    ],
    dependency_links=[
        'git+https://github.com/cionkubes/workq'
    ]
)
