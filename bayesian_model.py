import likelihood_model as lm
import numpy as np

def calculate_bayes_logs(d, prior_h1=1/3, prior_h2=1/3):
    """
    Calculates the Bayesian analysis for hypothesis 1
    h1 = the deck is completely shuffled

    Inputs
    ------
    :param d: a list of lenght-2 lists, each of which represents a card, where the first index is a numerical
        value (where A = 1, J = 11, Q = 12, K = 13) and the second is the string of the suit (i.e. 'C', 'D', 'H', 'S')

    :param prior_h1: The prior probability of hypothesis 1 being true
    :param prior_h2: The prior probability of hypothesis 2 being true
    :param prior_h3: The prior probability of hypothesis 3 being true

    Returns
    ------
    :return:s: a list containing the bayesian for all 3 possible hypotheses in the order [P(h1|d), P(h2|d), P(h3|d)]
    """
    prior_h3 = 1 - (prior_h1 + prior_h2)
    likelihood_h1 = lm.calculate_likelihood(d)[0]
    likelihood_h2 = lm.calculate_likelihood(d)[1]
    likelihood_h3 = lm.calculate_likelihood(d)[2]
    bayes_h1 = (np.log(likelihood_h1) if likelihood_h1 != 0 else 0) + (np.log(1-prior_h1) if 1-prior_h1 != 0 else 0) - (np.log(likelihood_h2 * prior_h2 + likelihood_h3 * prior_h3) if (likelihood_h2 * prior_h2 + likelihood_h3 * prior_h3 != 0) else 0)
    bayes_h2 = (np.log(likelihood_h2) if likelihood_h2 != 0 else 0) + (np.log(1-prior_h2) if 1-prior_h2 != 0 else 0) - (np.log(likelihood_h1 * prior_h1 + likelihood_h3 * prior_h3) if (likelihood_h1 * prior_h1 + likelihood_h3 * prior_h3 != 0) else 0)
    bayes_h3 = (np.log(likelihood_h3) if likelihood_h3 != 0 else 0) + (np.log(1-prior_h3) if 1-prior_h3 != 0 else 0) - (np.log(likelihood_h2 * prior_h2 + likelihood_h1 * prior_h1) if (likelihood_h2 * prior_h2 + likelihood_h1 * prior_h1 != 0) else 0)

    return [bayes_h1, bayes_h2, bayes_h3]


def calculate_bayes_old(d, prior_h1=1/3, prior_h2=1/3):
    """
    Calculates the Bayesian analysis for hypothesis 1
    h1 = the deck is completely shuffled

    Inputs
    ------
    :param d: a list of lenght-2 lists, each of which represents a card, where the first index is a numerical
        value (where A = 1, J = 11, Q = 12, K = 13) and the second is the string of the suit (i.e. 'C', 'D', 'H', 'S')

    :param prior_h1: The prior probability of hypothesis 1 being true
    :param prior_h2: The prior probability of hypothesis 2 being true
    :param prior_h3: The prior probability of hypothesis 3 being true

    Returns
    ------
    :return:s: a list containing the bayesian for all 3 possible hypotheses in the order [P(h1|d), P(h2|d), P(h3|d)]
    """
    prior_h3 = 1 - (prior_h1 + prior_h2)
    likelihood_h1 = lm.calculate_likelihood(d)[0]
    likelihood_h2 = lm.calculate_likelihood(d)[1]
    likelihood_h3 = lm.calculate_likelihood(d)[2]
    bayes_h1 = np.log(likelihood_h1 / (likelihood_h2 * (prior_h2 / (1 - prior_h1)) + likelihood_h3 * (prior_h3 / (1 - prior_h1))))
    bayes_h2 = np.log(likelihood_h2 / (likelihood_h1 * (prior_h1 / (1 - prior_h2)) + likelihood_h3 * (prior_h3 / (1 - prior_h2))))
    bayes_h3 = np.log(likelihood_h3 / (likelihood_h2 * (prior_h2 / (1 - prior_h3)) + likelihood_h1 * (prior_h1 / (1 - prior_h3))))

    return [bayes_h1, bayes_h2, bayes_h3]

def calculate_bayes(d, prior_h1 = 1/3, prior_h2 = 1/3):
    prior_h3 = 1 - (prior_h1 + prior_h2)
    likelihood_h1 = lm.calculate_likelihood(d)[0]
    likelihood_h2 = lm.calculate_likelihood(d)[1]
    likelihood_h3 = lm.calculate_likelihood(d)[2]
    # print(likelihood_h1, likelihood_h2, likelihood_h3)
    bayes_h1 = (likelihood_h1 * (1-prior_h1) / (likelihood_h2 * prior_h2 + likelihood_h3 * prior_h3)) if likelihood_h2 * prior_h2 + likelihood_h3 * prior_h3 != 0 else 0
    bayes_h2 = (likelihood_h2 * (1-prior_h2) / (likelihood_h1 * prior_h1 + likelihood_h3 * prior_h3)) if likelihood_h1 * prior_h1 + likelihood_h3 * prior_h3 != 0 else 0
    bayes_h3 = (likelihood_h3 * (1-prior_h3) / (likelihood_h1 * prior_h1 + likelihood_h2 * prior_h2)) if likelihood_h1 * prior_h1 + likelihood_h2 * prior_h2 != 0 else 0
    return [bayes_h1, bayes_h2, bayes_h3]