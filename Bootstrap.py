import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from patsy import dmatrices

Base0 = pd.read_excel(r'C:\Users\femdi\OneDrive\Documentos\FEA-USP\Econometria 1\Tema 11 - Salários de CEOs.xlsx')
salary_sales=Base0['salary']/Base0['sales']
base=Base0.assign(salary_sales=salary_sales)

from resample.bootstrap import bootstrap
from tqdm import tqdm
import time


betas0 = []
for i in tqdm(np.arange(1000)):
    base_sample = base.sample(frac = 1, replace = True)
    Y,X = dmatrices('lsalary ~  lsales + roe + ros + indus + finance + utility', data=base_sample, return_type='dataframe')
    model = sm.OLS(Y,X)
    fit = model.fit()
    coef= fit.params[1]
    betas0 = np.append(betas0,coef)
    time.sleep(1)
print(np.mean(betas0))


boot_coef = bootstrap(a=base.join(Y).values, f=bootstrap_teste, b=5000)
