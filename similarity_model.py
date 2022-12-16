import random

import numpy as np
import create_decks as cd
import matplotlib.pyplot as plt
from math import exp


def expected_alpha(h, n, graph=False):
    """
    :param h: The hypothesis for which we are trying to find the expected paramter
    :return:
    """
    alpha_vals = []
    deck = list(cd.create_random_deck())
    saved_mean_alpha = []
    for i in range(50000):
        random.shuffle(deck)
        sequence = cd.create_sequence(h, n, deck)
        # append one every time there is a change
        changes = [1 for i, x in enumerate(sequence[:-1]) if x[1] != sequence[i + 1][1]]
        alpha_vals.append(len(changes) + 1)
        mean_alpha = np.mean(alpha_vals)
        if i % 100 == 0:
            saved_mean_alpha.append(mean_alpha)
    if graph:
        x = range(1, 20000, 100)
        plt.plot(x, saved_mean_alpha)
        plt.xlabel('Number of sequences used')
        plt.ylabel('Mean/Expected Alpha ')
        plt.title(f'Convergence to Expected Value of Alpha: Hypothesis {h}')
        plt.savefig(f'Alpha_Hypothesis{h}_Sequence{n}.png')

    return mean_alpha


def expected_beta(h, n, graph=False):
    deck = list(cd.create_random_deck())
    saved_mean_beta = []
    mean_step_sizes = []
    for i in range(5000):
        random.shuffle(deck)
        sequence = cd.create_sequence(h, n, deck)
        # append one every time there is a change
        step_sizes = [abs(sequence[i][0] - sequence[i + 1][0]) % 11 for i in range(len(sequence) - 1)]
        mean_step_sizes.append(np.mean(step_sizes))
        mean_beta = np.mean(mean_step_sizes)
        if i % 1000 == 0:
            saved_mean_beta.append(mean_beta)

    if graph:
        x = range(1, 50000, 1000)
        plt.plot(x, saved_mean_beta)
        plt.title(f'Convergence to Expected Value of Beta: Hypothesis {h} , Sequence {n}')
        plt.xlabel('Number of sequences used')
        plt.ylabel('Mean/Expected Alpha ')
        plt.savefig(f'Beta_Hypothesis{h}_Sequence{n}.png')

    return mean_beta


def get_expected():
    """

    :return: dictionary

    """
    parameters = {}
    n = [5, 10, 15]

    for i in range(len(n)):
        for j in range(1, 4):
            alpha = expected_alpha(j, n[i])
            beta = expected_beta(j, n[i])
            parameters[f'sequence{n[i]}_hypothesis{j}'] = [alpha, beta]

    return parameters


def similarity(sequence, h, wa=1, wb=1):
    """
    defined a simple similarity based model in terms of two intuitively relevant features
    sim(di,dj) = exp(-wa|ai-aj|-wb|b0-bj|
    where di and dj are two different sequeneces and a and be are the expected mean values that a sequence would have
    given a hypothesis
    in this case a is the number of suit changes there are in a sequence and b is the average step size between the
    sequence

    Inputs:
    :param wa: weight given to feature a
    :param wb: weight given to feature b

    Outputs:
    :return:
    """
    changes = [1 for i, x in enumerate(sequence[:-1]) if x[1] != sequence[i + 1][1]]
    alpha = len(changes)
    step_sizes = [abs(sequence[i][0] - sequence[i + 1][0]) % 11 for i in range(len(sequence) - 1)]
    beta = np.mean(step_sizes)
    n = len(sequence)
    params = {'sequence5_hypothesis1': [4.06142, 3.9974], 'sequence5_hypothesis2': [4.00494, 1.0],
              'sequence5_hypothesis3': [1.25234, 4.20725], 'sequence10_hypothesis1': [7.88266, 3.9905777777777782],
              'sequence10_hypothesis2': [7.7474, 1.0], 'sequence10_hypothesis3': [1.62844, 4.220688888888889],
              'sequence15_hypothesis1': [11.70646, 3.9935428571428564], 'sequence15_hypothesis2': [11.48814, 1.0],
              'sequence15_hypothesis3': [2.05504, 4.245242857142856]}

    param = params[f'sequence{n}_hypothesis{h}']

    hyp_alpha = param[0]
    hyp_beta = param[1]

    return exp(-wa * abs(hyp_alpha - alpha) - wb * abs(hyp_beta - beta))


def representativeness_similarity(sequence, wa=1, wb=1):
    sum_sim = similarity(sequence, 1, wa, wb) +  similarity(sequence, 2, wa, wb) +  similarity(sequence, 3, wa, wb)
    sim_h1 = similarity(sequence, 1, wa, wb) / sum_sim
    sim_h2 = similarity(sequence, 2, wa, wb) / sum_sim
    sim_h3 = similarity(sequence, 3, wa, wb) / sum_sim

    return [sim_h1, sim_h2, sim_h3]

deck = list(cd.create_random_deck())
# params = {'sequence5_hypothesis1': [4.06142, 3.9974], 'sequence5_hypothesis2': [4.00494, 1.0], 'sequence5_hypothesis3': [1.25234, 4.20725], 'sequence10_hypothesis1': [7.88266, 3.9905777777777782], 'sequence10_hypothesis2': [7.7474, 1.0], 'sequence10_hypothesis3': [1.62844, 4.220688888888889], 'sequence15_hypothesis1': [11.70646, 3.9935428571428564], 'sequence15_hypothesis2': [11.48814, 1.0], 'sequence15_hypothesis3': [2.05504, 4.245242857142856]}

# sequence = cd.create_sequence(1, 5, deck)
# sim = similarity(sequence,  1)
# print(sim)
