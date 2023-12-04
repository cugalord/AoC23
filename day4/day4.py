import sys


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data

def split(data):
    pile = dict()
    for game in data:
        game_id = int(game[:game.find(': ')].replace('Card ', ''))
        game = game[game.find(': ') + 1:].split('|')
        winners = set(num for num in game[0].split(' ') if len(num) > 0)
        ticket = [num for num in game[1].split(' ') if len(num) > 0]
        pile[game_id] = ([winners, ticket])
    return pile

def solve_part_one(pile):
    pile_result = 0
    for winners, ticket in pile.values():
        if sum([1 for num in ticket if num in winners]) != 0:
            pile_result += 2 ** (sum([1 for num in ticket if num in winners]) - 1)

    return pile_result

def solve_part_two(pile):
    no_of_cards = [1] * len(pile)

    for index, data in pile.items():
        winners, ticket = data
        no_of_win = sum([1 for num in ticket if num in winners])

        for card in range(no_of_cards[index - 1]):
            for i in range(1, no_of_win + 1):
                if index - 1 < len(no_of_cards):
                    no_of_cards[index - 1 + i] += 1

    return sum(no_of_cards)


def main():
    data = split(load_data('data/day4.txt'))
    print(solve_part_one(data))
    print(solve_part_two(data))


main()
