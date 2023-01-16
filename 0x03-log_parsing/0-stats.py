#!/usr/bin/python3
import sys

total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) != 7:
            continue

        ip_address, date, request, status_code, file_size = parts[0], parts[1], parts[2], int(parts[4]), int(parts[6])
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += file_size

        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            for status_code in sorted(status_codes.keys()):
                if status_codes[status_code] > 0:
                    print(f"{status_code}: {status_codes[status_code]}")
            print("-------------------")

except KeyboardInterrupt:
    print("Total file size: ", total_size)
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")
