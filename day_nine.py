import os
import re
os.chdir('D:/adventofcode2022/day nine')
import numpy as np
import cv2

def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')[:-1]
    h_pos, t_pos = np.array([0,0]),np.array([0,0])
    t_set = set()
    t_list = []
    for line in lines:
        dir, dis = line.split()
        for i in range(int(dis)):
            if dir == 'U':
                h_pos[1] += 1
            elif dir == 'R':
                h_pos[0] += 1
            elif dir == 'L':
                h_pos[0] -=1
            else:
                h_pos[1] -= 1

            if abs(t_pos[0]-h_pos[0]) > 1 or abs(t_pos[1]-h_pos[1]) > 1:

                t_pos = (t_pos + ((h_pos-t_pos)/2)).astype(np.int64)
                t_list.append(t_pos)

    t_list = np.array(t_list)
    vis_grid = np.zeros((np.max(t_list[:,0])+1, np.max(t_list[:,1])+1))
    for coord in t_list:
        vis_grid[coord[0],coord[1]] += 20

    final = np.zeros(np.shape(vis_grid)) + 1
    final = np.where(vis_grid > 0, final, np.zeros(np.shape(vis_grid)))
    print(np.sum(final))
    vis_grid = cv2.resize(vis_grid, (500,500), interpolation = cv2.INTER_NEAREST)
    cv2.imshow('window',vis_grid.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


solution_part_one('input.txt')