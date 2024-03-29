#! /usr/local/bin/python3
# stopwatch.py - A simple stopwatch program.

import time


print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')
input()
print('Started.')
start_time = time.time()
last_time = start_time
lap_num = 1

# Start tracking lap times.
try:
  while True:
    input()
    lap_time = round(time.time() - last_time, 2)
    total_time = round(time.time() - start_time, 2)
    print('Lap %s: %s (%s)' % (lap_num, total_time, last_time), end='')
    lap_num += 1
    last_time = time.time()
except KeyboardInterrupt:
  print('\nDone')
