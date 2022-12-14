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
    cts = {}
    for instr in instructions:
        if 'noop' in instr:
            cycles += 1
            cts[cycles] = sigstrength
        else:
            for i in range(2):
                cycles += 1
                cts[cycles] = sigstrength
            sigstrength += int(instr.split()[-1])

    ans = sum([x*cts[x] for x in range(20,260,40)])
    return ans


print(solution_part_one('input.txt'))