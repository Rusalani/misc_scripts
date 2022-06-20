import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats

def get_imputed_corr(df, nrounds = 4):
    '''

    :param df:
    :param nrounds:
    :return:
    '''
    #print(df.isnull().sum())
    dfm = df.copy()
    df_all = np.zeros(df.shape)
    for i in range(nrounds):
        df=dfm.copy()
        #df.loc[dfm.Y1.isna(), 'Y1'] = np.nan
        y1 = smf.ols('Y1 ~ X1+X2', data=df).fit()
        dof = y1.nobs - 3
        u = stats.chi2(dof).rvs()
        sigma_star = np.sqrt(y1.ssr / u)
        L = np.linalg.cholesky(y1.normalized_cov_params * sigma_star ** 2)
        beta_star1 = y1.params + sigma_star * L @ stats.norm([0, 0,0]).rvs()
        y1.params[:] = beta_star1
        df.loc[dfm.Y1.isna(), 'Y1'] = y1.predict(df.loc[dfm.Y1.isna(), ['X1','X2']])

        #df.loc[dfm.Y2.isna(), 'Y2'] = np.nan
        y2 = smf.ols('Y2 ~ Y1+X1+X2', data=df).fit()
        dof = y2.nobs -4
        u = stats.chi2(dof).rvs()
        sigma_star = np.sqrt(y2.ssr / u)
        L = np.linalg.cholesky(y2.normalized_cov_params * sigma_star ** 2)
        beta_star = y2.params + sigma_star * L @ stats.norm([0, 0, 0,0]).rvs()
        y2.params[:] = beta_star
        df.loc[dfm.Y2.isna(), 'Y2'] = y2.predict(df.loc[dfm.Y2.isna(), ['X1', 'X2','Y1']])

        #df.loc[dfm.Y3.isna(), 'Y3'] = np.nan
        y3 = smf.ols('Y3 ~ Y2+Y1+X1+X2', data=df).fit()
        dof = y3.nobs - 5
        u = stats.chi2(dof).rvs()
        sigma_star = np.sqrt(y3.ssr / u)
        L = np.linalg.cholesky(y3.normalized_cov_params * sigma_star ** 2)
        beta_star = y3.params + sigma_star * L @ stats.norm([0, 0, 0, 0,0]).rvs()
        y3.params[:] = beta_star
        df.loc[dfm.Y3.isna(), 'Y3'] = y3.predict(df.loc[dfm.Y3.isna(), ['X1', 'X2', 'Y1','Y2']])

        #df.loc[dfm.Y4.isna(), 'Y4'] = np.nan
        y4 = smf.ols('Y4 ~ Y3+Y2+Y1+X1+X2', data=df).fit()
        dof = y4.nobs - 6
        u = stats.chi2(dof).rvs()
        sigma_star = np.sqrt(y4.ssr / u)
        L = np.linalg.cholesky(y4.normalized_cov_params * sigma_star ** 2)
        beta_star = y4.params + sigma_star * L @ stats.norm([0,0, 0, 0, 0, 0]).rvs()
        y4.params[:] = beta_star
        df.loc[dfm.Y4.isna(), 'Y4'] = y4.predict(df.loc[dfm.Y4.isna(), ['X1', 'X2', 'Y1','Y2','Y3']])
        df_all += df



        #print(temp)

    fin_df = df_all / nrounds
    return fin_df.corr()
'''
df = pd.read_csv('missing_irish_wind.csv')
#hold2 = df.loc['Y3':'Y4','X1':'X2']
hold = get_imputed_corr(df,10)
temp  =hold.loc['Y3':'Y4','X1':'X2']

print(temp)
'''

#ans .791 .627
#    .840 .757