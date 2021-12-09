#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 8."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            data = {}
            tmp = line.split("|")
            data["patterns"] = tmp[0].split()
            data["outputs"] = tmp[1].split()
            ret.append(data)

    return ret


def solution1(signals):
    """Find solution 1."""
    total = 0

    for data in signals:
        for output in data["outputs"]:
            if len(output) in [2, 3, 4, 7]:
                total += 1

    return total


def solution2(signals):
    """Find solution 2."""

    return 0


def main():
    """Execute the script."""
    signals = get_input("input.txt")
    answer = solution1(signals)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(signals)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
