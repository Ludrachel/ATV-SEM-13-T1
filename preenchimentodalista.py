num = int(input())
lis = []

lis = [0] * num
print(lis)

lis = list(range(1, num + 1))
print(lis)

lis = []
for i in range(num):
    numero = int(input())
    lis.insert(0, numero)
lis.reverse()
print(lis)

lis = []
for i in range(num):
    numero = int(input())
    lis.append(numero)
lis.reverse()
print(lis)
