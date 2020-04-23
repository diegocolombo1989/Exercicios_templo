# lista = []
# numeros_lista_1 = 1

# while numeros_lista_1 > 0:
#     n = int(input('Digite numeros da primeira lista e digite 0 para terminar: '))
#     lista.append(n)
#     if n == 0:
#         print(lista)
#         break


# lista_2 = []
# numeros_lista_2 = 1

# while numeros_lista_2 > 0:
#     n = int(input('Digite numeros da segunda lista e digite 0 para terminar: '))
#     lista_2.append(n)
#     if n == 0:
#         print(lista)
#         break

# def soma(lista,lista_2):
    

# soma(lista,lista_2)


lista = []
for i in range(0,4):
    i = lista.append(int(input('Digite 4 numeros: ')))
print(max(lista))

lista_2 = []
for j in range(0,4):
    j = lista_2.append(int(input('Digite 4 numeros: ')))
print(max(lista_2))

def soma_listas(lista,lista_2): 
    soma = lista + lista_2
    print(soma)

soma_listas(f"{max(lista), max(lista_2)}")
