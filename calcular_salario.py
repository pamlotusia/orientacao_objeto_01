# Exercício 05
# Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o salário com um reajuste de aumento, sendo que:
# Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
# Caso contrário, o funcionário receberá 15% de aumento.
# _______________________________________________________________________________
def calcular_salario(a):
  if(a > 2000):
    reajuste = a*(7/100) + a
  else:
    reajuste = a*(10/100) + a
  return reajuste

a=float(input("digite seu salario: "))
print(calcular_salario(a))