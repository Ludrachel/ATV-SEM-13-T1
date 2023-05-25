lis = []
par = []
impar = []

for i in range(20):
    n = int(input())
    lis.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(lis)
print(par)
print(impar)
