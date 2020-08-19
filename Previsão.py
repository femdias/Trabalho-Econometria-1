
Base0 = pd.read_excel(r'C:\Users\femdi\OneDrive\Documentos\FEA-USP\Econometria 1\Tema 11 - Salários de CEOs.xlsx')
valor=(Base0['ros'])/(Base0['roe'])
sal_relativ=(Base0['pcsalary'])/(Base0['pcroe'])

ros1=(Base0['ros'])-np.mean(Base0['ros'])
roe1=(Base0['roe'])-np.mean(Base0['roe'])
lsales1=(Base0['lsales'])-np.mean(Base0['lsales'])
indus1=(Base0['indus'])-np.mean(Base0['indus'])
finance1=(Base0['finance'])-np.mean(Base0['finance'])
consprod1=(Base0['consprod'])-np.mean(Base0['consprod'])
valor1=valor-np.mean(valor)
sal_relativ1=sal_relativ-np.mean(sal_relativ)


sal_relativ=(Base0['pcsalary'])/(Base0['pcroe'])
base=Base0.assign(pcsalaryvalor_pcroe=valor,sal_relativ=sal_relativ)

# o '~' separa o y do x, e o '+' adiciona variaveis expicativas para o x
Y,X = dmatrices('lsalary ~  lsales1 + roe1 + ros1 + indus1 + finance1 + consprod1 + valor1 + sal_relativ1', data=base, return_type='dataframe')
model = sm.OLS(Y,X)
fit = model.fit()
fit.summary()

xxxx=base.describe()
