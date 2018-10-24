"""Clean code
"""

import versioneer

import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


PACKAGE_NAME = "clean-code"
AUTHOR = "Coding Yarns"
EMAIL = "zebedee.nicholls@climate-energy-college.org"
URL = "https://github.com/codingyarns/clean-code"

DESCRIPTION = (
    "Package for documenting our experiences and code snippets from learning to code"
)
README = "README.rst"

SOURCE_DIR = "src"

with open(README, "r") as readme_file:
    README_TEXT = readme_file.read()


class CleanCode(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        pytest.main(self.test_args)


cmdclass = versioneer.get_cmdclass()
cmdclass.update({"test": CleanCode})

setup(
    name=PACKAGE_NAME,
    version=versioneer.get_version(),
    description=DESCRIPTION,
    long_description=README_TEXT,
    long_description_content_type="text/x-rst",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license="CC0 1.0",
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "learning",
        "coding",
        "sharing",
    ],
    packages=find_packages(SOURCE_DIR),  # no tests/docs in `src` so don't need exclude
    package_dir={"": SOURCE_DIR},
    # package_data={
    #     "": ["*.csv"],
    #     "pymagicc": [
    #         "MAGICC6/*.txt",
    #         "MAGICC6/out/.gitkeep",
    #         "MAGICC6/run/*.CFG",
    #         "MAGICC6/run/*.exe",
    #         "MAGICC6/run/*.IN",
    #         "MAGICC6/run/*.MON",
    #         "MAGICC6/run/*.prn",
    #         "MAGICC6/run/*.SCEN",
    #     ],
    # },
    # include_package_data=True,
    # install_requires=["pandas", "f90nml"],
    # tests_require=["pytest"],
    cmdclass=cmdclass,
)
