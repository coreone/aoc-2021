#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 10."""
import sys
# import pdb


class InvalidLine(BaseException):
    """Exception for an invalid line."""


class IncompleteLine(BaseException):
    """Exception for an incomplete line."""


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            ret.append(line.rstrip())

    return ret


def validate(line):
    """Validate the chunks in a line."""
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    tracker = []

    for char in line:
        if char in pairs:
            tracker.append(pairs[char])
        else:
            if char != tracker.pop():
                raise InvalidLine(char)
        # print(tracker)

    if len(tracker) > 0:
        raise IncompleteLine(len(tracker))

    return True


def solution1(lines):
    """Find solution 1."""
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0

    for line in lines:
        try:
            validate(line)
        except InvalidLine as exc:
            char = str(exc)
            total += points[char]
            print(f"invalid: {line}: {char}")
        except IncompleteLine:
            print("incomplete")
            continue

    return total


def solution2(lines):
    """Find solution 2."""

    return 0


def main():
    """Execute the script."""
    lines = get_input("input.txt")
    # lines = get_input("j")
    answer = solution1(lines)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(lines)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
