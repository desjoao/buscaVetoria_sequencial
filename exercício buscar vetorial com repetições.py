def buscaVal (vetor, tam, valor):
    k = 0
    vet2 = [-1]*tam
    for i in range(tam):
        if vetor[i] == valor:
            vet2[k] = i
            k +=1
    return vet2

def leitura(tam):
    vetor = [0]*tam
    for i in range(tam):
        vetor[i] = int(input(f'Informe o {i +1}º valor positivo: '))
        if vetor[i] <0:
             vetor[i] = int(input(f'Informe o {i +1}º valor positivo: '))
    return vetor

vet = leitura(10)
n = int(input('Informe o valor que gostaria de encontrar: '))
val = buscaVal(vet, len(vet), n)
count = 0
for i in range(len(val)):
    if val[i] != -1:
        count+=1

res = [0]*count
for i in range(count):
    res[i] = val[i]
if count == 0:
    print(f'Não foi encontrado o valor desejado')
elif count == 1:
    print(f'O valor desejado foi encontrado {count} vez no vetor {vet}, estando na posição {res}.')

else:
    print(f'O valor desejado foi encontrado {count} vezes no vetor {vet}, estando nas posições {res}.')
