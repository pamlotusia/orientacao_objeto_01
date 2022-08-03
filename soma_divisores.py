# Exercício 06
# Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo e retorna a soma de todos os divisores desse número.

# Por exemplo:
# caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
# caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)
# _______________________________________________________________________________
def soma_divisores(a):
  soma= 0
  for i in range(1, a+1):
    if (a % i == 0):
      soma+=i
  return soma

a= int(input("digite um valor: "))
print(soma_divisores(a))