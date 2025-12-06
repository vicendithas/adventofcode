from operator import itemgetter

import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day5.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

id_ranges = []
id_avail = []

for input_item in input_list:
    if input_item != "":
        hyphen_index = input_item.find("-")
        if hyphen_index == -1:
            id_avail.append(int(input_item))
        else:
            id_start = int(input_item[:hyphen_index])
            id_stop = int(input_item[hyphen_index+1:])
            id_ranges.append([id_start, id_stop])

total_p1 = 0

for curr_avail in id_avail:
    available = False
    for [id_start, id_stop] in id_ranges:
        if (curr_avail >= id_start) and (curr_avail <= id_stop):
            available = True

    if available: total_p1 += 1

print(total_p1)

id_ranges.sort(key=itemgetter(0,1))

id_ranges_merged = []
id_ranges_merged.append(id_ranges[0])

for i in range(1, len(id_ranges)):
    last = id_ranges_merged[-1]
    curr = id_ranges[i]

    if curr[0] <= last[1]:
        last[1] = max(last[1], curr[1])
    else:
        id_ranges_merged.append(curr)

total_p2 = 0

for [curr_start, curr_stop] in id_ranges_merged:
    total_p2 += curr_stop - curr_start + 1

print(total_p2)