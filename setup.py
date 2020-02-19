import codecs
import os
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    print(version_file)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dpayocr",
    version=find_version("src", "dpayocr", "__init__.py"),
    description="识别支付宝微信收款码信息",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dust8/dpayocr",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["pillow", "pytesseract", "pyzbar"],
    scripts=["src/dpayocr/payqrcode.py"],
    entry_points={"console_scripts": ["dpayocr=payqrcode:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
