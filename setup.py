#!/usr/bin/env python

from setuptools import setup, find_packages

requires=['numpy', 'sympy', 'pylatex']

NME = 'MathsMonkey'
VER = '0.1'
EML = 'iztok.kucan@gmail.com'
WEB = 'https://github.com/ikucan/MathsMonkey'

setup(name         = NME,
      version      = VER,
      description  = 'A repetitive maths practice system.',
      author       = 'Iztok Kucan',
      author_email = EML,
      url          = WEB,
      packages     = find_packages()
     )
