import itertools, random

deck = list(itertools.product(range(1,14),['kriting','wajik','hati','sekop',]))

random.shuffle(deck)
print('kamu mendapat : ')
for i in range(5):
    print(deck[i][0],' dari', deck[i][1])
