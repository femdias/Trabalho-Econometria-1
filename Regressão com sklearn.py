import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

Base0 = pd.read_excel(r'C:\Users\femdi\OneDrive\Documentos\FEA-USP\Econometria 1\Tema 11 - Salários de CEOs.xlsx')


Nome_coluna = list(Base0.columns)
X = Base0[['ros','sales']] # values transforma a pandas series em numpy array
Y = Base0['salary'] # reshape(linhas, colunas) redimensiona a array (apenas 1 dimensão, linhas),\
                                      # o -1 significa que o número de linhas continua o mesmo e o 1 significa que\
                                      # agora o número de colunas
print(X)
Regressão = LinearRegression().fit(X,Y)

Y_pred = Regressão.predict(X)

Rquadrado = float(Regressão.score(X, Y)) # Valor do R²


Beta1 = (Regressão.coef_)   # Valor do Coeficiente (Beta 1)
print(Beta1[0])

Beta0 = float(Regressão.intercept_) # Valor do Intercepto (Beta 0)

Eq = 'y = {} + {}*x +{}*x;  R²={} '.format(round(Beta0,3), round(float(Beta1[0]),3),  round(float(Beta1[1]),3), round(Rquadrado,4))


print(Eq)