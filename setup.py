#!/usr/bin/env python
# coding: utf-8

import sys

import setuptools

PACKAGE_NAME = 'pycsvsql'
MINIMUM_PYTHON_VERSION = '3.6'


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {0}+ is required.".format(MINIMUM_PYTHON_VERSION))


def build_description():
    """Build a description for the project from documentation files."""
    readme = open("README.md").read()
    return readme


check_python_version()

setuptools.setup(
    name='pycsvsql',
    version='0.0.1',
    description="Python csvsql convertor.",
    url='https://github.com/gzxultra/pycsvsql',
    author='Zhixiang Gu',
    author_email='mygladfinger@gmail.com',

    packages=setuptools.find_packages(),

    long_description=build_description(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=[
        "click ~= 6.0",
        "peewee ~= 3.3.1",
    ]
)
