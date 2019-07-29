#! /usr/bin/env python3

import os

def findLargeFiles(folder, size):
  folder = os.path.abspath(folder)

  for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
      filePath = os.path.join(foldername, filename)
      if os.path.getsize(filePath) > size:
        print(filePath)

findLargeFiles('/Users/mbutera/Documents', 100000000)