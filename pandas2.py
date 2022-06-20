import pandas as pd

def add_month_yr (z):
    '''

    :param z:
    :return:
    '''
    assert isinstance(z,pd.DataFrame)
    z[['month','day','year']] = z['Timestamp'].str.split('/', expand=True)
    z[['year','time']] = z['year'].str.split(' ', expand=True)
    z['month'] = z['month'].map({'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'})

    z['month-yr'] = z['month'] + '-'+z['year']
    z.drop('day', axis=1, inplace=True)
    z.drop('time', axis=1, inplace=True)
    z.drop('year', axis=1, inplace=True)
    z.drop('month', axis=1, inplace=True)
    return z


def count_month_yr(x):
    '''

    :param x:
    :return:
    '''
    assert isinstance(x, pd.DataFrame)
    x=x['month-yr']
    x=x.value_counts().to_frame()
    return x
def fix_categorical(z):
    assert isinstance(z, pd.DataFrame)
    #temp = x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()

    x = z['month-yr']
    x = x.value_counts().to_frame()
    x.index = pd.to_datetime(x.index)
    x.sort_index(inplace=True)
    # pd.Categorical
    x.index = pd.Categorical(x.index)
    x.columns=['Timestamp']
    x['label'] = list(x.axes[0])
    x[['year', 'month', 'day']] = x['label'].dt.strftime('%Y-%m-%d').str.split('-', expand=True)

    x['month'] = x['month'].map(
        {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep',
         '10': 'Oct', '11': 'Nov', '12': 'Dec'})

    x['month-yr'] =  (x['month'] + '-' + x['year'])

    x.drop('year', axis=1, inplace=True)
    x.drop('month', axis=1, inplace=True)
    x.drop('day', axis=1, inplace=True)
    x.drop('label',axis=1,inplace=True)
    x.set_axis(x['month-yr'], axis='index',inplace=True)
    x.drop('month-yr',axis=1,inplace=True)

    temp = pd.CategoricalDtype(list(x.index),ordered=True)



    type = pd.CategoricalDtype(list(x.index),ordered=True)
    z=z.astype({'month-yr':type})

    return z

'''
x = pd.read_csv('survey_data.csv')
x = add_month_yr(x)
x = fix_categorical(x)
print(x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index() )
'''





