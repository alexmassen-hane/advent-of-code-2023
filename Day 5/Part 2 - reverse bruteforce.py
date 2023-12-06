import re

with open("almanac.txt") as f_in:
    in_data = [line.rstrip() for line in f_in]

# Parse the incoming data file and build a dictionary of the maps
maps = {}
seeds = [int(seed) for seed in in_data[0].rstrip().split(" ")[1:]]
seed_ranges = [[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds), 2)]
for line in in_data[1:]:
    if re.match(r"(.+?)\s+map:", line):
        key = re.search(r"(.+?)\s+map:", line).group(1)
        maps[key] = []

    elif re.match(r"\d+\s\d+\s\d+", line):
        numbers = [int(i) for i in line.split(" ")]
        maps[key].append(numbers)


def dst_to_src(input, range_list):
    result = None
    for dst, src, rng in range_list:
        if dst <= input <= dst + rng - 1:
            result = abs(input - dst) + src
            break
    # Not in any of the ranges, same as input
    if result is None:
        result = input

    return result


location = 0
found = False
reverse_keys = list(maps.keys())[::-1]
while not found:
    seed = location
    for key in reverse_keys:
        seed = dst_to_src(seed, maps[key])

    for seed_start, seed_end in seed_ranges:
        if seed_start <= seed <= seed_end:
            found = True
            print(f"Lowest location found: {location} - seed = {seed}")
            break

    location += 1


# I'm still not happy with this reverse bruteforce method but it works much better and quicker than the forwards bruteforce.
