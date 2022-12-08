import numpy as np
import math

# h1 = deck is completely shuffled
# h2 = deck is shuffled by number
# h3 = deck is shuffled by suit

def calc_log_likelihood_h1(seq_len):
    prob = 0
    curr = 52
    while seq_len > 0:
        prob += np.log(1/curr)
        curr -= 1
        seq_len -= 1
    return prob

def calc_log_likelihood_h2(seq_len):
    num_repeats = seq_len - seq_len % 13 # the number of values that repeat within a sequence
    num_nonrepeats = seq_len - num_repeats # the number of values that don't repeat

    return np.log(1/13) + np.log(1/2) + num_nonrepeats * np.log(1/4) + num_repeats * np.log(1/3)

def calc_log_likelihood_h3(seq_len):
    num_seq = num_seq_in_h3(seq_len)
    return -1*np.log(num_seq)

def calc_log_likelihood_all(d):
    hs = [0]*3
    hs[0] = calc_log_likelihood_h1(len(d))
    if is_shuff_by_num(d):
        hs[1] = calc_log_likelihood_h2(len(d))
    if is_shuff_by_suit(d):
        hs[2] = calc_log_likelihood_h3(len(d))
    
    return hs

def calculate_likelihood(d):
    """
    Calculates the likelihood of the data for each of the three hypotheses:
        h1 = the deck is completely shuffled
        h2 = the deck is shuffled by number
        h3 = the deck is shuffled by suit

    Inputs
    ------
    d: a list of lenght-2 lists, each of which represents a card, where the first index is a numerical
        value (where A = 1, J = 11, Q = 12, K = 13) and the second is the string of the suit (i.e. 'C', 'D', 'H', 'S')

    Returns
    ------
    hs: a list containing the likelihood for all 3 possible hypotheses in the order [P(d|h1), P(d|h2), P(d|h3)]
    """
    hs = [0]*3
    hs[0] = 1 / num_seq_in_h1(len(d))
    if is_shuff_by_num(d):
        hs[1] = 1 / num_seq_in_h2(len(d))
    if is_shuff_by_suit(d):
        hs[2] = 1 / num_seq_in_h3(len(d))
    
    return hs

def num_seq_in_h1(seq_len):
    """
    Calculates the number of possible sequences by hypothesis 1 of the specified sequence length

    Inputs
    ------
    seq_len: the length of the sequence of cards

    Returns
    ------
    num_sequences: the number of possible sequences = 52*51*...*(52-seq_len+1)
    """
    num_sequences = 1
    curr = 52
    while seq_len > 0:
        num_sequences *= curr
        curr -= 1
        seq_len -= 1
    return num_sequences

def is_shuff_by_num(d):
    """
    Returns whether the sequence is shuffled by number in either ascending or descending order

    Input
    ------
    d: the sequence to check

    Returns
    ------
    true if the sequence is shuffled by number (with wrap around), false otherwise
    """
    ascending = True
    descending = True
    for i in range(len(d)-1):
        diff = d[i+1][0] - d[i][0]
        if (diff != 1 or int(diff) != diff) and not (d[i][0] == 13 and d[i+1][0] == 1):
            ascending = False
        if (diff != -1 or int(diff) != diff) and not (d[i][0] == 1 and d[i+1][0] == 13):
            descending = False
        if not (ascending or descending):
            break
    return ascending or descending

def num_seq_in_h2(seq_len):
    """
    Calculates the number of possible sequences by hypothesis 2 of the specified sequence length
    Precondition: the sequence must be possible by hypothesis 2

    Input
    ------
    seq_len: The sequence length

    Returns
    ------
    the number of possible sequences
        - for seq_len = 5: (13)(2)(4^5)
        - for seq_len = 10: (13)(2)(4^10)
        - for seq_len = 15: (13)(2)(4^13)(3^2)
    """
    num_repeats = seq_len - seq_len % 13 # the number of values that repeat within a sequence
    num_nonrepeats = seq_len - num_repeats # the number of values that don't repeat

    return 13 * 2 * 4**num_nonrepeats * 3**num_repeats

def num_seq_in_h3(seq_len):
    """
    Calculates the number of possible sequences by hypothesis 3 od the specified sequence length
    Precondition: the sequence must be possible by hypothesis 3

    Input
    ------
    seq_len: The length of the sequence

    Returns
    ------
    the number of possible sequences
    """
    num_cards_per_suit = memoize_num_cards_per_suit()

    num_selected_per_suit = [min(seq_len,13),max(seq_len-13,0),0]
    total = 0
    while num_selected_per_suit[0] > 0:
        temp_sum = 4*num_cards_per_suit[num_selected_per_suit[0]]
        if num_selected_per_suit[1] > 0:
            temp_sum *= 3*num_cards_per_suit[num_selected_per_suit[1]]
        if num_selected_per_suit[2] > 0:
            temp_sum *= 2*num_cards_per_suit[num_selected_per_suit[2]]
        total += temp_sum
        num_selected_per_suit[0] -= 1
        if num_selected_per_suit[1] < 13:
            num_selected_per_suit[1] += 1
        else:
            num_selected_per_suit[2] += 1
    return total

def is_shuff_by_suit(d):
    """
    Determines whether the length of the sequence is shuffled by suit
    """
    d_suits = set([point[1] for point in d])
    if len(d) < 15 and len(d_suits) > 2:
        return False
    
    suit_count = 0
    seen_suits = []
    suit_ind = 0
    for card in d:
        suit = card[1]
        if not seen_suits:
            seen_suits.append(suit)
        if suit == seen_suits[-1]:
            suit_count += 1
        else:
            if suit in seen_suits:
                return False
            if suit_ind == 1 and not suit_count == 13:
                return False
            seen_suits.append(suit)
            suit_ind += 1
            suit_count = 1
    return True
    
def memoize_num_cards_per_suit():
    memo = {0:1}
    i = 1
    for val in range(13,0,-1):
        memo[i] = memo[i-1] * val
        i += 1
    return memo

# d = [[1,'S'],[2,'S'],[3,'S'],[4,'H'],[5,'H']]
# d2 = [[13,'H'],[1,'S'],[2,'S'],[3,'S'],[4,'H'],[5,'H']]
# print(is_shuff_by_suit(d))
# print(is_shuff_by_num(d2))

# print(calculate_likelihood(d))

print(1/num_seq_in_h3(5))
print(calc_log_likelihood_h3(5))
print()
print(1/num_seq_in_h3(10))
print(calc_log_likelihood_h3(10))
print()
print(1/num_seq_in_h3(15))
print(calc_log_likelihood_h3(15))
