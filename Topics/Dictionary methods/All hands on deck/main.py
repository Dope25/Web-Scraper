cards = []
for _ in range(6):
    card = input()
    if card == 'Ace':
        card = 14
    elif card == 'King':
        card = 13
    elif card == 'Queen':
        card = 12
    elif card == 'Jack':
        card = 11
    cards.append(int(card))
print(sum(cards) / len(cards))
