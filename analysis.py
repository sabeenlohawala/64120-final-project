import pandas as pd
import numpy as np
import likelihood_model as lm
import Bayesian_model as bm

def get_series_cards(i, series_cards_values, series_cards_suits):
    return [(series_cards_values['series'+str(i)][j],series_cards_suits['series'+str(i)][j]) for j in range(series_cards_values['series'+str(i)].count())]

def get_series_means(i, responses_df):
    return [responses_df['series'+str(i)+'_h'+str(j)].mean() for j in range(1,4)]

def get_series_modes(i,responses_df):
    return [responses_df['series'+str(i)+'_h'+str(j)].mode().to_numpy()[0] for j in range(1,4)]

def build_series_info(all_responses_filename, cards_values_filename, cards_suits_filename):
    responses_df = pd.read_csv(all_responses_filename)
    series_cards_values = pd.read_csv(cards_values_filename)
    series_cards_suits = pd.read_csv(cards_suits_filename)

    series_info = {}
    for i in range(1,10):
        series_dict = {'cards':[],'mean':[],'mode':[],'likelihood':[],'bayesian':[]}
        series_dict['cards'] = get_series_cards(i, series_cards_values, series_cards_suits)
        series_dict['mean'] = get_series_means(i, responses_df)
        series_dict['mode'] = get_series_modes(i, responses_df)
        series_dict['likelihood'] = lm.calc_log_likelihood_all(series_dict['cards'])
        series_dict['bayesian'] = bm.calculate_bayes_logs(series_dict['cards'])
        series_info['series'+str(i)] = series_dict
    return series_info

series_info = build_series_info('./data/google_form_responses.csv','./data/series_cards_values.csv','./data/series_cards_suits.csv')
for key,val in series_info.items():
    print(key)
    print(val)
    print()
