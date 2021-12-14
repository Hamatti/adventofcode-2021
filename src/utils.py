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
        

def read_multisection_input(day, transformers):
    """
    Given a day number (1-25), reads the corresponding input file, splits by empty line
    and runs a transformer function from `transformers` list for each section and returns
    a list of section outputs
    """
    try:
        with open(os.path.join('..', 'inputs', f'day_{day}.txt')) as input_file:
            output = []
            sections = input_file.read().split('\n\n')
            for idx, section in enumerate(sections):
                output.append(transformers[idx](section))
            return output
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
