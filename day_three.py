import os
os.chdir('D:/adventofcode2022/day three')

"""part 1 solution"""
def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split()
    total = 0
    for line in lines:
        comp1, comp2 = line[:int(len(line)/2)], line[int(len(line)/2):]
        letter = ''
        c1s = set()
        for l in comp1:
            c1s.add(l)
        for l in comp2:
            if l in c1s:
                letter = l

        if letter.isupper():
            total += 26
            letter = letter.lower()
        total += ord(letter)-ord('a') + 1

    return total

"""part 2 solution"""
def solution_part_two(input_path):
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split()
    total = 0
    for i in range(0,len(lines),+3):
        letter = ''
        inter = set(list(lines[i]))&set(list(lines[i+1]))&set(list(lines[i+2]))
        letter = inter.pop()
        if letter.isupper():
            total += 26
            letter = letter.lower()
        total += ord(letter)-ord('a') + 1
    return total

print(solution_part_two('input.txt'))