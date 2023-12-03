import re


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data


def numerizer(data):
    converter = {'one': 'o1e',
                 'two': 't2o',
                 'three': 't3e',
                 'four': 'f4r',
                 'five': 'f5e',
                 'six': 's6x',
                 'seven': 's7n',
                 'eight': 'e8t',
                 'nine': 'n9e'
                 }
    numerized = []
    for line in data:
        for key, value in converter.items():
            line = line.replace(key, value)
        numerized.append(line)
    return numerized


def puzzle_solver(data):
    num = 0
    for line in data:
        digits_in_line = re.findall("\d", line)
        num += int(digits_in_line[0] + digits_in_line[-1])
    return num


def main():
    data = load_data('data/day1.txt')
    print(data)
    data = numerizer(data)
    print(puzzle_solver(data))


main()
