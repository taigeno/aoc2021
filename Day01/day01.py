import itertools
import sys

with open('input.txt', 'r') as inputFile:
    lines = [int(line.strip()) for line in inputFile]

def part_one():
    sum = 0
    for i, _ in enumerate(lines):
        if i >= 1:
            if lines[i] > lines[i-1]:
                sum += 1
    print(sum)

def part_two():
    sum = 0
    for i, _ in enumerate(lines):
        if i >= 3:
            if lines[i] + lines[i-1] + lines[i-2] > lines[i-1] + lines [i- 2] + lines[i- 3]:
                sum += 1
    print(sum)

part_one()
part_two()
