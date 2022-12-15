import os
import re
os.chdir('D:/adventofcode2022/day eleven')
import numpy as np
import cv2


"""made two versions of the monkey class. There's deffo a more elegant way to do this """
class monkey_part_one:
    def __init__(self,items, test, op, true, false):
        self.test = test
        self.op = op
        self.items = items
        self.true = true
        self.false = false
        self.inspections = 0

    def pass_to_monkey(self,item,target):
        return item, target

    def turn(self):
        pass_dict = {self.true:[],self.false:[]}
        while len(self.items) > 0:
            curr = self.items.pop(0)
            result = int(eval(''.join([str(curr),self.op])) // 3)
            if result % self.test == 0:
                pass_dict[self.true].append(result)
            else:
                pass_dict[self.false].append(result)
            self.inspections += 1
        return pass_dict

class monkey_part_two:
    def __init__(self,items, test, op, true, false):
        self.test = test
        self.op = op
        self.items = items
        self.true = true
        self.false = false
        self.inspections = 0
    def pass_to_monkey(self,item,target):
        return item, target

    def turn(self, monkeymod):
        pass_dict = {self.true:[],self.false:[]}
        while len(self.items) > 0:
            curr = self.items.pop(0)
            result = eval(''.join([str(curr),self.op])) % monkeymod
            if result % self.test == 0:
                pass_dict[self.true].append(result)
            else:
                pass_dict[self.false].append(result)
            self.inspections += 1
        return pass_dict




def solution_part_one(input_path):
    monkeys = {}
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')
    i = 0
    """parsing"""
    while i < len(lines)-6:
        if 'Monkey' in lines[i]:
            instr = lines[i:i+6]
            name = [int(x) for x in instr[0] if x.isdigit()][0]
            items = [int(x) for x in instr[1][17:].split(',')]
            op = '**2' if 'old' in instr[2].split()[-1] else ''.join(instr[2].split()[len(instr[2].split())-2:len(instr[2].split())+1])
            test = [int(x) for x in instr[3].split() if x.isdigit()][0]
            true, false = [[int(x) for x in instr[i].split() if x.isdigit()][0] for i in range(4,6)]

            monkeys[name] = monkey_part_one(items, test, op, true, false)
            i += 5
        i += 1

    """main logic"""
    for rounds in range(20):
        for j in monkeys.keys():
            pass_dict = monkeys[j].turn()
            for i in pass_dict.keys():
                monkeys[i].items += pass_dict[i]


    final = sorted([monkeys[x].inspections for x in monkeys])[::-1]
    print(final[0]*final[1])

def solution_part_two(input_path):
    monkeys = {}
    with open(input_path) as f:
        lines = f.read()
    lines = lines.split('\n')
    i = 0
    monkeymod = 1
    """parsing"""
    while i < len(lines)-6:
        if 'Monkey' in lines[i]:
            instr = lines[i:i+6]
            name = [int(x) for x in instr[0] if x.isdigit()][0]
            items = [int(x) for x in instr[1][17:].split(',')]
            op = '**2' if 'old' in instr[2].split()[-1] else ''.join(instr[2].split()[len(instr[2].split())-2:len(instr[2].split())+1])
            test = [int(x) for x in instr[3].split() if x.isdigit()][0]
            true, false = [[int(x) for x in instr[i].split() if x.isdigit()][0] for i in range(4,6)]
            monkeymod *= test
            monkeys[name] = monkey_part_two(items, test, op, true, false)
            i += 5
        i += 1

    """main logic"""
    for rounds in range(10000):
        for j in monkeys.keys():
            pass_dict = monkeys[j].turn(monkeymod)
            for i in pass_dict.keys():
                monkeys[i].items += pass_dict[i]


    final = sorted([monkeys[x].inspections for x in monkeys])[::-1]
    print(final[0]*final[1])


solution_part_two('input.txt')