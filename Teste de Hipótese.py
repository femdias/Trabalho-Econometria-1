'''Teste de Hipótese:
Ho: Bj=0
H1: Bj != 0'''


'''Zj = (Bj - 0)/erro padrão'''

'''https://towardsdatascience.com/verifying-the-assumptions-of-linear-regression-in-python-and-r-f4cd2907d4c0'''

import statsmodels.api as sm


X2=X+Beta0

ols = sm.OLS(Y, X2)
ols_result = ols.fit()
ols_result.summary()









