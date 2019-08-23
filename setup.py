#!/usr/bin/env python
# -*- coding: utf-8

import os

from setuptools import setup, find_packages

GENERIC_REQ = [
    "six==1.12.0",
    "requests==2.22.0",
    "pyrfc3339==1.1",
    "cachetools==3.1.1",
]

CODE_QUALITY_REQ = [
    'prospector',
]

TESTS_REQ = [
    'tox==3.13.2',
    'mock==3.0.5',
    "pytest-sugar==0.9.2",
    "pytest-html==1.22.0",
    "pytest-cov==2.7.1",
    "pytest-helpers-namespace==2019.1.8",
    'pytest==3.10.1',
    "GitPython==2.1.14",
]

# These are not direct dependencies, but we need to lock down their versions here
EXTRA_REQ = [
    # "pluggy==0.12.0",
    # "prospector==1.9.0",
]


def _generate_description():
    description = [_read("README.rst")]
    changelog_file = os.getenv("CHANGELOG_FILE")
    if changelog_file:
        description.append(_read(changelog_file))
    return "\n".join(description)


def _get_license_name():
    with open(os.path.join(os.path.dirname(__file__), "LICENSE")) as f:
        for line in f:
            if line.strip():
                return line.strip()


def _read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


def main():
    setup(
        name="k8s",
        author="FiaaS developers",
        author_email="fiaas@googlegroups.com",
        use_scm_version=True,
        packages=find_packages(exclude=("tests",)),
        zip_safe=True,
        include_package_data=True,

        # Requirements
        install_requires=GENERIC_REQ,
        setup_requires=['pytest-runner', 'wheel', 'setuptools_scm'],
        extras_require={
            "dev": TESTS_REQ + CODE_QUALITY_REQ + EXTRA_REQ,
            "codacy": ["codacy-coverage"],
            "release": ["gitpython", "twine"],
            "docs": ["Sphinx>=1.6.3"]
        },
        tests_require=TESTS_REQ,
        # Metadata
        description="Python client library for the Kubernetes API",
        long_description=_generate_description(),
        url="https://github.com/fiaas/k8s",
        license=_get_license_name(),
        keywords="kubernetes fiaas",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Clustering",
            "Topic :: System :: Distributed Computing",
        ]
    )


if __name__ == "__main__":
    main()
