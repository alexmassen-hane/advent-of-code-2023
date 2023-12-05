import re

with open("almanac.txt") as f_in:
    in_data = [line.rstrip() for line in f_in]

# Parse the incoming data file and build a dictionary of the maps
maps = {}
seeds = [int(seed) for seed in in_data[0].rstrip().split(" ")[1:]]
for line in in_data[1:]:
    if re.match(r"(.+?)\s+map:", line):
        key = re.search(r"(.+?)\s+map:", line).group(1)
        maps[key] = []

    elif re.match(r"\d+\s\d+\s\d+", line):
        numbers = [int(i) for i in line.split(" ")]
        maps[key].append(numbers)


def find_from_map(input, range_list):
    result = None
    for num in range_list:
        if input in range(num[1], num[1] + num[2]):
            result = abs(input - num[1]) + num[0]
            break
    # Not in any of the ranges, same as input
    if result is None:
        result = input

    return result


# Loop over all the seeds
locations = []
for seed in seeds:
    item = seed
    for key in maps.keys():
        # Use the maps to find number of each item
        item = find_from_map(item, maps[key])

    # Make a list of all locations.
    locations.append(item)

print(f"Lowest location: {min(locations)}")
