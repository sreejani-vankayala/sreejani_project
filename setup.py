from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sreejani_app/__init__.py
from sreejani_app import __version__ as version

setup(
	name="sreejani_app",
	version=version,
	description="creating an app",
	author="sreejani",
	author_email="sreejanivankayala@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
