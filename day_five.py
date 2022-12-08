import os
import re
os.chdir('D:/adventofcode2022/day five')
import numpy as np

"""part 1 solution"""
def solution_part_one(input_path):

    """this is just parsing the boxes"""
    with open(input_path) as f:
        lines = f.read()
    boxes = lines[:(36*8)-1].split('\n')
    newlines = []
    for line in boxes:
        line = line[1::4]
        newlines.append(list(line))
    newlines = np.array(newlines)
    newlines = np.transpose(newlines)
    newlines = np.flip(newlines, axis=1)
    final_lines = []
    for i in range(len(newlines)):
        curr = ''.join(list(newlines[i]))
        curr = curr.split()
        curr = ''.join(curr)
        curr = list(curr)

        final_lines.append(curr)


    instr=lines[(36*9)+1:-1]
    instr = instr.split('\n')

    for ins in instr:
        nums = [int(x) for x in ins.split()[1::2]]
        tmp = [final_lines[nums[1]-1].pop() for x in range(nums[0])]
        final_lines[nums[2]-1] += tmp

    return ''.join([final_lines[i][-1] for i in range(len(final_lines))])


def solution_part_two(input_path):

    """this is just parsing the boxes"""
    with open(input_path) as f:
        lines = f.read()
    boxes = lines[:(36*8)-1].split('\n')
    newlines = []
    for line in boxes:
        line = line[1::4]
        newlines.append(list(line))
    newlines = np.array(newlines)
    newlines = np.transpose(newlines)
    newlines = np.flip(newlines, axis=1)
    final_lines = []
    for i in range(len(newlines)):
        curr = ''.join(list(newlines[i]))
        curr = curr.split()
        curr = ''.join(curr)
        curr = list(curr)

        final_lines.append(curr)


    instr=lines[(36*9)+1:-1]
    instr = instr.split('\n')

    for ins in instr:
        nums = [int(x) for x in ins.split()[1::2]]
        tmp = final_lines[nums[1]-1][-nums[0]:]
        final_lines[nums[1]-1] = final_lines[nums[1]-1][:-nums[0]]
        final_lines[nums[2]-1] += tmp

    return ''.join([final_lines[i][-1] for i in range(len(final_lines))])



print(solution_part_two('input.txt'))