num = int(input())
lis = []
for i in range(num):
    n = float(input())
    lis.append(n)
print(lis[::-1])

notas = []
soma = 0
for i in range(num):
    nota = float(input())
    notas.append(nota)
    soma += nota
print(notas)
if num != 0:
    media = round(soma/ num, 1)
    print(f'{media:.1f}')
if num == 0:
    print("SEM NOTAS")
letras = []
vogais = 0
consoantes = []
for i in range(num):
    caractere = input()[0]
    letras.append(caractere)
    if caractere.lower() in ['a','e','i','o','u']:
        vogais += 1
    else:
        consoantes.append(caractere)
print(vogais)
print(consoantes)
    
    
