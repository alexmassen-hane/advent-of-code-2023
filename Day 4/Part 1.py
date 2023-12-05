import re

with open("cards.txt") as f_in:
    cards = [line.rstrip() for line in f_in]

# Loop through all of the cards
sum_points = 0
for card in cards:
    # Pull out the winning and other available numbers for the card.
    winning = re.findall(r"\d+", card.split(":")[1].split("|")[0])
    all = re.findall(r"\d+", card.split(":")[1].split("|")[1])

    # Find if the winning numbers are in the list of all numbers, calculate points
    first = True
    points = 0
    for win in winning:
        if win in all:
            if first:
                points = 1
                first = False
            else:
                points = 2 * points

    # Sum the points of all cards together
    sum_points += points

print(f"Sum of all points: {sum_points}")
