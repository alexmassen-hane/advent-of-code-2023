import re

with open("races.txt") as f_in:
    in_data = [line.rstrip() for line in f_in]

time = int("".join(re.findall(r"\d+", in_data[0].split(":")[1])))
distance = int("".join(re.findall(r"\d+", in_data[1].split(":")[1])))

count = 0
for charge_time in range(time):
    # charge_time is equal to charge_speed
    distance_travelled = (time - charge_time) * charge_time

    if distance_travelled > distance:
        count += 1

print(f"Number of ways to win: {count}")
