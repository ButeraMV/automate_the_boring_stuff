#! /usr/bin/env python3
# takes a list of lists of strings and displays it in 
# a well-organized table with each column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
  colWidths = [0] * len(tableData)
  for i in range(len(tableData)):
    longestItemLength = 0
    for item in tableData[i]:
      if longestItemLength < len(item):
        longestItemLength = len(item)
    colWidths[i] = longestItemLength
  
  for i in range(len(tableData[0])):
    for j in range(len(tableData)):
      print(str(tableData[j][i]).rjust(colWidths[j]), end = ' ')
    print('\n')


printTable(tableData)