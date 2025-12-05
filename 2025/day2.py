import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day2.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

idrange_list = input_list[0].split(",")

def isInvalid(test_id, seg):
    id_len = len(test_id)

    if id_len % seg != 0:
        return False

    seg_len = int(id_len / seg)
    chunks = [test_id[i: i+seg_len] for i in range(0, id_len, seg_len)]

    invalid = True
    for i in range(len(chunks)-1):
        if chunks[i] != chunks[i+1]:
            invalid = False

    return invalid

total_p1 = 0
total_p2 = 0

for idrange in idrange_list:
    hyphen = idrange.index("-")
    id_start = int(idrange[:hyphen])
    id_stop = int(idrange[hyphen+1:])

    for curr_id in range(id_start, id_stop + 1, 1):
        if isInvalid(str(curr_id), 2):
            total_p1 += curr_id

        invalid = False
        for i in range(2, len(str(curr_id))+1, 1):
            if isInvalid(str(curr_id), i):
                invalid = True

        if invalid:
            total_p2 += curr_id
            
print(total_p1)
print(total_p2)

