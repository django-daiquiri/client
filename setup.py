from setuptools import setup, find_packages

version = '0.1.0'

author = 'Jochen Klar'
email = 'jklar@aip.de'

setup(
    name='django-daiquiri-client',
    version=version,
    author=author,
    author_email=email,
    maintainer=author,
    maintainer_email=email,
    license='Apache-2.0',
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
