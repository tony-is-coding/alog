import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.rst')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

testing_extras = [
    'pytest',
    'coverage',
    'pytest-cov',
]

docs_extras = [
    'Sphinx >= 1.3.1',
]

setup(
    name='alog',
    version='0.9.6',
    description='Python logging for Humans',
    long_description='',
    url='https://github.org/keitheis/alog',
    author='Keith Yang',
    author_email='yang@keitheis.org',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Logging',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='simple basic application logging',
    packages=['alog'],
    package_data={'': ['LICENSE']},
    zip_safe=False,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
    },
)
