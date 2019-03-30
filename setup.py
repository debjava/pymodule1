'''
Created on Mar 30, 2019

@author: PIKU
'''
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'pymodule1'
DESCRIPTION = 'My short description for my project.'
URL = 'https://github.com/debjava/pymodule1'
EMAIL = 'deba.java@gmail.com'
AUTHOR = 'Debadatta Mishra'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '1.0'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description='long_description',
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=['peppercorn'],
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
#     install_requires=REQUIRED,
#     extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    # $ setup.py publish support.
#     cmdclass={
#         'upload': UploadCommand,
#     },
    )
