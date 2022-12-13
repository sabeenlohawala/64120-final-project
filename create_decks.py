""" Creates the Decks based on our different hypothesis and  allows us to get a sequence that is representative
of that hypotheis"""

from operator import itemgetter

SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def create_random_deck():
    """
    Creates the deck from hypothesis 1

    :return: a fully shuffled deck
    """
    deck = set()
    for suite in SUITS:
        suite_cards = {(rank, f'{suite}') for rank in RANKS}
        deck.update(suite_cards)
    return deck


def create_ascending_deck():
    """
    Creates the deck from hypothesis 2
    :return: a deck shuffled in ascending order
    """
    deck = sorted(create_random_deck(), key=itemgetter(0))
    ascending_deck = []
    for i in range(int(len(deck) / 13)):
        temp_deck = deck[i::4]
        ascending_deck.append(temp_deck)
    return ascending_deck


def create_suit_deck():
    """
    Creates the deck from hypothesis 3
    :return: a deck shuffled by suit
    """
    deck = create_random_deck()
    sort_order = list(set(SUITS))
    return list(sorted(deck, key=lambda i: sort_order.index(i[1])))


def create_sequence(h, n):
    """
    Input:
    :param h: integer corresponding to the desired hypothesis
    :param n: length of sequence

    Output
    :return: a sequence drawn from a deck corresponding to each sequence
    """

    if h == 1:
        deck = create_random_deck()
    elif h == 2:
        deck = create_ascending_deck()
    elif h == 3:
        deck = create_suit_deck()
    else:
        raise Exception("Not a valid hypothesis")

    sequence = []
    for _ in range(n):
        sequence.append(deck.pop())

    return sequence


# def main():
# ascending_deck = create_suit_deck()
# print(ascending_deck)
# random_deck = create_random_deck()
# seq1 = []
# for _ in range(5):
#     seq1.append(random_deck.pop())
