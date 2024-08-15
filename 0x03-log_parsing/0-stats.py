#!/usr/bin/python3
'''Reads stdin line by line and returns the total file size
and the amount of each present status code'''


import re
import signal
import sys


total_size = 0
line_count = 0
status_codes = {}


def print_stats():
    '''Prints the accumulated file size and counts of status codes'''
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


def signal_handler(sig, frame):
    '''Handles Crtl+C signal to print stats before exiting'''
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

log_pattern = re.compile(r'^\S+ - \[\S+\] "GET \S+ HTTP/1.1" \d{3} \d+$')
if log_pattern.match(line):
    for line in sys.stdin:
        parts = line.split()
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code) + 1
        except (ValueError, IndexError):
            continue

        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
