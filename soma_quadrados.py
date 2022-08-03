# Exercício 03
# Implemente a função soma_dos_quadrados que receba dois numeros e devolve a soma dos seus quadrados.
# Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação.
# _______________________________________________________________________________
def quadrado(a):
  x = a**2
  return x

def soma_quadrado(a,b):
  x = quadrado(a) + quadrado(b)
  return x

a=int(input("digite um valor: "))  
b=int(input("digite um valor: "))  

print(soma_quadrado(a,b))
