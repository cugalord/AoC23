from functools import reduce
from operator import mul


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data


def transform_p1(data):
    times = list(filter(None, data[0].replace('Time: ', '').split(' ')))
    distances = list(filter(None, data[1].replace('Distance: ', '').split(' ')))
    return [(int(time), int(distance)) for time, distance in zip(times, distances)]


def solve_part_one(data):
    result = []
    for time, record in data:
        record_breakers = [hold * (time - hold) for hold in range(1, time) if hold * (time - hold) > record]
        result.append(len(record_breakers))
    return reduce(mul, result)


def transform_p2(data):
    time = data[0].replace('Time: ', '').replace(' ', '')
    record = data[1].replace('Distance: ', '').replace(' ', '')
    return int(time), int(record)


def solve_part_two(data):
    time, record = data
    record_breakers = [hold * (time - hold) for hold in range(1, time) if hold * (time - hold) > record]
    return len(record_breakers)


def main():
    data = load_data('data/day6.txt')
    data1 = transform_p1(data)
    print(solve_part_one(data1))
    data2 = transform_p2(data)
    print(solve_part_two(data2))


main()
