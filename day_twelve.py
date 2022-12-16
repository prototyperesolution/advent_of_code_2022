import os
import numpy as np
os.chdir('D:/adventofcode2022/day twelve')
def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    grid = np.array([list(lines.split('\n')[x]) for x in range(len(lines.split('\n'))-1)])
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x,y] == 'S':
                print(x,y)
    x, y = 0,0


def find_neighbours(x,y,grid):
    neighbours = []
    #if x <= len(grid)-1 and y <=len(grid[0])


solution_part_one('input.txt')