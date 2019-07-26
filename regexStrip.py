#! /usr/bin/env python3
# regexStrip.py - Regex version of the strip method
import re


def regexStrip(text, toRemove=' '):
  if toRemove == ' ':
    leadingRegex = re.compile(r'^\s*')
    trailingRegex = re.compile(r'\s*$')
    leadingTrimmed = leadingRegex.sub('', text)
    result = trailingRegex.sub('', leadingTrimmed)
    print(result)
  else:
    regex = re.compile(r'%s' %toRemove)
    result = regex.sub('', text)
    print(result)
    


regexStrip('    test    ')
regexStrip('abctestabc', 'abc')
