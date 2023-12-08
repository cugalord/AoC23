from itertools import cycle
from math import lcm


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data


def transform_data(data):
    nodes = dict()
    instructions = [char for char in data[0]]

    for row in data[2:]:
        split = row.split(' = ')
        nodes[split[0]] = tuple(split[1].replace(')', '').replace('(', '').split(', '))
    return instructions, nodes


def find_zzz(instructions, nodes):
    key = 'AAA'
    steps = 0
    for direction in cycle(instructions):
        if key == 'ZZZ':
            return steps

        steps += 1
        if direction == 'R':
            key = nodes[key][1]
        else:
            key = nodes[key][0]


def find_z(instructions, nodes):
    keys = set(node for node in nodes.keys() if node.endswith('A'))

    steps = 0
    solution = []
    new_keys = set()
    for direction in cycle(instructions):
        if len(keys) == 0:
            return solution
        matched = [key for key in keys if key.endswith('Z')]
        for key in matched:
            keys.remove(key)
            solution.append(steps)

        steps += 1
        for key in keys:
            if direction == 'R':
                new_keys.add(nodes[key][1])
            else:
                new_keys.add(nodes[key][0])
        keys = new_keys.copy()
        new_keys.clear()


def main():
    instructions, nodes = transform_data(load_data('data/day8.txt'))
    result = find_zzz(instructions, nodes)
    print(result)
    result2 = find_z(instructions, nodes)
    print(lcm(*result2))


main()
