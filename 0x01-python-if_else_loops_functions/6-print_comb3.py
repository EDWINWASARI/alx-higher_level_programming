#!/usr/bin/python3
for num in range(1, 10):
    print("{:02d}".format(num), end=", " if num < 9 else "\n")
