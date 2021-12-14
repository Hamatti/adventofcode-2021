import os


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
        
def read_day_13():
    try:
        with open(os.path.join('..', 'inputs', 'day_13.txt')) as input_file:
            coordinates_input, instructions = input_file.read().split('\n\n')
            coordinates_input = coordinates_input.split('\n')
            
            coordinates = []
            for coordinate in coordinates_input:
                x, y = coordinate.split(',')
                coordinates.append((int(x), int(y)))
            folds = []
            for instruction in instructions.split('\n'):
                _, location = instruction.split('fold along ')
                plane, value = location.split('=')
                value = int(value)
                folds.append((plane, value))
                
            return coordinates, folds
    except FileNotFoundError as e:
        print(e)
        
def read_day_14():
    try:
        with open(os.path.join('..', 'inputs', 'day_14.txt')) as input_file:
            template, pairings = input_file.read().split('\n\n')
            pairs = {}
            for pairing in pairings.split('\n'):
                start, insertion = pairing.split(' -> ')
                pairs[start] = insertion
            return template, pairs            
    except FileNotFoundError as e:
        print(e)