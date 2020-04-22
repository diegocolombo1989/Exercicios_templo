lista = []
for i in range(0,3):
    numeros = int(input('Digite numeros: '))
    lista.append(numeros)
print(lista)

lista_2 = []
for i in range(0,3):
    numeros = int(input('Digite numeros: '))
    lista_2.append(numeros)
print(lista_2)

def soma(lista,lista_2): return max(lista) + max(lista_2)
    

soma(lista,lista_2)



