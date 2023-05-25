n = []
for i in range(10):
    numero = int(input())
    n.append(numero)
print(n)
soma = sum(n)
print(soma)
multiplicacao = 1
for numero in n:
    multiplicacao *= numero
print(multiplicacao)
