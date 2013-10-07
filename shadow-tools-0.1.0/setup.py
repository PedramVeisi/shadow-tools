#!/usr/bin/env python

from distutils.core import setup

setup(name='ShadowTools',
      version='0.1.0dev',
      description='A simple app for changing and restoring passwords in /etc/shadow',
      long_description=open('README.txt').read(),
      license='GPLv3',
      author='Pedram Veisi',
      author_email='pedramveisi@gmail.com',
      packages=['shadow-tools'],
     )

