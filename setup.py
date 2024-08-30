import os
import re

import setuptools


def update_version_file(version: str):
    # Extract the version from the init file.
    VERSIONFILE = "fchart/__init__.py"
    with open(VERSIONFILE, "rt") as f:
        raw_content = f.read()

    content = re.sub(r"__version__ = [\"'][^']*[\"']", f'__version__ = "{version}"', raw_content)
    with open(VERSIONFILE, "wt") as f:
        f.write(content)

    def revert():
        with open(VERSIONFILE, "wt") as f:
            f.write(raw_content)

    return revert


version_str = "0.01"
revert_version_file = update_version_file(version_str)

# Configurations
with open("readme.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()


cur_dir = os.path.dirname(
    os.path.abspath(
        __file__,
    ),
)

required_packages = []
with open(os.path.join(cur_dir, "requirements.txt"), "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        else:
            package = line.strip()
            if "whl" in package:
                continue
            required_packages.append(package)
# print(required_packages)

packages = [
    *setuptools.find_packages(),
]

try:
    setuptools.setup(
        install_requires=required_packages,  # Dependencies
        extras_require={},
        # Minimum Python version
        python_requires=">=3.10",
        name="fchart",  # Package name
        version=version_str,  # Version
        author="zhangdazhi",  # Author name
        author_email="zdzwsz@126.com",  # Author mail
        description="Python package fchart",  # Short package description
        # Long package description
        long_description=long_description,
        long_description_content_type="text/markdown",
        # Searches throughout all dirs for files to include
        packages=packages,
        # Must be true to include files depicted in MANIFEST.in
        # include_package_data=True,
        license_files=["LICENSE"],  # License file
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
    )
finally:
    revert_version_file()
