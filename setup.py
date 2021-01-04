import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pathsolver", # Replace with your own username
    version="1.0.1",
    author="Athul Mathew Konoor",
    author_email="athulmathewkonoor@gmail.com",
    description="A package to solve maze problem using A-star Algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toshihiroryuu/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)