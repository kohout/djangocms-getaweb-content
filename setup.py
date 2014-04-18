import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms-getaweb-content',
    version='0.1',
    packages=['djangocms_content'],
    include_package_data=True,
    license='Unlicense',  # example license
    description='Plugin for Django CMS 3.0 that allows arranging Text and Images in a Typo3-like way.',
    long_description=README,
    url='https://github.com/kohout/djangocms-getaweb-content/',
    author='Christian Kohout',
    author_email='ck@getaweb.at',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
