import re

with open("games.txt", "r") as f_in:
    games = f_in.readlines()

n_cubes = {"red": 12, "green": 13, "blue": 14}

sum = 0
for game in games:
    game_id = int(re.findall(r"\d+", game.split(":")[0])[0])
    print(game_id)

    # split for each round of the game, using the semi-colon
    game_work = True
    rounds = game.split(":")[-1].split(";")
    for round in rounds:
        # Loop over cubes
        cubes = round.split(",")
        for cube in cubes:
            if re.findall(r"red", cube):
                if int(re.findall(r"\d+", cube)[0]) > n_cubes["red"]:
                    game_work = False
                    print(f"Game id: {game_id} does not work!")

            if re.findall(r"green", cube):
                if int(re.findall(r"\d+", cube)[0]) > n_cubes["green"]:
                    game_work = False
                    print(f"Game id: {game_id} does not work!")

            if re.findall(r"blue", cube):
                if int(re.findall(r"\d+", cube)[0]) > n_cubes["blue"]:
                    game_work = False
                    print(f"Game id: {game_id} does not work!")

    # If it passes the checks, sum the game_id together
    if game_work:
        sum += game_id

print(f"Game id sum: {sum}")
