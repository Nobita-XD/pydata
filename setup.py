import pathlib
import setuptools


def read(file: str) -> list:
    with open(file, encoding="utf-8") as r:
        return [i.strip() for i in r]


file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setuptools.setup(
    name="youtube_data",
    version="1.0.0",
    author="MrAbhiX",
    author_email="mrabhixd103@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    description="Python library Get YouTube Video Data",
    license="MIT",
    url="https://github.com/MrAbhiX/pydata",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires = read(""),
    python_requires=">=3.6"
)
