import re
import math

with open("engine_schematic.txt", "r") as f_in:
    matrix = [line.rstrip() for line in f_in]

# Symbol for the gear
reg_symbol = r"\*"


def find_match_in_row(input, position):
    results = []
    # This part loops through left to right
    for res in re.finditer(r"\d+", input):
        start, end = res.span()
        if position - 1 in range(start, end):
            results.append(int(input[start:end]))
        elif position in range(start, end):
            results.append(int(input[start:end]))
        elif position + 1 in range(start, end):
            results.append(int(input[start:end]))

    return results


total_sum = 0
for row_num in range(len(matrix)):
    for symbol in re.finditer(reg_symbol, matrix[row_num]):
        # This part loops from top down

        # All the numbers in the local group
        numbers = []
        for sel in [-1, 0, 1]:
            numbers.extend(find_match_in_row(matrix[row_num + sel], symbol.start()))

        # Require more than one gear for a ratio
        if len(numbers) > 1:
            total_sum += math.prod(numbers)

print(f"Sum of all numbers: {total_sum}")
