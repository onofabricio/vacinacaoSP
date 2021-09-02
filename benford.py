from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math

def extrair_primeiro_digito (numero_str):
	return numero_str[0]


def frequencia_digitos (coluna):

  coluna = coluna.astype(str).apply(extrair_primeiro_digito)
  coluna = coluna.loc[coluna != '0']
  coluna = coluna.value_counts(normalize=True)
  
  return coluna
  
def criar_regua_benford():
  regua_benford = [ math.log10(1 + 1/digito) for digito in range(1, 10) ]
  return regua_benford
  

def benford(coluna):
  
  df_benford['benford']= criar_regua_benford()
  df_benford['Vacinometro'] = frequencia_digitos(coluna)
  df_benford.plot.bar()
  plt.show()



#DataBase
end_vacinometro = 'https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/09/20210902_vacinometro.csv'
df_vacinometro = pd.read_csv(end_vacinometro, index_col=0)
df_benford = pd.DataFrame(index=[str(i) for i in range(1, 10)])


#MAIN
print(benford(df_vacinometro['Total Doses Aplicadas']))


