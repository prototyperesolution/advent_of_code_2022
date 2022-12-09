import os
import re
os.chdir('D:/adventofcode2022/day seven')
import numpy as np

class directory:
    def __init__(self,name, parent):
        self.name = name
        """parent is just gonna be name of parent"""
        self.parent = parent

        self.subdirs = set()
        self.files = {}


class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size

"""part 1 solution"""
def solution_part_one(input_path):
    visited_dirs = {}
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('$')
    current_dir = 'home'
    for line in lines:
        line = line.split('\n')
        command = line[0]
        if ' cd ' in command:
            new_dir = command.split()[-1]
            if new_dir in visited_dirs.keys():
                current_dir = current_dir + new_dir
            elif new_dir == '..':
                current_dir = visited_dirs[current_dir].parent
            else:
                visited_dirs[current_dir+'/'+new_dir] = directory(current_dir+'/'+new_dir, current_dir)
                current_dir = current_dir+'/'+new_dir
        elif command == ' ls':
            items = line[1:]
            for item in items:
                if item != '':
                    if 'dir ' in item:
                        new_dir_name = item.split()[-1]
                        visited_dirs[current_dir].subdirs.add(current_dir+'/'+new_dir_name)
                    else:
                        if item.split()[-1] not in visited_dirs[current_dir].files:
                            visited_dirs[current_dir].files[item.split()[-1]] = (file(item.split()[-1], int(item.split()[0])))

    """dfs size finding function"""
    def find_dir_size(dir):
        size = 0
        for file in visited_dirs[dir].files:
            size += visited_dirs[dir].files[file].size
        for subdir in visited_dirs[dir].subdirs:
            size += find_dir_size(subdir)
        return size

    total = 0
    print(len(visited_dirs), len(list(set(list(visited_dirs.keys())))))

    for dir in visited_dirs:
        if find_dir_size(dir) <= 100000:
            total += find_dir_size(dir)
    return total



print(solution_part_one('input.txt'))