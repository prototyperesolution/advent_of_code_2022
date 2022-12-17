import functools
import os
import numpy as np
import cv2
from itertools import zip_longest
os.chdir('D:/adventofcode2022/day thirteen')

def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')[:-1]
    pairs = []
    i = 0
    indices = []
    while i < len(lines):
        pairs.append([eval(lines[i]),eval(lines[i+1])])
        i += 3

    print(pairs)

    for i in range(len(pairs)):
        if compare(pairs[i][0],pairs[i][1]) == -1:
            indices.append(i+1)
    return sum(indices)

def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')[:-1]
    pairs = []
    i = 0
    indices = []
    while i < len(lines):
        pairs.append([eval(lines[i])])
        pairs.append([eval(lines[i+1])])
        i += 3

    pairs.append([[6]])
    pairs.append([[2]])

    pairs = sorted(pairs, key=functools.cmp_to_key(compare))
    print(pairs.index([[6]]))
    print(pairs.index([[2]]))
    return (pairs.index([[6]])+1)* (pairs.index([[2]])+1)


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0
    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)


print(solution_part_two('input.txt'))