import re

with open("cards.txt") as f_in:
    cards = [line.rstrip() for line in f_in]

# Pre define cards numbers. Start out all as 1.
num_cards = {i: 1 for i in range(1, len(cards) + 1, 1)}

# Loop through all of the cards
sum_points = 0
for card in cards:
    card_id = int(re.findall(r"\d+", card.split(":")[0])[0])

    # Pull out the winning and other available numbers for the card.
    winning = re.findall(r"\d+", card.split(":")[1].split("|")[0])
    all = re.findall(r"\d+", card.split(":")[1].split("|")[1])

    # Find cards ahead to add onto other cards
    count = 1
    for win in winning:
        if win in all:
            num_cards[card_id + count] += num_cards[card_id]
            count += 1

print(f"Sum of all cards: {sum(num_cards.values())}")
