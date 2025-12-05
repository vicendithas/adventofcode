import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day3.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

def maxDigit(bank):
    my_max = -1
    index = 0
    for i in range(len(bank)):
        curr_digit = int(bank[i])
        if curr_digit > my_max:
            my_max = curr_digit
            index = i

    return (my_max, index)

total_p1 = 0

for curr_bank in input_list:
    if curr_bank != "":
        (digit1, index1) = maxDigit(curr_bank[:-1])
        remaining = curr_bank[index1+1:]
        (digit2, index2) = maxDigit(remaining)

        joltage = (10 * int(digit1)) + int(digit2)
        total_p1 += joltage

print(total_p1)

total_p2 = 0

for curr_bank in input_list:
    if curr_bank != "":
        digits = []

        remaining = curr_bank
        for i in range(-11, 0, 1):
            (curr_digit, index) = maxDigit(remaining[:i])
            digits.append(curr_digit)
            remaining = remaining[index+1:]

        (curr_digit, index) = maxDigit(remaining)
        digits.append(curr_digit)

        joltage = 0
        for i in range(12):
            joltage += digits[i] * (10 ** (12-i-1))

        total_p2 += joltage

print(total_p2)
            
