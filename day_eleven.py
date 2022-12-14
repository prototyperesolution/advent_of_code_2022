import os
import re
os.chdir('D:/adventofcode2022/day eleven')
import numpy as np
import cv2

def solution_part_one(input_path):
    with open(input_path) as f:
        lines = f.read()