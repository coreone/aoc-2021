#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 10."""
import sys


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
    incomplete_scores = {")": 1, "]": 2, "}": 3, ">": 4}
    tracker = []
    inv_points = 0

    for char in line:
        if char in pairs:
            tracker.append(pairs[char])
        else:
            if char != tracker.pop():
                raise InvalidLine(char)

    if len(tracker) > 0:
        while len(tracker) > 0:
            inv_points *= 5
            char = tracker.pop()
            inv_points += incomplete_scores[char]
        raise IncompleteLine(inv_points)

    return True


def sorted_insert(array, new_value):
    """Insert a value into a sorted list."""
    newlist = []
    if not array:
        return [new_value]

    inserted = False
    for value in array:
        if new_value < value and not inserted:
            newlist.append(new_value)
            inserted = True
        newlist.append(value)

    if not inserted:
        newlist.append(new_value)

    return newlist


def solution(lines):
    """Find solution 1."""
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    invalid_total = 0
    incomplete_totals = []

    for line in lines:
        try:
            validate(line)
        except InvalidLine as exc:
            char = str(exc)
            invalid_total += points[char]
        except IncompleteLine as exc:
            inc = int(str(exc))
            incomplete_totals = sorted_insert(incomplete_totals, inc)

    index = int(len(incomplete_totals) / 2)
    return (invalid_total, incomplete_totals[index])


def main():
    """Execute the script."""
    lines = get_input("input.txt")
    (answer1, answer2) = solution(lines)
    print(f"Problem 1: answer: {answer1}")
    print(f"Problem 2: answer = {answer2}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
