import functools
import os
import numpy as np
import cv2
import re
from itertools import zip_longest
os.chdir('D:/adventofcode2022/day fourteen')

def parse_input(input_path):
    """reads the input path and returns a grid of the cave system"""
    with open(input_path) as f:
        lines = f.read()
    lines= lines.split('\n')[:-1]
    grid = np.zeros((600,200))
    for line in lines:
        curr = re.findall(r'\d+', ''.join(line))
        curr = [int(x) for x in curr]
        curr = np.reshape(np.array(curr), (len(curr)//2,2))
        for i in range(len(curr) - 1):
            grid[curr[i][0], curr[i][1]] = 1
            if curr[i + 1][0] == curr[i][0]:
                grid[curr[i][0], np.min([curr[i][1], curr[i+1][1]]):np.max([curr[i][1], curr[i+1][1]])+1] = 1
            if curr[i + 1][1] == curr[i][1]:
                grid[np.min([curr[i][0],curr[i + 1][0]]):np.max([curr[i][0], curr[i+1][0]])+1, curr[i][1]] = 1

    return(grid)


def drop_sand(source, grid):
    pos = np.array(source)
    '''if we've fallen off the grid we return the source'''
    while True:
        if pos[1]+1 == len(grid[0]):
            pos = source
            return pos
        if grid[pos[0],pos[1]+1] == 0:
            pos[1] += 1
        elif grid[pos[0]-1, pos[1]+1] == 0:
            pos[0] -= 1
            pos[1] += 1
        elif grid[pos[0]+1, pos[1]+1] == 0:
            pos += 1
        else:
            break

    return pos


def solution_part_one(input_path):
    grid = parse_input(input_path)
    source = np.array([500,0])
    while True:
        new = drop_sand(source, grid)
        if new.all() != source.all():
            grid[new[0],new[1]] = 2
        else:
            break
    grid = grid//2
    total = np.sum(grid)
    print(total)
    cv2.imshow('grid', grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



solution_part_one('input.txt')