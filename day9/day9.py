#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 9."""
from copy import copy
import sys


class Basins():
    """Class to keep track of the basins."""
    def __init__(self):
        """Initialize the class."""
        self.num_basins = 3
        self.basins = []
        for _ in range(0, self.num_basins):
            self.basins.append(0)

    def add(self, value):
        """Add a value to the basin."""
        index = -1
        for basin in self.basins:
            if value > basin:
                index += 1
                continue

        if index < 0:  # smaller than the lowest value
            return

        for place in range(0, index):
            self.basins[place] = self.basins[place + 1]
        self.basins[index] = value

    @property
    def product(self):
        """Calculate the product of all basins."""
        total = 1
        for basin in self.basins:
            total *= basin

        return total


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file, "r", encoding="ascii") as filep:
        for index, line in enumerate(filep):
            ret.append([])
            for num in line.rstrip():
                ret[index].append(int(num))

    return ret


def is_lowpoint(matrix, row, col):
    """Determine if the current point is a low point."""
    count = 0
    value = matrix[row][col]

    if row > 0:  # up
        if matrix[row - 1][col] > value:
            count += 1
    else:
        count += 1
    if col > 0:  # left
        if matrix[row][col - 1] > value:
            count += 1
    else:
        count += 1
    if row < (len(matrix) - 1):  # down
        if matrix[row + 1][col] > value:
            count += 1
    else:
        count += 1
    if col < (len(matrix[row]) - 1):  # right
        if matrix[row][col + 1] > value:
            count += 1
    else:
        count += 1

    if count == 4:
        return True

    return False


def walk_basin(matrix, row, col):
    """Walk the basin to find its size."""
    if (
         row < 0 or col < 0 or row > (len(matrix) - 1)
         or col > (len(matrix[row]) - 1)
         ):
        return 0
    if matrix[row][col] < 0:
        return 0
    if matrix[row][col] > 8:
        return 0

    total = 1
    matrix[row][col] = -1

    total += walk_basin(matrix, row - 1, col)  # up
    total += walk_basin(matrix, row + 1, col)  # down
    total += walk_basin(matrix, row, col - 1)  # left
    total += walk_basin(matrix, row, col + 1)  # right

    return total


def solution(numbers):
    """Find solution 1."""
    total = 0
    basins = Basins()

    for rownum, row in enumerate(numbers):
        for colnum, col in enumerate(row):
            if is_lowpoint(numbers, rownum, colnum):
                total += 1 + col
                matrix = copy(numbers)
                size = walk_basin(matrix, rownum, colnum)
                basins.add(size)

    return (total, basins.product)


def main():
    """Execute the script."""
    numbers = get_input("input.txt")
    (answer1, answer2) = solution(numbers)
    print(f"Problem 1: answer: {answer1}")
    print(f"Problem 2: answer = {answer2}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
