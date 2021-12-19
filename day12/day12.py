#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 12."""
from copy import deepcopy
import sys
# import pdb


def get_input(file):
    """Get formatted input from the file."""
    ret = {}
    with open(file) as filep:
        index = 0
        for line in filep:
            tmp = line.rstrip().split("-")
            ret[index] = tmp
            index += 1

    return ret


# def make_tree(nodes):
#     """Make a tree structure from the nodes."""
#     tmpnodes = deepcopy(nodes)
#     tree = {"start": {}}

#     level = tree
#     while len(tmpnodes) > 0:
#         print(f"1: {level}")
#         moarnodes = deepcopy(tmpnodes)
#         pdb.set_trace()
#         for parent in level:
#             print(f"2: {parent}")
#             for index, node in moarnodes.items():
#                 if parent in node:
#                     idx = 0
#                     if node[1] == parent:
#                         idx = 1
#                     key = node[int(not idx)]
#                     level[parent][key] = {}
#                     print(f"{index}, {parent}, {node}")
#                     if index in tmpnodes:
#                         del tmpnodes[index]
#                         print(f"delete index {index}")

#         level = tree[parent]
#         pdb.set_trace()

#     return tree


def make_tree(nodes):
    """Make a tree structure from the nodes."""
    tree = {}
    for index, node in nodes.items():
        if node[0] not in tree:
            tree[node[0]] = []
        tree[node[0]].append(node[1])
        if node[1] not in tree:
            tree[node[1]] = []
        tree[node[1]].append(node[0])

    return tree


def solution1(nodes):
    """Find solution 1."""

    return 0


def solution2(nodes):
    """Find solution 2."""

    return 0


def main():
    """Execute the script."""
    nodes = get_input("input.txt")
    tree = make_tree(nodes)
    answer = solution1(nodes)
    print(f"Problem 1: answer: {answer}")
    answer = solution2(nodes)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
