#! /usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def spam():
  bacon()
def bacon():
  raise Exception('This is the error message.')

spam()