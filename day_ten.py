import os
import re
os.chdir('D:/adventofcode2022/day ten')
import numpy as np
import cv2

def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    instructions = lines.split('\n')[:-1]
    cycles = 0
    sigstrength = 1
    ans = 0
    for instr in instructions:
        if 'noop' in instr:
            cycles += 1
            if cycles in range(20,260,40):
                ans += cycles*sigstrength
        else:
            for i in range(2):
                cycles += 1
                if cycles in range(20, 260, 40):
                    ans += cycles * sigstrength
            sigstrength += int(instr.split()[-1])
    return ans

def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    instructions = lines.split('\n')[:-1]
    cycles = 0
    sigstrength = 1
    ans = [['.' for x in range(40)]for i in range(6)]
    for instr in instructions:

        if 'noop' in instr:
            if cycles % 40 in range(sigstrength - 1, sigstrength + 2):
                ans[cycles // 40][cycles % 40] = '#'
            cycles += 1
        else:
            for i in range(2):
                if cycles % 40 in range(sigstrength - 1, sigstrength + 2):
                    ans[cycles // 40][cycles % 40] = '#'
                cycles += 1
            sigstrength += int(instr.split()[-1])


    return ans

for line in solution_part_two('input.txt'):
    print(line)
