#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    ld = abs(number % 10)
    print("{:d}".format(ld), end="")
    return ld
