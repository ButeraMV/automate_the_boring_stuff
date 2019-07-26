#! /usr/bin/env python3
# madLibs.py - It's mad libs

# Create a Mad Libs program that reads in text files and 
# lets the user add their own text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
import os, re


def madLibs(filename):
  # Read in a text file.
  textFile = open('./txt/%s.txt' % filename)
  oldString = textFile.read()
  textFile.close()
  oldStringList = re.findall(r"[\w']+|[.,!?;]|\s", oldString)
  newString = ''

  # Scan for keywords and prompt for input.
  keywords = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
  for i in range(len(oldStringList)):
    for j in range(len(keywords)):
      if oldStringList[i] == keywords[j]:
        # Check for a or an.
        if keywords[j] == 'ADJECTIVE' or keywords[j] == 'ADVERB':
          print('Enter an %s:' % keywords[j].lower())
        else:
          print('Enter a %s:' % keywords[j].lower())
        # Replace keywords with user input
        newWord = input()
        oldStringList[i] = newWord

  # Save a new file with user input
  newFile = open('./txt/newMadLibs.txt', 'w')
  newFile.write(''.join(oldStringList))
  newFile.close()

madLibs('madLibs')
