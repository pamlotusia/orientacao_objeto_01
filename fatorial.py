# Exercício 07
# Implemente a função fatorial que recebe um número positivo e retorna o fatorial desse número.
# O fatorial de um número N é o produto dos números naturais consecutivos de 1 até N.

# Por exemplo:
# - O fatorial de 5 é 120 (1 * 2 * 3 * 4 * 5)
# - O fatorial de 10 é 3628800 (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)
#_____________________________________________________________________________________

def fatorial(a):
  cont=1
  for i in range(1, a+1):
    cont= cont*i
  return cont

a=int(input("digite um valor: "))
print(fatorial(a))
