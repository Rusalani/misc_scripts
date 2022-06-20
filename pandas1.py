import pandas as pd

def split_count (z):
    '''

    :param z:
    :return:
    '''
    assert isinstance(z,pd.Series)
    z = z.str.split(', ',expand=True)
    l=[]
    for x in range(z.shape[1]):
        l.append(z[x].value_counts())

    temp7 = pd.concat(l).to_frame()
    temp7.columns = ['count']
    temp7['label'] = list(temp7.axes[0])
    final = temp7.groupby(['label']).sum()
    final = final.sort_values(by='count',ascending=True)
    return final



'''
x = pd.read_csv('survey_data.csv')
x=x['Is there anything in particular you want to use Python for?']
split_count(x)
'''
