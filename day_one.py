import os
os.chdir('D:/adventofcode2022/day one')


"""part 1"""
def solution_one(input_path):
    with open(input_path) as f:
        lines = f.read()

    """goes thru every entry and splits it by double newline aka splits it into individuals"""
    lines = lines.split('\n\n')
    max = 0

    for i in range(len(lines)):
        if sum([int(x) for x in lines[i].split()]) > max:
            max = sum([int(x) for x in lines[i].split()])

    return max

"""part 2"""

def solution_two(input_path):
    with open(input_path) as f:
        lines = f.read()

    """goes thru every entry and splits it by double newline aka splits it into individuals"""
    lines = lines.split('\n\n')

    """sorting in descending order"""
    totals = sorted([sum([int(x) for x in lines[i].split()]) for i in range(len(lines))])[::-1]
    return sum(totals[:3])

print(solution_two('input.txt'))