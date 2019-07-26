#! /usr/bin/env python3
# Write a program that opens all .txt files in a folder and searches 
# for any line that matches a user-supplied regular expression. 
# The results should be printed to the screen.

import os, re


def regexSearch():
  print('Enter the path to a directory to search:')
  dirToSearch = input()
  print('Enter a regex to search with (usage: (r\'<userInput>\')):')
  regexSupplied = input()

  if dirToSearch == '' or regexSupplied == '':
    print('Please specify a directory and/or an expression to search with.')
    return False

  files = os.listdir(dirToSearch)
  textFiles = []
  os.chdir(dirToSearch)
  
  for fileName in files:
    if fileName.endswith('.txt'):
      contents = open(os.path.join('.', fileName)).read()
      results = re.findall(r'%s' % regexSupplied, contents)
      for result in results:
        print(result)

regexSearch()