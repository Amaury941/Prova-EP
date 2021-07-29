'''
Segundo um radar, as velocidades de 15 carros numa perimetral de São Paulo 
no início de uma noite foram: 
77, 69, 82, 76, 69, 80, 66, 70, 77, 72, 73, 80, 86, 77 e 89 quilõmetros por hora.
sendo 3 o número de classes:
'''

### from x.py import x

n_classes = 3
dados = [77, 69, 82, 76, 69, 80, 66, 70, 77, 72, 73, 80, 86, 77, 89]

''' 1 '''
def string_frequencies(limites,dados):
    print ('frequências')
    x = [min(dados)]+list(limites)
    for n in range(1,len(x)):
        print ('%i-%i : %i'%(x[n-1],x[n]-1,limites[ (x[n]) ]))

def string_Relatives_frequencies(limites,dados):
    print ('frequências relativas')
    x = [min(dados)]+list(limites)
    for n in range(1,len(x)):
        print ('%i-%i : %.3f%s'%(x[n-1],x[n]-1,(limites[ (x[n]) ]/len(dados))*100,'%' ))

'''   '''

''' 2 '''
def calcular_moda(lista,temp='',temp0=0):
	moda = [0,0]
	for n in lista:
		frequência = 0
		for m in lista:
			if n == m:
				frequência += 1
		if frequência > moda[1]:
			moda = [n,frequência]
	return moda[0] 

def calcular_media(lista): return sum(lista)/len(lista)

def calcular_mediana(listaS):
    if len(listaS)%2 == 0:
      mediana = (listaS[int(len(listaS)/2-1)] + listaS[int(len(listaS)/2)])/2
    else:
      mediana = listaS[int(len(listaS)/2-1)]
    return mediana

''' 2 '''

''' 3 '''
def amplitude_dados(dados):  return max(dados) - min(dados)

def amplitude_classe(amplitude_dados,n_classes): return round(amplitude_dados/n_classes)

def definir_limites(dados,n_classes,amplitude_classe):
    limites = {str(min(dados)):0}
    for i in range(n_classes):
        limites.update({int(list(limites)[i])+amplitude_classe:0})
    del limites[str(min(dados))]
    return limites

def fill (data,limites,n=0):
    if data < int(list(limites)[n]):
        limites[list(limites)[n]] += 1
        return limites
    if n+1<len(limites):
        fill (data,limites,n+1)

def fill_limits(limites,dados):
    for data in dados:
        fill(data,limites)

def calcular_amplitude (maior,menor,n_classes): return (maior - menor)

def calcular_variancia(lista,var=0):
  media =calcular_media(lista)
  for numero in lista:
    var += (numero - media)**2
  var = var/len(lista)
  return var

def calcular_desvio_padrão(lista):
    return calcular_variancia(lista)**(1/2)

'''  '''

limites = definir_limites(dados,n_classes,amplitude_classe(amplitude_dados(dados),n_classes))
fill_limits(limites,dados)


#1 - Construa a tabela de frequência para o conjunto de dados, sendo 3 o número de classes
print ('1_______________________________')
string_frequencies(limites,dados)
string_Relatives_frequencies(limites,dados)

# 2 - Encontre a média, a mediana e a moda dos dados.
print ('2_______________________________')
print('média:'  ,calcular_media  (dados))
print('mediana:',calcular_mediana(dados))
print('moda:'   ,calcular_moda   (dados))

# 3 - Encontre a amplitude, a variˆancia e o desvio padr ̃ao do conjunto.
print ('3_______________________________')
print('amplitude:',calcular_amplitude (max(dados),min(dados),n_classes))
print('variância:',calcular_variancia (dados))
print ('desvio:',calcular_desvio_padrão(dados))

print ('end_____________________________')
