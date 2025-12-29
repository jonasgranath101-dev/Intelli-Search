# setup.py

from setuptools import setup, find_packages


setup(
    name="intellisearch",
    version="v0.1.0",
    packages=find_packages(),
    package_data={"Intelli": ["src/mod/default.h"]},  # Include header file
    include_package_data=True,
    description="A lambda search engine for python.",
    url="https://intellisearch-gv0j.onrender.com/",
    # cffi_modules tells setuptools to run the specified build script
    # to compile the C extension.
    cffi_modules=["intellisearch/build.py:ffibuilder"],
    # You need cffi as a build-time dependency
    setup_requires=["cffi>=1.0.0"],
    # And also as an install-time dependency for the user
    install_requires=["cffi>=1.0.0"],
    author="Jonas Granath",
    license="GPL-3.0",
    zip_safe=False,  # Generally good practice for packages with C extensions
)
