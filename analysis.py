import pandas as pd
import numpy as np
import likelihood_model as lm
import Bayesian_model as bm

def get_series_cards(i, series_cards_values, series_cards_suits):
    """
    Gets the card values in series_cards_values and the card suits in series_cards_suits and formats
    the cards data for series i as (value, suit) for each card in that series.
    """
    return [(series_cards_values['series'+str(i)][j],series_cards_suits['series'+str(i)][j]) for j in range(series_cards_values['series'+str(i)].count())]

def get_series_means(i, responses_df):
    """
    Gets the mean of the google form responses for series i from the responses_df.
    """
    return [responses_df['series'+str(i)+'_h'+str(j)].mean() for j in range(1,4)]

def get_series_modes(i,responses_df):
    """
    Gets the mode of the google form responses for series i from the responses_df.
    """
    return [responses_df['series'+str(i)+'_h'+str(j)].mode().to_numpy()[0] for j in range(1,4)]

def build_series_info(all_responses_filename, cards_values_filename, cards_suits_filename):
    """
    Builds the series_info dict formatted as:
    {'seriesi': {
        'cards': [(value,suit)] array from get_series_cards,
        'mean': [mean_h1, mean_h2, mean_h3] from get_series_means,
        'mode': [mode_h1, mode_h2, mode_h3] from get_series_modes,
        'likelihood': [likelihood_h1, likelihood_h2, likelihood_h3] from likelihood_model.py,
        'bayesian': [bayes_h1, bayes_h2, bayes_h3] from Bayesian_model.py
    }}
    """
    responses_df = pd.read_csv(all_responses_filename)
    series_cards_values = pd.read_csv(cards_values_filename)
    series_cards_suits = pd.read_csv(cards_suits_filename)

    series_info = {}
    for i in range(1,10):
        series_dict = {'cards':[],'mean':[],'mode':[],'likelihood':[],'bayesian':[]}
        series_dict['cards'] = get_series_cards(i, series_cards_values, series_cards_suits)
        series_dict['mean'] = get_series_means(i, responses_df)
        series_dict['mode'] = get_series_modes(i, responses_df)
        series_dict['likelihood'] = lm.calculate_likelihood(series_dict['cards'])
        series_dict['bayes_equal_priors'] = bm.calculate_bayes_logs(series_dict['cards'])
        series_info['series'+str(i)] = series_dict
    return series_info

def optimize_bayes_corrcoef(series_info,num_steps=10,mean_or_mode='mean'): # optimize average corrcoef
    """
    Finds the prior_h1 and prior_h2 settings that result in the maximum avg corrcoef for the three hypotheses.

    Inputs
    ------
    The dictionary containing the information for all of the nine series as built by the build_seris_info function.

    Returns
    ------ 
    The maximum average corrcoef and prior_h1 and prior_h2 that correspond with that, where the priors are found by
    iterating over the range 0 to 1 in 1/num_step size steps.
    """
    mean_h1,mean_h2,mean_h3 = [[series[mean_or_mode][i] for series in series_info.values()] for i in range(3)]
    max_corrcoef = -float('inf')
    max_p1 = None
    max_p2 = None

    for p1 in [i/num_steps for i in range(0,num_steps + 1)]:
        for p2 in [i/num_steps for i in range(0,num_steps + 1)]:
            if p1 + p2 <= 1:
                # print(p1,p2)
                all_bayes = [bm.calculate_bayes(series_info[key]['cards'],p1,p2) for key in series_info.keys()]
                bayes_h1 = [arr[0] for arr in all_bayes]
                bayes_h2 = [arr[1] for arr in all_bayes]
                bayes_h3 = [arr[2] for arr in all_bayes]

                corr_h1 = np.corrcoef(mean_h1,bayes_h1)[0][1]
                corr_h2 = np.corrcoef(mean_h2,bayes_h2)[0][1]
                corr_h3 = np.corrcoef(mean_h3,bayes_h3)[0][1]
                avg_corr = (corr_h1 + corr_h2 + corr_h3) / 3
                if not max_p1 or not max_p2 or avg_corr > max_corrcoef:
                    max_corrcoef = avg_corr
                    max_p1 = p1
                    max_p2 = p2
    return max_corrcoef, max_p1, max_p2

def calculate_likelihood_corrcoef(series_info,mean_or_mode='mean'):
    """
    Finds the corrcoef of the human data compared to the likelihood model.

    Inputs
    ------
    The dictionary containing the information for all of the nine series as built by the build_seris_info function.

    Returns
    ------
    The average corrcoef of the three hypotheses when comparing the likelihood model to human data.
    """
    mean_h1,mean_h2,mean_h3 = [[series[mean_or_mode][i] for key,series in series_info.items()] for i in range(3)]
    likelihood_h1,likelihood_h2,likelihood_h3 = [[series['likelihood'][0] for key,series in series_info.items()] for i in range(3)]
    return (np.corrcoef(mean_h1,likelihood_h1)[0][1] + np.corrcoef(mean_h2,likelihood_h2)[0][1] + np.corrcoef(mean_h3,likelihood_h3)[0][1])/3

def main():
    series_info = build_series_info('./data/google_form_responses.csv','./data/series_cards_values.csv','./data/series_cards_suits.csv')
    likelihood_corrcoef = calculate_likelihood_corrcoef(series_info,'mean')
    max_bayes_corrcoef, max_p1, max_p2 = optimize_bayes_corrcoef(series_info,10,'mean')
    print('mean')
    print(likelihood_corrcoef)
    print(max_bayes_corrcoef, max_p1, max_p2)

    print('mode')
    likelihood_corrcoef = calculate_likelihood_corrcoef(series_info,'mode')
    max_bayes_corrcoef, max_p1, max_p2 = optimize_bayes_corrcoef(series_info,10,'mode')
    print(likelihood_corrcoef)
    print(max_bayes_corrcoef, max_p1, max_p2)

if __name__ == "__main__":
    main()
