import re

with open("games.txt", "r") as f_in:
    games = f_in.readlines()

sum_power = 0
for game in games:
    game_id = int(re.findall(r"\d+", game.split(":")[0])[0])

    # split for each round of the game, using the semi-colon
    rounds = game.split(":")[-1].split(";")
    max_red = 0
    max_green = 0
    max_blue = 0
    for round in rounds:
        # Loop over cubes
        cubes = round.split(",")
        for cube in cubes:
            if re.findall(r"red", cube):
                max_red = max(int(re.findall(r"\d+", cube)[0]), max_red)

            if re.findall(r"green", cube):
                max_green = max(int(re.findall(r"\d+", cube)[0]), max_green)

            if re.findall(r"blue", cube):
                max_blue = max(int(re.findall(r"\d+", cube)[0]), max_blue)

    sum_power += max_red * max_green * max_blue

print(f"Power sum: {sum_power}")
