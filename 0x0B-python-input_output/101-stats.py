#!/usr/bin/python3


import sys


def print_metrics(total_size, status_codes):
    print(f"File size: {total_size}")
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print(f"{code}: {count}")


def read_stdin():
    line_count = 0
    total_size = 0
    status_codes = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        }

    try:
        for line in sys.stdin:
            line_count += 1
            split_line = line.split()
            total_size += int(split_line[-1])

            if split_line[-2] in status_codes:
                status_codes[split_line[-2]] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise


if __name__ == "__main__":
    read_stdin()
