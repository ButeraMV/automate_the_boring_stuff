#! /usr/bin/env python3
# A program that walks through a folder tree and searches for 
# files with a certain file extension (such as .pdf or .jpg)
# and copies them into a new folder.

import os, shutil


def selectiveCopy(folder, extension):
  folder = os.path.abspath(folder)
  destFolder = os.path.dirname(folder) + '/' + os.path.basename(folder) + '_copy'
  if not os.path.exists(destFolder):
    os.makedirs(destFolder)
  for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith(extension):
        src = os.path.join(foldername, filename)
        dst = os.path.join(destFolder, filename)
        shutil.copy(src, dst)
  print('Done.')

selectiveCopy('folderToCopy', 'txt')
