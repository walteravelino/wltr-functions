import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wltr-functions",
    version="2.9.2",
    author="Walter José Avelino da Silva",
    author_email="walter.avelin@gmail.com",
    description="WLTR Functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walteravelino/wltr-functions",
    packages=setuptools.find_packages(),
    install_requires=[
        "boto3",
        "botocore",
        "simple-salesforce",
        "email-validator",
        "psycopg2-binary",
        "cx-Oracle",
        "pymongo",
        "pycryptodomex"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
