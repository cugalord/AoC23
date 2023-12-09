import re
import collections


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data
def transform(data):
    transformed=[]
    for line in data:
        transformed.append([int(x) for x in line.split(' ')])
    return transformed

def transform_2(data):
    transformed = []
    for line in data:
        transformed.append([int(x) for x in line.split(' ')][::-1])
    return transformed

def find_next(sequence):
    diff_tree=[sequence]

    while not all([True if num==0 else False for num in diff_tree[-1]]):
        curr_tree=[]
        for i in range(0,len(diff_tree[-1])-1):
            curr_tree.append(diff_tree[-1][i+1]-diff_tree[-1][i])
        diff_tree.append(curr_tree)

    for i in range(len(diff_tree)-1,0,-1):
        diff_tree[i-1].append(diff_tree[i-1][-1]+diff_tree[i][-1])
    return diff_tree[0][-1]

def solve_part_one(data):
    result=0
    for sequence in data:
        result += find_next(sequence)
    print(result)

def main():
    data1 = transform(load_data('data/day9.txt'))
    solve_part_one(data1)
    data2=transform_2(load_data('data/day9.txt'))
    solve_part_one(data2)


main()
