from setuptools import find_packages, setup
from dbx_local_test import __version__

setup(
    name="dbx_local_test",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
