import os
import re
os.chdir('D:/adventofcode2022/day nine')
import numpy as np
import cv2

def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')[:-1]
    h_pos, t_pos = [0,0],[0,0]
    t_set = set()
    md = {'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}
    for line in lines:
        dir, dis = line.split()
        for i in range(int(dis)):
            h_pos[0] += md[dir][0]
            h_pos[1] += md[dir][1]
            if abs(t_pos[0]-h_pos[0]) > 1 or abs(t_pos[1]-h_pos[1]) > 1:
                xdis = 0 if h_pos[0] == t_pos[0] else (h_pos[0] - t_pos[0]) / abs(h_pos[0] - t_pos[0])
                ydis = 0 if h_pos[1] == t_pos[1] else (h_pos[1] - t_pos[1]) / abs(h_pos[1] - t_pos[1])
                t_pos[0] += int(xdis)
                t_pos[1] += int(ydis)
                t_set.add((t_pos[0],t_pos[1]))

    return(len(t_set))

def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')[:-1]
    positions = [[0,0] for _ in range(10)]
    t_set = set()
    md = {'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}

    for line in lines:
        dir, dis = line.split()
        for i in range(int(dis)):
            positions[-1][0] += md[dir][0]
            positions[-1][1] += md[dir][1]
            for x in range(8,-1,-1):
                print('x is',x)
                if abs(positions[x][0] - positions[x+1][0]) > 1 or abs(positions[x][1] - positions[x+1][1]) > 1:
                    xdis = 0 if positions[x+1][0] == positions[x][0] else (positions[x+1][0] - positions[x][0]) / abs(positions[x+1][0] - positions[x][0])
                    ydis = 0 if positions[x+1][1] == positions[x][1] else (positions[x+1][1] - positions[x][1]) / abs(positions[x+1][1] - positions[x][1])
                    positions[x][0] += int(xdis)
                    positions[x][1] += int(ydis)

                if x == 0:
                    print('here')
                    t_set.add((positions[x][0], positions[x][1]))


    return(len(t_set))


print(solution_part_two('input.txt'))