#! /usr/bin/env python3
# strongPassword.py - A program to check a string against preset 
#                     password strength conditions

import re

# A strong password is defined as one that is at least eight characters long, 
# contains both uppercase and lowercase characters, and has at least one digit.

def verifyStrongPassword(password):
  if len(password) < 8:
    print('Password is not secure.')

  mo1 = re.compile(r'[a-z]').search(password)
  mo2 = re.compile(r'[A-Z]').search(password)
  mo3 = re.compile(r'\d').search(password)

  if mo1 and mo2 and mo3:
    print('The password is secure.')
  else:
    print('The password is NOT secure.')

verifyStrongPassword('1234') # false
verifyStrongPassword('12345678') # false
verifyStrongPassword('1234asdf') # false
verifyStrongPassword('123ABCab') # true
