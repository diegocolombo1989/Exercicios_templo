cab = '::'*100
print(cab,'\n')
print('\t'*9,'- MAIOR SOMA DE PARES NA MATRIZ - \n')
print(cab,'\n')
cab2 = '--'*50

primeira_lista = []
for i in range(0,5):
    i = primeira_lista.append(int(input('\tDigite os números: \t')))
print(f"\n O maior número da lista digitada é: {max(primeira_lista)}",'\n',cab2,'\n')

segunda_lista = []
for j in range(0,5):
    j = segunda_lista.append(int(input('\tDigite os números: \t')))
print(f"\n O maior número da lista digitada é: {max(segunda_lista)}",'\n',cab2,'\n')

def soma_listas(lista,lista_2): 
    soma = max(primeira_lista) + max(segunda_lista)
    print(f" O resultado da soma entre os maiores números é: {soma}\n")
    print(cab2)


soma_listas(primeira_lista, segunda_lista)
print('\t'*9,'             - FIM - ')