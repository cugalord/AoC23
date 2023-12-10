def load_data(filename):
    grid = []
    with open(f'{filename}', 'rt') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def solve_part_one(grid):
    pipes = {
'|': {(0, 1), (0, -1)},
'-': {(1, 0), (-1, 0)},
'L': {(0, -1), (1, 0)},
'J': {(0, -1), (-1, 0)},
'7': {(-1, 0), (0, 1)},
'F': {(0, 1), (1, 0)},
}

    DIST = {}
    start = None

    for y, row in enumerate(grid):
        if 'S' in row:
            start = (row.index('S'), y)
            break

    grid[start[1]][start[0]] = 'F'
    dist = 0
    pipe = start
    while pipe not in DIST:
        DIST[pipe] = dist
        dist += 1

        x, y = pipe
        c = grid[y][x]

        for dx, dy in pipes[c]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in DIST:
                pipe = (nx, ny)
                break

    return dist // 2, DIST



def solve_part_two(grid, DIST):
    tile_count = 0
    for y, row in enumerate(grid):
        parity = 0
        for x, c in enumerate(row):
            if (x, y) not in DIST:
                if parity % 2 == 1:
                    tile_count += 1
                continue

            if c in ['|', 'L', 'J']:
                parity += 1

    print(tile_count)

def main():
    grid = load_data('data/day10.txt')
    res, DIST = solve_part_one(grid)
    print(res)
    print(solve_part_two(grid,DIST))

main()