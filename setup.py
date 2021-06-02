import setuptools


setuptools.setup(
    name="versioned-package-sample",
    version="0.1.0",
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
