#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 7."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        ret = list(map(int, filep.readline().rstrip().split(",")))

    return ret


def find_max(numbers):
    """Find the maximum number in the set."""
    max_num = 0

    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def solution1(numbers):
    """Find solution 1."""
    max_coord = find_max(numbers)
    least = max_coord * len(numbers)

    for coord in range(0, max_coord):
        total = 0
        for num in numbers:
            total += abs(num - coord)
        if total < least:
            least = total

    return least


def gauss(val):
    """Gauss formula."""
    gsum = 0
    n_val = val
    if n_val % 2 != 0:
        gsum += n_val
        n_val -= 1

    n_2 = int(n_val / 2)
    gsum += n_2 * (n_val + 1)

    return gsum


def solution2(numbers):
    """Find solution 2."""
    max_coord = find_max(numbers)
    least = 0

    for coord in range(0, max_coord):
        total = 0
        for num in numbers:
            g_sum = gauss(abs(num - coord))
            total += g_sum
        if (least == 0) or (total < least):
            least = total

    return least


def main():
    """Execute the script."""
    numbers = get_input("input.txt")
    answer = solution1(numbers)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(numbers)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
