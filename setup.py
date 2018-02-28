import re

from setuptools import setup, find_packages

with open('daiquiri_client/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name='django-daiquiri-client',
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    url='https://github.com/aipescience/django-daiquiri-client',
    description=u'Daiquiri Client is a python library meant to be used with the Daiquiri Framework.',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests>=2.18.4',
        'simplejson>= 3.11.1',
    ],
    classifiers=[],
    packages=find_packages(),
    include_package_data=True
)
