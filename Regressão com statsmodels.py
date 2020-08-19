import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from patsy import dmatrices

Base0 = pd.read_excel(r'C:\Users\femdi\OneDrive\Documentos\FEA-USP\Econometria 1\Tema 11 - Salários de CEOs.xlsx')
valor=(Base0['ros'])/(Base0['roe'])
sal_relativ=(Base0['pcsalary'])/(Base0['pcroe'])
base=Base0.assign(pcsalaryvalor_pcroe=valor,sal_relativ=sal_relativ)

# o '~' separa o y do x, e o '+' adiciona variaveis expicativas para o x
Y,X = dmatrices('lsalary ~  lsales + roe + ros + indus + finance + consprod ', data=base, return_type='dataframe')

#X=X.drop(columns=['Intercept'])

model = sm.OLS(Y,X)
fit = model.fit()
fit.summary()


a=u2
b=base['lsalary']
plt.scatter(b,a)
plt.show()

ychapeu = fit.predict(X)
u = fit.resid
u2= u*u




média_condicional_dos_erros= fit.resid.mean()
print(média_condicional_dos_erros)



import seaborn as sns

sns.heatmap(base.corr(), annot=True, vmin=-1, vmax=1)
plt.show()


