#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/synthesizer.svg
        :target: https://pypi.python.org/pypi/synthesizer
.. image:: https://img.shields.io/travis/priyanshum17/synthesizer.svg
        :target: https://travis-ci.org/priyanshum17/synthesizer

Information


Links:
---------
* `Github <https://github.com/priyanshum17/synthesizer>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Priyanshu Mehta",
    author_email='pmehta305@gatech.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Information",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='synthesizer',
    name='synthesizer',
    packages=find_packages(include=['synthesizer']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/priyanshum17/synthesizer',
    version='0.1.0',
    zip_safe=False,
)
