'''
Um estudo feito em uma determinada região apontou que a probabilidade
de os pais terem um filho com cabelo loiro foi de 1/4. Se houverem 6 crianças
em uma família dessa região, qual a probabilidade de que 2 delas tenha cabelo
loiro?
'''

x = 2    # valor a ser buscado
n = 6    #frequência das ocorrências

#distribuição de bernoulli
p  = 1/4 #probabilidade de sucesso
q  = 1-p #probabilidade de falha
s2 = p*q # variância VAR(X)
x_ = p   # Média E(x)

''' algoritmo para distribuições de probabilidades Discretas  '''

def fatorial(num,fatorial=1):
	if num == 0: num = 1
	for n in range (num):
		fatorial = fatorial * (n+1)
	return fatorial

def probabilidade_binomial (n,p,q,x):
	return (fatorial(n)/(fatorial(n-x)*fatorial(x)))*(p**x)*(q**(n-x))

print('tem %.3f%s de chance que %i de %i crianças nascerem galegas.'%(probabilidade_binomial(n,p,q,x)*100,"%",x,n))