#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 5."""
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            data = {}
            pieces = line.rstrip().split()
            (data["x1"], data["y1"]) = map(int, pieces[0].split(","))
            (data["x2"], data["y2"]) = map(int, pieces[2].split(","))
            ret.append(data)

    return ret


def build_matrix(coordinates):
    """Builds a blank matrix of the correct size."""
    max_x = 0
    max_y = 0
    matrix = {}

    for line in coordinates:
        if line["x2"] > max_x:
            max_x = line["x2"]
        if line["y2"] > max_y:
            max_y = line["y2"]

    for yval in range(0, max_y + 1):
        matrix[yval] = []
        for xval in range(0, max_x + 1):
            matrix[yval].append(0)

    return matrix


def diagonal_fill(matrix, line):
    """Fill in a diagonal line in the matrix."""
    x_step = 1
    if line["x1"] > line["x2"]:
        x_step = -1

    y_step = 1
    if line["y1"] > line["y2"]:
        y_step = -1

    # Because it's a 45-degree angle, the difference between the X's and Y's needs to be the same.
    # So, only use the X's to calculate the range.
    diff_range = abs(line["x2"] - line["x1"])
    for val in range(0, diff_range + 1):
        x_coord = line["x1"] + (x_step * val)
        y_coord = line["y1"] + (y_step * val)
        matrix[y_coord][x_coord] += 1


def vertical_fill(matrix, line):
    """Fill in a diagonal line in the matrix."""
    # Pass for solution 1
    if line["x1"] != line["x2"]:
        raise Exception("Not a vertical line??")

    x_coord = line["x1"]
    step = 1
    if line["y1"] > line["y2"]:
        step = -1

    for yval in range(line["y1"], line["y2"] + step, step):
        matrix[yval][x_coord] += 1


def horizontal_fill(matrix, line):
    """Fill in a diagonal line in the matrix."""
    if line["y1"] != line["y2"]:
        raise Exception("Not a horizonal line??")

    y_coord = line["y1"]
    step = 1
    if line["x1"] > line["x2"]:
        step = -1

    for xval in range(line["x1"], line["x2"] + step, step):
        matrix[y_coord][xval] += 1


def fill_matrix(coordinates, diagonal=False):
    """Fill in a matrix with lines, optionally with diagonal lines."""
    matrix = build_matrix(coordinates)

    for line in coordinates:
        if line["x1"] == line["x2"]:
            vertical_fill(matrix, line)
        elif line["y1"] == line["y2"]:
            horizontal_fill(matrix, line)
        else:
            if diagonal:
                diagonal_fill(matrix, line)

    return matrix


def solution1(coordinates, diagonal=False):
    """Find solution 1."""
    total = 0

    matrix = fill_matrix(coordinates, diagonal=diagonal)
    for y_val in matrix:
        for point in matrix[y_val]:
            if point > 1:
                total += 1

    return total


def solution2(coordinates):
    """Find solution 2."""
    total = solution1(coordinates, diagonal=True)
    return total


def main():
    """Execute the script."""
    coordinates = get_input("input.txt")
    answer = solution1(coordinates)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(coordinates)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
