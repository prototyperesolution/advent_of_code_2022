import os
import re
os.chdir('D:/adventofcode2022/day six')
import numpy as np

"""part 1 solution"""
def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    i = 0
    while i < len(lines)-4:
        if len(set(list(lines[i:i+4]))) == 4:
            return i+4
        else:
            i += 1

print(solution_part_one('input.txt'))

def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    i = 0
    while i < len(lines)-14:
        if len(set(list(lines[i:i+14]))) == 14:
            return i+14
        else:
            i += 1

print(solution_part_two('input.txt'))