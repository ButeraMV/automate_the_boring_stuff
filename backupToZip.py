#! /usr/bin/env python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, zipfile


def backupToZip(folder):
  # Backup the entire contents of 'folder' into a ZIP file.
  folder = os.path.abspath(folder) # Make sure the folder is absolute.

  # Figure out the filename this code should use based on what files already exist
  number = 1
  while True:
    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipFilename):
      break
    else:
      number += 1
  
  # Create the ZIP file.
  print('Creating %s...' % (zipFilename))
  backupZip = zipfile.ZipFile(zipFilename, 'w')

  # Walk the entire folder tree and compress the files in each folder.
  for foldername, subfolders, filenames in os.walk(folder):
    print('Adding files in the %s...' % (foldername))
    # Add the current folder to the ZIP file.
    backupZip.write(foldername)
    # Add all the files in this folder to the ZIP file.
    for filename in filenames:
      newBase = os.path.basename(folder) + '_'
      if filename.startswith(newBase) and filename.endswith('.zip'):
        continue # Don't backup the backup ZIP files.
      backupZip.write(os.path.join(foldername, filename))
  backupZip.close()
  print('Done.')

backupToZip('/Users/mbutera/practice/automate_the_boring_stuff/folderToZip')