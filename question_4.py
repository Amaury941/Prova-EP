'''
Um fabricante de máquinas de lavar sabe, por longa experiência, que a
dura ̧c ̃ao de suas m ́aquinas tem dura ̧c ̃ao normal com média de 1000 dias e desvio
padrão de 200 dias. Oferece uma garantia de 365 dias. Produz mensalmente
2000 maquinas. Quantas espera trocar pelo uso da garantia dada, mensalmente?

'''

''' algoritmo para distribuições de probabilidades contínuas '''

# seja X: N(μ,σ2) e σ == σ2**(1/2) 
μ  = 1000
σ2 = None
σ  = 200#σ2**(1/2)

# seja P(x1<X<x2) == P(z1<Z<z2)
x1,x2 = 365,None
z1,z2 = None,None

import pandas as pd # arquivo tabelaZ.csv necessário para a execução plena do programa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def printar_grafico(media,desvio,x1,x2,quantidade=1000):
  numeros = np.random.normal(media,desvio,quantidade)
  #print ('média da amostra do gráfico:',numeros.mean())
  #print ('desvio padrão da amostra do gráfico:',numeros.std())
  graph = sns.displot(
  	data=numeros, 
  	kind="kde",
  	height=4, 
  	aspect=1.3,
  )
  plt.axvline(media,color='k')
  plt.title("gráfico da distribuição normal")
  if x1!=None:
  	plt.axvline(x1,color='r',linestyle=':')
  if x2!=None:
  	plt.axvline(x2,color='r',linestyle=':')
  plt.show()

def valor_z(x,μ,σ): return float('%.3f'%((x-μ)/σ))

def z1_z2 (fz):
	fz1 = int('%i'%(fz*10))
	return fz1/10,((float('%.2f'%((fz1-fz*10)/10)))**2)**(1/2)

def area_acumulada (Z1,Z2):
	t = pd.read_csv("tabelaZ.csv")
	w = {t['Z'][n]:n for n in range(len(t['Z']))}
	return float ('%f'% t[('%.2f'% (Z2))] [w[Z1] ])

def determinar_probabilidade (z):
	z_value = (z1_z2(z))
	return area_acumulada(z_value[0],z_value[1])	

def menor_e_maior (var1,var2):
	if var1 < var2:
		return var1,var2
	return var2,var1

def calcular_probabilidades_P(μ,σ,x1=None,z1=None,x2=None,z2=None):
	if z1 == z2 and z1 == None:
		if x1 != None and x2 != None:
			ordem = menor_e_maior (
				determinar_probabilidade (valor_z(x1,μ,σ)),
				determinar_probabilidade (valor_z(x2,μ,σ)),
			),
			print ('estilo n < x < n')
			return ('P(%s < x < %s) = P(%s < Z < %s) = %f - %f = %f'%
				(
					x1,
					x2,
					valor_z(x1,μ,σ),
					valor_z(x2,μ,σ),
					ordem[0][1],
					ordem[0][0],
					ordem[0][1]-ordem[0][0]
				)	
			)
		if x1 == None:
			print ('estilo x < n')
			return ('P(x < %s) = P(Z < %s) = %f - %f = %f'%
				(
					x2,
					valor_z(x2,μ,σ),
					1,
					determinar_probabilidade (valor_z(x2,μ,σ)),
					1 - determinar_probabilidade (valor_z(x2,μ,σ)),
				)
			)
		if x2 == None:
			print ('estilo n < x')
			return ('P(%s < x) = P(%s < Z) = %f = %f%s'%
				(
					x1,
					valor_z(x1,μ,σ),
					determinar_probabilidade (valor_z(x1,μ,σ)),
					determinar_probabilidade (valor_z(x1,μ,σ))*100,
					'%',
				)
			)

	if z1 != None and z2 != None:
		ordem = menor_e_maior (
			determinar_probabilidade (z1),
			determinar_probabilidade (z2),
		),
		print ('estilo n < z < n')
		return ('P(%s < z < %s) =  %f - %f = %f'%
			(
				z1,
				z2,
				ordem[0][1],
				ordem[0][0],
				ordem[0][1]-ordem[0][0]
			)
		)
	if z1 == None:
		print ('estilo z < n')
		return ('P(z < %s) = %f - %f = %f'%
			(
				z2,
				1,
				determinar_probabilidade (z2),
				1 - determinar_probabilidade (z2),
			)
		)
	if z2 == None:
		print ('estilo n < z')
		return ('P(%f < z) = %f = %f%c' % 
			(
				z1,
				determinar_probabilidade (z1),
				(determinar_probabilidade (z1))*100,
				'%',
			)
		)

print (calcular_probabilidades_P(μ,σ,x1,z1,x2,z2))

#caso estejamos trabalhando com variáveis x
printar_grafico(μ,σ,x1,x2,quantidade=2000)