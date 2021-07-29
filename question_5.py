'''
A experiência com trabalhadores de uma certa indústria indica que o
tempo necess ́ario para que um trabalhador, aleatoriamente selecionado, real-
ize uma tarefa  ́e distribuído de maneira aproximadamente normal, com desvio
padrão de 12 minutos. Uma amostra de 25 trabalhadores forneceu x = 140min.
Determine o intervalo de confiança de 95% para a média μ da população de
todos os trabalhadores que fazem aquele determinado serviço.

'''

### algoritmo para intervalos de confiança ###
import pandas as pd # arquivo tStudent.csv necessário para a execução plena do programa

''' entradas alternativas '''
lista = None # amostra em forma de lista
s     = None # valor s
σ2    = None # variância

''' entradas notáveis '''
n     = 25   # tamanho da amostra
x_    = 140 # média amostral
σ     = 12  # desvio padrão

''' entradas obrigatórias '''
c     = 95 # porcentagem de confiança (em porcentagem)
α     = ((100-c)/2)/100 # porcentagem das caudas% (em decimais)

''' variáveis uteis '''
zc    = None

def check_lista (lista,x_,s,n):
	if lista != None :
		return Listax_(lista,temp=0),(Listas2(lista,x_,temp=0) ** (1/2)),len(lista)
	return x_,s,n

def check_desvio (σ,zc,σ2,n,s,α,c):
	if σ == None: ## se desvio padrão desconhecido...

		if σ2 != None:  #... e variância conhecida.
			return σ2 **(1/2),zc(c)

		if n > 30: #... e amostra maior que 30.
			return s, zc (c)

		return s, tϕα (α,ϕ(n)) #... e amostra menor que 30.

	return σ, zc(c) ## se desvio padrão conhecido.

def Listax_ (lista,temp=0):
  for n in lista:
    temp += n
  return temp/len(lista)

def Listas2 (lista,x_,temp=0):
  for n in lista:
    temp += (n - x_)**2
  return ((1/(len(lista)-1))*temp)

def ϕ (n): return n - 1

# para quando há amostra pequena e variância (e desvio) desconhecida
def tϕα (α,ϕ):
	t = pd.read_csv("tStudent.csv")
	w = {t['xxx'][n]:n for n in range(len(t['xxx']))}
	return (t[str(α)][w[ϕ]])

# valores críticos na tabela padrão
def zc (c):
	notable_values = {"90":1.645,"95":1.96,"99":2.576}
	return notable_values[str(c)] 

# margem de erro amostral
def E (c,σ,n,zc):
	return ( zc *  (σ / n**(1/2)) )

# intervalo de confiança
def intervalo_de_confianca_amostral (c,σ,n,x_,zc):
	return (x_-E(c,σ,n,zc) ,x_+E(c,σ,n,zc) )

x_,s,n = check_lista (lista,x_,s,n)
σ,zc = check_desvio (σ,zc,σ2,n,s,α,c)

print ("α = %s" % (α))
print ("ϕ = %s"%ϕ (n))
print ("zc = %f e -zc = -%f."%(zc,zc))
print ("E = %f"%E(c,σ,n,zc))
print ("com %s%s de confiança, sabemos que a média populacional (μ) está entre %.3f e %.3f" % 
	(
		c,
		"%",
		intervalo_de_confianca_amostral (c,σ,n,x_,zc)[0],
		intervalo_de_confianca_amostral (c,σ,n,x_,zc)[1]

	)

)
