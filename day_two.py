import os
os.chdir('D:/adventofcode2022/day two')

"""part 1 solution"""
def solution_part_one(input_path):
    #draw, loss
    hm = {'A':['X','Y'],'B':['Y','Z'],'C':['Z','X']}
    r = ['X','Y','Z']
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split()
    score = 0
    for i in range(0, len(lines), +2):
        score += ((hm[lines[i]].index(lines[i+1])+1)*3)+r.index(lines[i+1])+1 if lines[i+1] in hm[lines[i]] else r.index(lines[i+1])+1
    return score

"""part 2 solution"""
def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split()
    #win, draw, lose
    em = {'A':['S','R','P'],'B':['R','P','S'],'C':['P','S','R']}
    m = ['R','P','S']
    hm = ['X','Y','Z']
    score = 0
    for i in range(0,len(lines),+2):
        score += (hm.index(lines[i+1])*3) + (m.index(em[lines[i]][hm.index(lines[i+1])])+1)
    return score

print(solution_part_two('input.txt'))