#Sequencia de Fibonacci em Python

ntermos = int(input("Qual o numero de termos?"))

n1, n2 = 0, 1
contador = 0

print("Sequencia de Fibonacci:")

while contador < ntermos:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    contador += 1
