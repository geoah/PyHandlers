# -*- coding: utf-8 -*-
"""Setup for Pericles Handlers.

Copyright 2014 University of Liverpool

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import inspect
import os

import handlers

# Import Setuptools
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

# Import our own module here for version number
#from alloy2.setup.commands import develop, install, unavailable

# Inspect to find current path
setuppath = inspect.getfile(inspect.currentframe())
setupdir = os.path.dirname(setuppath)

# Find longer description from README
with open(os.path.join(setupdir, 'README.rst'), 'r') as fh:
    _long_description = fh.read()

# Requirements
with open(os.path.join(setupdir, 'requirements.txt'), 'r') as fh:
    _install_requires = fh.readlines()


setup(
    name='PyHandlers',
    version=handlers.__version__,
    description='PyHandlers',
    packages=find_packages(),
    install_requires=_install_requires,
    long_description=_long_description,
    author='Jérôme Fuselier',
    maintainer_email='jerome.fuselier@free.fr',
    license="Apache License, Version 2.0",
    url='https://github.com/kaldrill/PyHandlers',
    setup_requires=['setuptools-git'],
    entry_points={
        'console_scripts': [
            "handler-serve = handlers.server:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
    ],
#    cmdclass = {
#        'bdist_egg': unavailable,
#        'bdist_rpm': unavailable,
#        'bdist_wininst': unavailable,
#        'develop': unavailable,
#        'install': install,
#    },
)
