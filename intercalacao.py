lis_A = []
lis_B = []
lis_C = []

for i in range(25):
    n_A = int(input())
    lis_A.append(n_A)

for i in range(25):
    n_B = int(input())
    lis_B.append(n_B)

for i in range(25):
    lis_C.append(lis_A[i])
    lis_C.append(lis_B[i])

print(lis_A)
print(lis_B)
print(lis_C)
    
