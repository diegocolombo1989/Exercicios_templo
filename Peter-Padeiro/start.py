cab = '#\t'*20
print(f'{cab}\n')
print('#\t                                                     COZINHA DO PETER                                                                           #\n')
print(f'{cab}')
print('\n'*2)

def bolos(receita,ingredientes): 
    receita_pronta = (0,1,2)
    print(f"Receita 1 -> \t BOLO DE FUBÁ \n\nIngredientes necessários: {receita}.\nIngredientes que Peter possui: {ingredientes}.\nQuantidade de bolos que conseguirá fazer: \n")
    return print(max(receita_pronta))

def bolos_2(receita, ingredientes):
    receita_pronta = (0,1,2)
    print(f"Receita 2 -> \t BOLO DE MAÇÃ \n\nIngredientes necessários: {receita}\nIngredientes que Peter possui: {ingredientes}.\nQuantidade de bolos que conseguirá fazer:  \n")
    return print(min(receita_pronta))

bolos({'farinha': 500, 'açúcar': 200, 'ovos': 1}, {'farinha': 1200, 'açúcar': 1200, 'ovos': 5, 'leite': 200})
print('\n'*2)
bolos_2({'maçãs': 3, 'farinha': 300, 'açúcar': 150, 'leite': 100, 'oleo': 100}, {'açúcar': 500, 'farinha': 2000, 'leite': 2000})