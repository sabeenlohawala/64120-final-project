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


#def main():
    # ascending_deck = create_suit_deck()
    # print(ascending_deck)
    # random_deck = create_random_deck()
    # seq1 = []
    # for _ in range(5):
    #     seq1.append(random_deck.pop())
