import re
def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data


def solve_part_one(data):
    result=0
    for line in data:
        game_id = int(line[:line.find(':')].replace('Game ', ''))
        if any(gballs > 13 for gballs in [int(green_rounds[0].replace(' green','')) if green_rounds else 0 for green_rounds in [re.findall('[0-9]+ green', round) for round in line.split(';')]]):
            continue
        if any(bballs > 14 for bballs in [int(blue_rounds[0].replace(' blue','')) if blue_rounds else 0 for blue_rounds in [re.findall('[0-9]+ blue', round) for round in line.split(';')]]):
            continue
        if any(rballs > 12 for rballs in [int(red_rounds[0].replace(' red','')) if red_rounds else 0 for red_rounds in [re.findall('[0-9]+ red', round) for round in line.split(';')]]):
            continue
        else:
            result += game_id
    return result

def solve_part_two(data):
    result=0
    for line in data:
        g = max([int(green_rounds[0].replace(' green','')) if green_rounds else 0 for green_rounds in [re.findall('[0-9]+ green', round) for round in line.split(';')]])
        r = max([int(blue_rounds[0].replace(' blue','')) if blue_rounds else 0 for blue_rounds in [re.findall('[0-9]+ blue', round) for round in line.split(';')]])
        b = max([int(red_rounds[0].replace(' red','')) if red_rounds else 0 for red_rounds in [re.findall('[0-9]+ red', round) for round in line.split(';')]])
        result += g*r*b
    return result




def main():
    data = load_data('data/day2.txt')
    print(data)
    print(solve_part_two(data))


main()
