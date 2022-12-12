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
    grid = [[int(x) for x in line] for line in lines[:-1]]

    newgrid = np.rot90(find_highs(grid))
    newgrid += find_highs(np.rot90(grid))
    final = np.zeros(np.shape(newgrid)) + 1
    final = np.where(newgrid > 0, final, np.zeros(np.shape(newgrid)))

    visualise(newgrid)
    return np.sum(final)

def line_score(line, point):
    up_vis, down_vis = 0,0
    for i in range(point+1, len(line)):
        if line[i] >= line[point]:
            up_vis = i-point
            break
        up_vis = len(line) - point - 1
    for i in range(point-1, -1, -1):
        if line[i] >= line[point]:
            down_vis = point-i
            break
        down_vis = point
    return up_vis*down_vis

def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')
    grid = np.array([[int(x) for x in line] for line in lines[:-1]])

    max = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score = line_score(grid[i],j)
            score *= line_score(grid[:,j],i)
            if score > max:
                max = score

    return max





print(solution_part_two('input.txt'))