import time

cab = '-='*90
print(f'{cab}\n')
print('\t                                                                     Monkeys Count\n')
print(f'{cab}\n')

n = int(input('Dad, say the total of monkeys ... \n'))
print("Let's count, little monkey ...  ")
monkeyCount = list(range(1, n + 1))
for i in monkeyCount:
    print(f'{i} ... ')
    time.sleep(1)
print(f'{monkeyCount}\n')
print(f"There're {len(monkeyCount)} monkeys at the florest. ")