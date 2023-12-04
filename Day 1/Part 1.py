

import re
with open("calibration_input.txt", 'r') as f_in:    
    calibrations = f_in.readlines()

sum = 0
for cal in calibrations:

    digits = re.findall(r'\d+', cal)
    digits = "".join(digits)
    # print(digits)

    if len(digits) > 1:
        numbers = digits[0] + digits[-1]
        # print(numbers)
        sum += int(numbers)
    else:
        numbers = digits[0] + digits[0]
        # print(numbers)
        sum += int(numbers)

    # print(f"Part sum: {sum}")

print(f"Sum: {sum}")