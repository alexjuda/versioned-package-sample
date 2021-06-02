import os
import setuptools


def _this_path():
    return os.path.abspath(os.path.dirname(__file__))


def _read_readme():
    with open(os.path.join(_this_path(), "README.md")) as f:
        return f.read()


def _read_version():
    with open(os.path.join(_this_path(), "VERSION")) as f:
        return f.read().strip()


setuptools.setup(
    name="versioned-package-sample",
    version=_read_version(),
    # author="Alexander Juda",
    # author_email="alexanderjuda@gmail.com",
    packages=setuptools.find_packages(
        include=["sample", "sample.*"],
        where="src",
    ),
    package_dir={"": "src"},
    install_requires=[
        # Add prod deps here
    ],
    extras_require={
        "dev": [
            # Add optional dev deps here
            "pytest",
        ],
    },
)
