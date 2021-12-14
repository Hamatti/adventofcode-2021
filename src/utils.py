import os


def read_input(day, transformer=str, example=False):
    """
    Given a day number (1-25), reads the corresponding input file into
    a list with each line as an item.
    
    Runs transformer function on each item.
    """
    try:
        if example:
            filename = f'day_{day}_example.txt'
        else:
            filename = f'day_{day}.txt'
        with open(os.path.join('..', 'inputs', filename)) as input_file:
            return [transformer(line.strip()) for line in input_file]
    except FileNotFoundError as e:
        print(e)
        

def read_multisection_input(day, transformers, example=False):
    """
    Given a day number (1-25), reads the corresponding input file, splits by empty line
    and runs a transformer function from `transformers` list for each section and returns
    a list of section outputs
    """
    try:
        if example:
            filename = f'day_{day}_example.txt'
        else:
            filename = f'day_{day}.txt'
        with open(os.path.join('..', 'inputs', filename)) as input_file:
            output = []
            sections = input_file.read().split('\n\n')
            for idx, section in enumerate(sections):
                output.append(transformers[idx](section))
            return output
    except FileNotFoundError as e:
        print(e)


def read_bingo_input(example=False):
    try:
        if example:
            filename = f'day_4_example.txt'
        else:
            filename = f'day_4.txt'
        with open(os.path.join('..', 'inputs', filename)) as input_file:
            data = input_file.read().split('\n\n')
            numbers, boards = data[0], data[1:]
            numbers = [int(n) for n in numbers.split(',')]
            return numbers, boards
    except FileNotFoundError as e:
        print(e)
