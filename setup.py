#!/usr/bin/env python

from setuptools import setup, find_packages

requires=['numpy', 'sympy', 'pylatex']

NME = 'MathsMonkey'
VER = '0.1'
EML = 'iztok.kucan@gmail.com'
WEB = 'https://github.com/ikucan/MathsMonkey'
AUT = 'iztok kucan'
DSC = 'A maths practice system.'

setup(name         = NME,
      version      = VER,
      description  = DSC,
      author       = AUT,
      author_email = EML,
      url          = WEB,
      packages     = find_packages()
     )
