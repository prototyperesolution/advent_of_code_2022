import os
import re
os.chdir('D:/adventofcode2022/day eight')
import numpy as np
import cv2

def visualise(grid):
    """visualising"""
    grid = np.array(grid)
    grid = grid * (256 / 4)
    grid = grid.astype(np.uint8)
    grid = cv2.resize(grid, (500, 500))
    cv2.imshow('grid vis', grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def find_highs(grid):
    newgrid = np.zeros(np.shape(grid))
    for i in range(0,len(grid)):
        highest_left, highest_right = 0,0
        print('new line ')
        for j in range(0,len(grid[i])):
            curr_left, curr_right = grid[i][j], grid[i][len(grid[i])-j-1]
            if curr_left > highest_left or j == 0:
                highest_left = curr_left
                newgrid[i][j] = 1
            if curr_right > highest_right or j == 0:
                highest_right = curr_right
                newgrid[i][len(grid[i])-j-1] = 1



    return newgrid


def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')
    lines = np.array(lines)
    grid = []
    for i in range(len(lines)):
        line = list(str(lines[i]))
        line = [int(x) for x in line]
        grid.append(line)
    grid = grid[:-1]
    grid = np.array(grid)

    newgrid = np.rot90(find_highs(grid))
    newgrid += find_highs(np.rot90(grid))
    final = np.zeros(np.shape(newgrid)) + 1
    final = np.where(newgrid > 0, final, np.zeros(np.shape(newgrid)))

    #tst = [0,1,2,3,4,5]
    print(newgrid)
    visualise(newgrid)
    return np.sum(final)



print(solution_part_one('input.txt'))