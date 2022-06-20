import pandas as pd
import numpy as np

def get_odds_ratio_overall():
    '''

    :return:
    '''
    #df={'Smoke':[2/55,3/124,14/109,27/130,51/115,29/36,13/13],'No Smoke':[1/62,5/157,7/121,12/78,40/121]}
    df={'Smoke':[139/582,1-139/582],
        'No Smoke':[230/732,1-230/732]}

    return (139/443) / (230/502)

def get_odds_ratio_by_age():
    '''

    :return:
    '''
    result = {
        '18-24': (2/53)/(1/61),
        '25-34': (3/121)/(5/152),
        '35-44': (14/95)/(7/114),
        '45-54': (27/103)/(12/62),
        '55-64': (51/64)/(40/81),
        '65-74': (29/7)/(101/28)

    }

    return result
#print(get_odds_ratio_by_age())
#print((2/53)/(1/61))