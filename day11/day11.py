#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 11."""
from copy import deepcopy
import os
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            tmp = []
            for char in line.rstrip():
                tmp.append(int(char))
            ret.append(tmp)

    return ret


def print_matrix(matrix):
    """Print out the matrix."""
    for row in matrix:
        line = ""
        for val in row:
            line += f"{val:3}"
        print(line)
    print("")


def increment(matrix):
    """Increment every cell in the matrix."""
    for yval in range(0, len(matrix)):
        for xval in range(0, len(matrix[0])):
            matrix[yval][xval] += 1


def adjacencies(matrix, row, col):
    """Increment a cell watching all adjacent cells."""
    for yval in range(row - 1, row + 2):
        # Boundaries
        if yval < 0 or yval > len(matrix) - 1:
            continue
        for xval in range(col - 1, col + 2):
            # Boundaries
            if xval < 0 or xval > len(matrix[yval]) - 1:
                continue
            # Skip self
            if yval == row and xval == col:
                continue
            if matrix[yval][xval] > 0:
                matrix[yval][xval] += 1


def flash(matrix):
    """Find flashes in the matrix and reset flashed octopi."""
    flashes = 0

    for yval, row in enumerate(matrix):
        for xval, col in enumerate(row):
            if col > 9:
                flashes += 1
                matrix[yval][xval] = 0
                adjacencies(matrix, yval, xval)

    return flashes


def solution1(numbers):
    """Find solution 1."""
    matrix = deepcopy(numbers)
    flashes = 0

    for _ in range(1, 101):
        increment(matrix)
        while True:
            tmp_flash = flash(matrix)
            if tmp_flash == 0:
                break
            flashes += tmp_flash

    return flashes


def solution2(numbers):
    """Find solution 2."""
    matrix = deepcopy(numbers)

    step = 1
    while True:
        flashes = 0
        increment(matrix)
        while True:
            tmp_flash = flash(matrix)
            if tmp_flash == 0:
                break
            flashes += tmp_flash
        if flashes == 100:
            break
        step += 1

    return step


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
