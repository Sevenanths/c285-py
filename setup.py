from setuptools import setup, find_packages

setup(
    name="c285-py",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="anthe.studio",
    author_email="c285-py@anthe.studio",
    description="Python interface for the AVerMedia Game Capture HD II (C285) RESTful web interface",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sevenanths/c285-py",
    python_requires='>=3',
)