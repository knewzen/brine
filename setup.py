""" setup.py

    Basic setup file to enable pip install

    http://python-distribute.org/distribute_setup.py

    python setup.py register -r pypi sdist upload -r pypi

    More secure to use twine to upload  $ pip3 install twine
$ python3 setup.py sdist
$ twine upload dist/brining-0.2.7.tar.gz
"""
from setuptools import setup, find_packages

setup(  name='brining',
        version='0.2.7',
        description='Python object to/from JSON serialization/deserialization module',
        url='https://github.com/SmithSamuelM/brine',
        author='Samuel M Smith',
        author_email='smith.samuel.m@gmail.com',
        install_requires = ['simplejson'],
        packages = find_packages(exclude=[]),
        package_data={'': ['*.txt',  '*.ico',  '*.json', '*.md', '*.conf']},
        tests_require = ['nose'],
        test_suite = 'nose.collector',
        license="MIT",
        keywords='Python object JSON serialization'
      )
