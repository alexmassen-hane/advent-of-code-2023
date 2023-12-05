import re
from concurrent.futures import ProcessPoolExecutor, as_completed

with open("almanac.txt") as f_in:
    in_data = [line.rstrip() for line in f_in]

# Parse the incoming data file and build a dictionary of the maps
maps = {}
seeds = [int(seed) for seed in in_data[0].rstrip().split(" ")[1:]]
seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
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


def find_lowest_from_seed_range(seed_range: range, maps) -> int:
    lowest = 9999999999999999999
    for seed in seed_range:
        item = seed
        for key in maps.keys():
            # Use the maps to find number of each item
            item = find_from_map(item, maps[key])

        lowest = item if item < lowest else lowest

    return lowest


locations = []
# Use parallel processing to make looping over all seeds faster.
with ProcessPoolExecutor() as executor:
    futures = []
    for seed_range in seed_ranges:
        futures.append(executor.submit(find_lowest_from_seed_range, seed_range, maps))
    for future in as_completed(futures):
        result = future.result()
        print(f"Finished seed_range: {seed_range} with local min = {result}")
        locations.append(result)

print(f"Lowest location: {min(locations)}")

# This brute force method worked but it's the dumb way of doing it. I will
# work on another way that will use a binary search instead and will put up a revised version.
