#!/usr/bin/python3
'''Reads stdin line by line and returns the total file size
and the amount of each present status code'''


import signal
import sys


status_codes = {}


for line in sys.stdin:
    parts = line.split()
    status_code = parts[-2]
    try:
        file_size = int(parts[-1])
    except ValueError:
        continue
    total_size += file_size
    status_codes[status_code] = status_codes.get(status_code) + 1

    def signal_handler(sig, frame):
        '''Breaks the loop when Crtl+C is pressed'''
        break

    signal.signal(signal.SIGINT, signal_handler)

    if line_count == 10:
        break
    else:
        line_count += 1

print("File size:", total_size)
for code in sorted(status_codes.keys()):
    print(f"{code}: {status_codes[code]}")

