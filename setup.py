#!/usr/bin/env python

from setuptools import setup

setup(name='friday-notifier',
      version='0.4',
      description='Sends text messages using the Twilio SMS API on fridays',
      author='Michael Cullen',
      author_email='michael@michaelcullen.name',
      url='https://github.com/mich181189/friday-notifier',
      scripts=['friday-notifier'],
      install_requires=['twilio'],
     )