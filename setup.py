from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="twitter-analytics",
    version="1.0.0",
    author="Mohammad Amin Dadgar, TogetherCrew",
    maintainer="Mohammad Amin Dadgar",
    maintainer_email="dadgaramin96@gmail.com",
    packages=find_packages(),
    description="Twitter Analytics jobs of TogetherCrew.",
    long_description=open("README.md").read(),
    install_requires=requirements,
)
