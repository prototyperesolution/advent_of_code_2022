import os
import re
os.chdir('D:/adventofcode2022/day four')

"""part 1 solution"""
def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split()
    total = 0
    for line in lines:
        line = [int(x) for x in (re.split('-|,', line))]
        ranges = [range(line[i], line[i+1]+1) for i in range(0,len(line),+2)]
        total += 1 if (line[2] in ranges[0] and line[3] in ranges[0]) or (line[0] in ranges[1] and line[1] in ranges[1]) else 0
    return total

"""part 2 solution"""
def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split()
    total = 0
    for line in lines:
        line = [int(x) for x in (re.split('-|,', line))]
        ranges = [range(line[i], line[i+1]+1) for i in range(0,len(line),+2)]
        total += 1 if (line[2] in ranges[0] or line[3] in ranges[0]) or (line[0] in ranges[1] or line[1] in ranges[1]) else 0
    return total
print(solution_part_two('input.txt'))