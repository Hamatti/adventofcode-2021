import os
from collections import namedtuple

Line = namedtuple('Line', ['x1', 'y1', 'x2', 'y2'])


def read_input(day, transformer=str):
    """
    Given a day number (1-25), reads the corresponding input file into
    a list with each line as an item.
    
    Runs transformer function on each item.
    """
    try:
        with open(os.path.join('..', 'inputs', f'day_{day}.txt')) as input_file:
            return [transformer(line.strip()) for line in input_file]
    except FileNotFoundError as e:
        print(e)
           
def read_bingo_input():
    try:
        with open(os.path.join('..', 'inputs', 'day_4.txt')) as input_file:
            data = input_file.read().split('\n\n')
            numbers, boards = data[0], data[1:]
            numbers = [int(n) for n in numbers.split(',')]
            return numbers, boards
    except FileNotFoundError as e:
        print(e)