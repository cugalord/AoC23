import re
from functools import reduce


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data


def symbols(data):
    symbols = (set(sym for row in data for sym in re.findall('[^.|0-9]', row)))
    return symbols

def checker(data,i,j):
    nums = set(next(iter([((int(num.group(0))), num.start(0), num.end(0)) for num in re.finditer('[0-9]+', data[i+io]) if num.start(0) <= j + jo < num.end(0)]), (None, 0, 0)) for jo in range(-1, 2) for io in range(-1,2))
    return [num for num,s_ind,e_ind in nums if num is not None]


def solve_part_one(data: list[str]):
    match_sym=symbols(data)
    result=0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char in match_sym:
                result += sum(checker(data, i, j))
    print(result)

def solve_part_two(data: list[str]):
    match_sym=symbols(data)
    result=0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char in '*':
                nums=checker(data, i, j)
                if len(nums) > 1:
                    result += reduce((lambda x, y: x * y), checker(data, i, j))
    print(result)

def main():
    data = load_data('data/day3.txt')
    solve_part_two(data)


main()



