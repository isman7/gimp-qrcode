from pathlib import Path
from setuptools import setup
from setuptools import find_packages

requirements = Path("requirements.txt").read_text().split("\n")
readme = Path("README.md").read_text()

setup(
    name='gimp-qrcode',
    version='0.1.0',
    packages=find_packages(exclude="gimp2"),
    url='https://github.com/isman7/gimp-python-development/',
    license='GNU GPLv3',
    author='ibenito',
    author_email='ismaelbenito@protonmail.com',
    description='Create QR Codes inside GIMP 3.',
    install_requires=requirements,
    package_data={"gimp.plugins.qrcode": ["qrcode"]},
    long_description=readme,
    long_description_content_type='text/markdown',
)
