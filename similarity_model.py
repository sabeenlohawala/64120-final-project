import numpy as np

def similarity(wa,wb):
    """
    defined a simple similarity based model in terms of two intuitively relevant features
    sim(di,dj) = exp(-wa|ai-aj|-wb|b0-bj|
    where di and dj are two different sequeneces and a and be are the expected mean values that a sequence would have
    given a hypothesis

    Inputs:
    :param wa: weight given to feature a
    :param wb: weight given to feature b

    Outputs:
    :return:
    """
