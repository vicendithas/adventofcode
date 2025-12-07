import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day6.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

operand1 = input_list[0].split()
operand2 = input_list[1].split()
operand3 = input_list[2].split()
operand4 = input_list[3].split()
operator = input_list[4].split()

total_p1 = 0

for i in range(len(operator)):
    if operator[i] == "+":
        total_p1 += int(operand1[i]) + int(operand2[i]) + int(operand3[i]) + int(operand4[i])
    else:
        total_p1 += int(operand1[i]) * int(operand2[i]) * int(operand3[i]) * int(operand4[i])

print(total_p1)

total_p2 = 0

operand1 = input_list[0]
operand2 = input_list[1]
operand3 = input_list[2]
operand4 = input_list[3]
operator = input_list[4]

start = 0
stop = 0

while(start < len(input_list[0])):
    while(operand1[stop] != " " or operand2[stop] != " " or operand3[stop] != " " or operand4[stop] != " " or operator[stop] != " "):
        stop += 1
        if stop == len(input_list[0]):
            break

    curr_operator = operator[start]
    curr_operands = []

    for i in range(start, stop, 1):
        temp_operand = (operand1[i] + operand2[i] + operand3[i] + operand4[i]).strip()
        curr_operands.append(int(temp_operand))

    temp_total = 0 if curr_operator == "+" else 1
    for i in range(len(curr_operands)):
        if curr_operator == "+":
            temp_total += curr_operands[i]
        else:
            temp_total *= curr_operands[i]
 
    total_p2 += temp_total

    start = stop + 1
    stop = stop + 1

print(total_p2)
