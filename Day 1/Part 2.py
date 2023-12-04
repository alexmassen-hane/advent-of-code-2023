import re

# with open("test_part2.txt", "r") as f_in:
with open("calibration_input.txt", "r") as f_in:
    calibrations = f_in.readlines()

word_lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum = 0
for cal in calibrations:
    items = re.findall(r"(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))", cal)

    first = word_lookup.get(items[0], items[0])
    last = word_lookup.get(items[-1], items[-1])

    sum += int(first + last)

print(f"Sum: {sum}")
