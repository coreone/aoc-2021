#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day ."""
from copy import deepcopy
import logging
import os
import sys

LOGGER = logging.getLogger(os.path.basename(__file__))


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        for line in filep:
            ret.append(int(line.rstrip(), base=2))
        digits = len(line)

    return (ret, digits)


def identify_bits(number, factors):
    """Identify the bits in each number."""
    bits = []
    for factor in factors:
        if (number & factor) > 0:
            bits.append(1)
        else:
            bits.append(0)

    return bits


def accumulate(numbers, numbits):
    """Find solution 1."""
    accumulator = []
    factors = []

    # Setup the accumulator storage
    for index in range(0, numbits):
        accumulator.append({0: 0, 1: 0})
        # Slight optimization...only calculate powers of 2 once per run
        factors.append(2**(numbits - index - 1))

    for num in numbers:
        bits = identify_bits(num, factors)
        for index, bit in enumerate(bits):
            accumulator[index][bit] += 1

    return (accumulator, factors)


def solution1(numbers, numbits):
    """Find solution 1."""
    gamma_rate = 0
    epsilon_rate = 0

    (accumulator, factors) = accumulate(numbers, numbits)
    for index, data in enumerate(accumulator):
        if data[0] > data[1]:
            epsilon_rate += factors[index]
        else:
            gamma_rate += factors[index]

    return epsilon_rate * gamma_rate


def find_keepers(numbers, factor, acc_data, default):
    """Generate a list of numbers to keep."""
    ret_nums = []
    winner = 0
    if acc_data[1] > acc_data[0]:
        winner = 1
    if acc_data[1] == acc_data[0]:
        winner = -1

    for index, number in enumerate(numbers):
        num = 0
        if (number & factor) > 0:
            num = 1

        if winner < 0:
            if num == default:
                LOGGER.debug(f"adding {numbers[index]:12b} equal occurrence")
                ret_nums.append(numbers[index])
        elif (default == 1) and (num == winner):
            LOGGER.debug(f"adding {numbers[index]:12b} == {num}")
            ret_nums.append(numbers[index])
        elif (default == 0) and (num != winner):
            LOGGER.debug(f"adding {numbers[index]:12b} == {num}")
            ret_nums.append(numbers[index])

    LOGGER.debug("%s", "-"*40)

    return ret_nums


def solution2(numbers, numbits):
    """Find solution 2."""
    oxygen_nums = deepcopy(numbers)
    co2_nums = deepcopy(numbers)

    for bit in range(0, numbits):
        if len(oxygen_nums) > 1:
            (accumulator, factors) = accumulate(oxygen_nums, numbits)
            LOGGER.debug("acc: %s: %s", bit, accumulator[bit])
            LOGGER.debug(f"{' '*(7+bit)}v")
            oxygen_nums = find_keepers(oxygen_nums, factors[bit], accumulator[bit], default=1)
        if len(co2_nums) > 1:
            (accumulator, factors) = accumulate(co2_nums, numbits)
            LOGGER.debug("acc: %s: %s", bit, accumulator[bit])
            LOGGER.debug(f"{' '*(7+bit)}v")
            co2_nums = find_keepers(co2_nums, factors[bit], accumulator[bit], default=0)

    return oxygen_nums[0] * co2_nums[0]


def main():
    """Execute the script."""
    logging.basicConfig(level="INFO")
    (numbers, length) = get_input("input.txt")
    answer = solution1(numbers, length)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(numbers, length)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
