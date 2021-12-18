#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day ."""
from copy import deepcopy
import sys


def get_input(file):
    """Get formatted input from the file."""
    cards = {}
    rows = []
    with open(file) as filep:
        winners = list(map(int, filep.readline().rstrip().split(",")))
        card_num = 0
        for line in filep:
            line = line.rstrip()
            if not line:
                if rows:
                    cards[card_num] = rows
                    card_num += 1
                rows = []
                continue
            rows.append(list(map(int, line.split())))

    return (winners, cards)


def mark_cards(number, cards):
    """Mark all occurences of the provided number on all cards."""
    for _, card in cards.items():
        for row in card:
            for index, col in enumerate(row):
                if col == number:
                    row[index] = -1

    return cards


def check_rows(card):
    """Check all rows for a winner."""
    for row in card:
        count = 0
        for col in row:
            if col < 0:
                count += 1
        if count == 5:
            return True

    return False


def check_cols(card):
    """Check all columns for a winner."""
    for col in range(0, 5):
        count = 0
        for row in range(0, 5):
            if card[row][col] < 0:
                count += 1
        if count == 5:
            return True

    return False


def check_winners(cards):
    """Check all cards to see if there's a winner."""
    winners = []
    for index, card in cards.items():
        if check_rows(card) or check_cols(card):
            winners.append(index)

    return winners


def sum_card(card):
    """Find the sum of the card."""
    total = 0
    for row in card:
        for col in row:
            if col >= 0:
                total += col

    return total


def solution1(winners, cards):
    """Find solution 1."""
    newcards = deepcopy(cards)
    for num in winners:
        newcards = mark_cards(num, newcards)
        card_nums = check_winners(newcards)
        if card_nums:
            if len(card_nums) > 1:
                raise Exception("More than one card wins at the same time.")
            cnum = card_nums[0]
            total = sum_card(newcards[cnum])
            break

    return total * num


def solution2(winners, cards):
    """Find solution 2."""
    newcards = deepcopy(cards)
    done = False

    for num in winners:
        newcards = mark_cards(num, newcards)
        card_nums = check_winners(newcards)
        if card_nums:
            # print(f"{num}: {card_nums} {len(newcards)}")
            for cnum in card_nums:
                # for row in newcards[cnum]:
                #     print(row)
                # print("")
                if len(newcards) < 2:
                    total = sum_card(newcards[cnum])
                    done = True
                del newcards[cnum]
                # print(f"{'-'*40}")
        if done:
            break

    return total * num


def main():
    """Execute the script."""
    (winners, cards) = get_input("input.txt")
    answer = solution1(winners, cards)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(winners, cards)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
