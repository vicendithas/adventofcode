import re

import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day7.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

manifold = []

# Lines with only . are redundant and can be skipped
s_split_re = r"[S^]"
for curr_line in input_list:
    if re.search(s_split_re, curr_line):
        temp_line = []
        for curr_pos in curr_line:
            temp_line.append(curr_pos)

        manifold.append(temp_line)

total_p1 = 0
total_p2 = 0

num_re = r"\d+"

# Find the start and advance down from there
for i in range(len(manifold[0])):
    if manifold[0][i] == "S":
        manifold[0][i] = "1"

for row in range(1, len(manifold)):
    # Run through each row twice
    # First to advance downward from existing beams if not on a splitter
    # Second to split if at a splitter and a beam is coming from above
    for col in range(len(manifold[row])):
        num_above = re.fullmatch(num_re, manifold[row-1][col])
        if manifold[row][col] == "." and num_above:
            manifold[row][col] = manifold[row-1][col]
        
    for col in range(len(manifold[row])):
        num_above = re.fullmatch(num_re, manifold[row-1][col])
        if manifold[row][col] == "^" and num_above:
            if manifold[row][col-1] == ".":
                manifold[row][col-1] = manifold[row-1][col]
            else:
                value = int(manifold[row-1][col]) + int(manifold[row][col-1])
                manifold[row][col-1] = str(value)
            
            if manifold[row][col+1] == ".":
                manifold[row][col+1] = manifold[row-1][col]
            else:
                value = int(manifold[row-1][col]) + int(manifold[row][col+1])
                manifold[row][col+1] = str(value)
            
            total_p1 += 1

for row in range(len(manifold)):
    tmp_str = ""
    for col in range(len(manifold[row])):
        tmp_str = tmp_str + str(manifold[row][col]) + ","
    print(tmp_str)


for curr_item in manifold[len(manifold)-1]:
    is_number = re.fullmatch(num_re, curr_item)
    if is_number:
        total_p2 += int(curr_item)

print(total_p1)
print(total_p2)