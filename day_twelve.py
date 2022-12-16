import os
import numpy as np
import cv2
os.chdir('D:/adventofcode2022/day twelve')
def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    grid = np.array([list(lines.split('\n')[x]) for x in range(len(lines.split('\n'))-1)])
    queue = []

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x,y] == 'S':
                queue.append((x,y))
                grid[x,y] = 'a'



    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x,y] == 'E':
                grid[x,y] = '{'

    shortest_dist = 0
    distances = {(queue[0][0], queue[0][1]): 0}
    new_grid = np.zeros((np.shape(grid)))
    while queue:
        curr = queue.pop(0)
        for neighbour in find_neighbours(curr[0],curr[1], grid):
            if (neighbour[0],neighbour[1]) not in distances:
                queue.append(neighbour)
                distances[(neighbour[0],neighbour[1])] = distances[(curr[0],curr[1])]+1
                new_grid[neighbour[0], neighbour[1]] = distances[(curr[0],curr[1])]+1
                if grid[neighbour[0], neighbour[1]] == '{':
                    shortest_dist = distances[(neighbour[0],neighbour[1])]
                    new_grid[neighbour[0],neighbour[1]] = 400
                    break
    print(shortest_dist)

def find_neighbours(x,y,grid):
    neighbours = []
    if x < len(grid)-1:
        if (ord(grid[x+1,y])) - (ord(grid[x,y])) <= 1:
            neighbours.append((x+1, y))
    if x >= 1:
        if (ord(grid[x-1,y])) - (ord(grid[x,y])) <= 1:
            neighbours.append((x-1, y))
    if y <len(grid[0])-1:
        if (ord(grid[x,y+1])) - (ord(grid[x,y])) <= 1:
            neighbours.append((x, y+1))
    if y >= 1:
        if (ord(grid[x,y-1])) - (ord(grid[x,y])) <= 1:
            neighbours.append((x, y-1))
    return neighbours

solution_part_one('input_2.txt')