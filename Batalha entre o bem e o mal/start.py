import time
cab1 = '--'*85
cab = '\t -='* 20
print(cab)
print('\t\n         -=                                                      BATALHA ENTRE O BEM E O MAL                                                                     -=\n')
print(cab)

print('\n')
print('\t\t\t\t EXÉRCITO DO BEM\n')
def bem():
    bem = []
    hobbits = bem.append(int(input('\tQuantidade de hobbits: \t'))) #1
    homens = bem.append(int(input('\tQuantidade de homens: \t'))) #2
    elfos = bem.append(int(input('\tQuantidade de elfos: \t'))) #3
    anoes = bem.append(int(input('\tQuantidade de anoes: \t'))) #3
    eagles = bem.append(int(input('\tQuantidade de águias: \t'))) #4
    assistentes = bem.append(int(input('\tQuantidade de magos: \t'))) #10
    print(f"\tHobbits: {bem[0]*1}, Homens: {bem[1]*2}, Elfos: {bem[2]*3}, Anões: {bem[3]*3}, Águias: {bem[4]*4}, Magos: {bem[5]*10}\n")
    soma = f"{sum((bem[0]*1, bem[1]*2, bem[2]*3, bem[3]*3, bem[4]*4, bem[5]*10))}"
    return soma


exercito_bem = bem()


print('\n')
print('\t\t\t\t EXÉRCITO DO MAL\n')


def mal():
    mal = []
    orcs = mal.append(int(input('\tQuantidade de orcs: \t'))) #1
    homens = mal.append(int(input('\tQuantidade de homens: \t'))) #2
    wargs = mal.append(int(input('\tQuantidade de wargs: \t'))) #2
    goblins = mal.append(int(input('\tQuantidade de goblins: \t'))) #2
    urukhai = mal.append(int(input('\tQuantidade de Uruk Hais: '))) #3
    trolls = mal.append(int(input('\tQuantidade de trolls: \t'))) #5
    assistentes = mal.append(int(input('\tQuantidade de magos: \t'))) #10
    print(f"\tOrcs: {mal[0]*1}, Homens: {mal[1]*2}, Wargs: {mal[2]*2}, Goblins: {mal[3]*2}, Uruh-Khais: {mal[4]*3}, Trolls: {mal[5]*5}, Magos: {mal[6]*10}\n")
    soma = f"{sum((mal[0]*1, mal[1]*2, mal[2]*2, mal[3]*2, mal[4]*3, mal[5]*5, mal[6]*10))}"
    return soma


exercito_mal = mal()

print(f" \n\n\t\t\t\t A BATALHA COMEÇA ... \n\n{cab1}\n")
time.sleep(5)


def battle(exercito_bem, exercito_mal):
    print(f"\t\t\t O PODER DO EXÉRCITO DO BEM É DE ->\t{exercito_bem}\n\t\t\t O PODER DO EXÉRCITO DO MAL É DE ->\t{exercito_mal}")
    if exercito_bem > exercito_mal:
        print("\n\t\t\t O BEM TRIUNFA SOBRE O MAL \n")
    else:
        print("\n\t\t\t O MAL ERRADICA TODOS OS VESTÍGIOS DO BEM \n")
    
    print(f"\n\t\t\t\t FIM DA BATALHA \n{cab1}")
    
    
battle(exercito_bem, exercito_mal)

