#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 1."""
import sys


def get_numbers(file):
    """Get numbers from the file."""
    nums = []
    with open(file, "r", encoding="ascii") as filep:
        for line in filep:
            num = int(line.strip())
            nums.append(num)

    return nums


def solution1(nums):
    """Find solution 1."""
    total = 0
    last = nums[0]
    for num in nums:
        if num > last:
            total += 1
        last = num

    return total


def solution2(nums):
    """Find solution 2."""
    total = 0
    last = nums[0] + nums[1] + nums[2]
    for index in range(0, len(nums) - 2):
        subtotal = nums[index] + nums[index+1] + nums[index+2]
        if subtotal > last:
            total += 1
        last = subtotal

    return total


def main():
    """Execute the script."""
    nums = get_numbers("input.txt")
    sol = solution1(nums)
    print(f"Problem 1: {sol}")
    sol = solution2(nums)
    print(f"Problem 2: {sol}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
