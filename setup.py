import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-shannon",
    version="0.0.1",
    author="Ori Roza",
    author_email="ori75660@gmail.com",
    description="a package for arithmetic coding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="package URL",
    project_urls={
        "Bug Tracker": "package issues URL",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "shannon"},
    packages=setuptools.find_packages(where="shannon"),
    python_requires=">=3.6",
    package_requires=["pytest==7.1.2"]
)
