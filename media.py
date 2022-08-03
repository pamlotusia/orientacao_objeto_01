# Exercício 04
# Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos valores.
# _______________________________________________________________________________
from re import X


def media(a,b,c):
  x = (a+b+c)/3
  return x

a=int(input("digite um valor: "))
b=int(input("digite um valor: "))
c=int(input("digite um valor: "))

print(media(a,b,c))