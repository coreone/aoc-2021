#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 2."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            ret.append(line.rstrip())

    return ret


def solution1(directions):
    """Find solution 1."""
    horiz_pos = 0
    depth = 0

    for instruction in directions:
        (direction, val) = instruction.split()
        val = int(val)
        if direction.startswith("f"):
            horiz_pos += val
        elif direction.startswith("u"):
            depth -= val
        else:
            depth += val

    return (horiz_pos, depth)


def solution2(directions):
    """Find solution 2."""
    horiz_pos = 0
    depth = 0
    aim = 0

    for instruction in directions:
        (direction, val) = instruction.split()
        val = int(val)
        if direction.startswith("f"):
            horiz_pos += val
            depth += aim * val
        elif direction.startswith("u"):
            aim -= val
        else:
            aim += val

    return (horiz_pos, depth)


def both(directions):
    """Find both solutions."""
    horiz_pos = 0
    depth = 0
    aim = 0

    for instruction in directions:
        (direction, val) = instruction.split()
        val = int(val)
        if direction.startswith("f"):
            horiz_pos += val
            depth += aim * val
        elif direction.startswith("u"):
            aim -= val
        else:
            aim += val

    print(f"Problem 1: answer: {horiz_pos * aim}")
    print(f"Problem 2: answer: {horiz_pos * depth}")


def main():
    """Execute the script."""
    directions = get_input("input.txt")
    # answer = solution1(directions)
    # print(f"Problem 1: answer: {answer[0] * answer[1]}")
    # answer = solution2(directions)
    # print(f"Problem 2: answer: {answer[0] * answer[1]}")
    both(directions)

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
