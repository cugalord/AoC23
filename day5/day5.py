def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().split("\n\n"))
    return data


def transform_data(data):
    seeds = [int(n) for n in data[0].split(": ")[1].split()]
    maps = [[[int(m) for m in n.split()] for n in l.split(":\n")[1].splitlines()] for l in data[1:]]
    return seeds, maps


def get_1(depth, src, map_ranges):
    for c, d, dst in map_ranges[depth]:
        if c <= src < d:
            new = src - c + dst
            return new if depth == 6 else (get_1(depth + 1, new, map_ranges))
    return src if depth == 6 else get_1(depth + 1, src, map_ranges)


def part_one(seeds, maps):
    map_ranges = [[] for _ in range(7)]
    for depth, map in enumerate(maps):
        for dst, src, l in map:
            map_ranges[depth].append([src, src + l, dst])

    return min([get_1(0, seed, map_ranges) for seed in seeds])


def get_2(depth, a, b, map_ranges):
    for c, d, dst in map_ranges[depth]:
        if c <= a < d:
            if b < d:
                new_a, new_b = a - c + dst, b - c + dst
                return new_a if depth == 6 else get_2(depth + 1, new_a, new_b, map_ranges)
            else:
                return min(get_2(depth, a, d - 1,map_ranges), get_2(depth, d, b, map_ranges))
    return a if depth == 6 else get_2(depth + 1, a, b, map_ranges)


def part_two(seeds, maps):
    map_ranges = [[] for _ in range(7)]
    for depth, m in enumerate(maps):
        for dst, src, l in m:
            map_ranges[depth].append([src, src + l, dst])

    return min([get_2(0, seeds[i], seeds[i] + seeds[i + 1], map_ranges) for i in range(0, len(seeds), 2)])


def main():
    data = load_data('data/day5.txt')
    seeds, maps = transform_data(data)
    print(part_one(seeds, maps))
    print(part_two(seeds, maps))


main()
