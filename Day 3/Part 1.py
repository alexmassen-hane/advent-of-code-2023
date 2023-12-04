import re

with open("engine_schematic.txt", "r") as f_in:
    matrix = [line.rstrip() for line in f_in]

# All possible symbols in the input data
# Found by scanning through the data first
reg_symbol = r"\@|\#|\&|\/|\+|\-|\*|\%|\=|\$"


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


numbers = []
for row_num in range(len(matrix)):
    for symbol in re.finditer(reg_symbol, matrix[row_num]):
        # This part loops from top down
        for sel in [-1, 0, 1]:
            numbers.extend(find_match_in_row(matrix[row_num + sel], symbol.start()))


print(f"Sum of all numbers: {sum(numbers)}")
