import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PacaPy-raul-guajardo",
    version="0.0.1",
    author="Raul Guajardo",
    author_email="rguajardo95@gmail.com",
    description="A package designed as a wrapper over Alpaca API for my general use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raulguajardo/PacaPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)