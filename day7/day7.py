import re
import collections


def load_data(filename):
    data = []
    with open(f'{filename}', 'rt') as file:
        data.extend(file.read().splitlines())
    return data


def transform(data):
    hands = []
    for line in data:
        line = line.split(' ')
        hands.append([line[0], int(line[1]), 0])
    return hands


def relative_strength(card):
    card_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                  '3': 3,
                  '2': 2}
    return card_order[card]


def hand_strength(hand):
    return [relative_strength(card) for card in hand[0]]


def hand_strength_joker(hand):
    joker_strength = 0
    for card in hand[0]:
        if card == 'J':
            joker_strength = max(joker_strength, 1)
        else:
            joker_strength = max(joker_strength, relative_strength(card))

    return [relative_strength(card) if card != 'J' else joker_strength for card in hand[0]]


def rank_hands(hands):
    type = {
        '5OA': [],
        '4OA': [],
        'FH': [],
        '3OA': [],
        '2P': [],
        '1P': [],
        'HC': []

    }
    for index, unpack in enumerate(hands):
        card_counts = collections.Counter([chr for chr in unpack[0]])
        if len(card_counts) == 1:
            type['5OA'].append(hands[index])
        elif len(card_counts) == 2 and 4 in card_counts.values():
            type['4OA'].append(hands[index])
        elif len(card_counts) == 2 and 3 in card_counts.values() and 2 in card_counts.values():
            type['FH'].append(hands[index])
        elif len(card_counts) == 3 and 3 in card_counts.values() and 1 in card_counts.values():
            type['3OA'].append(hands[index])
        elif len(card_counts) == 3 and 2 in card_counts.values() and 1 in card_counts.values():
            type['2P'].append(hands[index])
        elif len(card_counts) == 4:
            type['1P'].append(hands[index])
        else:
            type['HC'].append(hands[index])
    type['HC'] = sorted(type['HC'], key=lambda hand: [hand_strength(hand) for card in hand])
    type['1P'] = sorted(type['1P'], key=lambda hand: [hand_strength(hand) for card in hand])
    type['2P'] = sorted(type['2P'], key=lambda hand: [hand_strength(hand) for card in hand])
    type['3OA'] = sorted(type['3OA'], key=lambda hand: [hand_strength(hand) for card in hand])
    type['FH'] = sorted(type['FH'], key=lambda hand: [hand_strength(hand) for card in hand])
    type['4OA'] = sorted(type['4OA'], key=lambda hand: [hand_strength(hand) for card in hand])
    type['5OA'] = sorted(type['5OA'], key=lambda hand: [hand_strength(hand) for card in hand])
    ranks = type['HC']
    ranks.extend(type['1P'])
    ranks.extend(type['2P'])
    ranks.extend(type['3OA'])
    ranks.extend(type['FH'])
    ranks.extend(type['4OA'])
    ranks.extend(type['5OA'])
    tot_win = 0
    for rank, unpack in enumerate(ranks):
        tot_win += unpack[1] * (rank + 1)
        ranks[rank][2] = (rank + 1)
    return tot_win, ranks


def rank_hands_jokers(hands):
    type = {
        '5OA': [],
        '4OA': [],
        'FH': [],
        '3OA': [],
        '2P': [],
        '1P': [],
        'HC': []

    }
    for index, unpack in enumerate(hands):
        card_counts = collections.Counter([chr for chr in unpack[0]])
        if (len(card_counts) == 1) or (len(card_counts) == 2 and card_counts.get('J', 0) >= 1):
            type['5OA'].append(hands[index])

        elif (len(card_counts) == 2 and 4 in card_counts.values()) or (
                len(card_counts) == 3 and 3 in card_counts.values() and card_counts.get('J', 0) >= 1):
            type['4OA'].append(hands[index])

        elif (len(card_counts) == 2 and 3 in card_counts.values()):
            type['FH'].append(hands[index])

        elif (len(card_counts) == 3 and 3 in card_counts.values() and 1 in card_counts.values()):
            type['3OA'].append(hands[index])

        elif len(card_counts) == 3 and 2 in card_counts.values() and 1 in card_counts.values():
            type['2P'].append(hands[index])

        elif len(card_counts) == 4:
            type['1P'].append(hands[index])

        else:
            type['HC'].append(hands[index])

    type['HC'] = sorted(type['HC'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    type['1P'] = sorted(type['1P'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    type['2P'] = sorted(type['2P'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    type['3OA'] = sorted(type['3OA'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    type['FH'] = sorted(type['FH'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    type['4OA'] = sorted(type['4OA'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    type['5OA'] = sorted(type['5OA'], key=lambda hand: [hand_strength_joker(hand) for card in hand])
    ranks = type['HC']
    ranks.extend(type['1P'])
    ranks.extend(type['2P'])
    ranks.extend(type['3OA'])
    ranks.extend(type['FH'])
    ranks.extend(type['4OA'])
    ranks.extend(type['5OA'])
    tot_win = 0
    for rank, unpack in enumerate(ranks):
        tot_win += unpack[1] * (rank + 1)
        ranks[rank][2] = (rank + 1)
    return tot_win, ranks


def main():
    data = transform(load_data('data/day7.txt'))
    total_wins, data = rank_hands(data)
    print(total_wins)


main()
